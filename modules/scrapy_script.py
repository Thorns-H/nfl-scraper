import json
import scrapy
from scrapy.crawler import CrawlerProcess

class custom_spider(scrapy.Spider):
    name = 'football_scraper'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'LOG_LEVEL': 'ERROR'
    }

    def __init__(self, arguments: dict) -> None:
        super(custom_spider, self).__init__()
        self.year = arguments['year']
        self.week = arguments['week']
        self.type = arguments['type']
        self.start_urls = [f'https://www.footballdb.com/scores/index.html?lg=NFL&yr={self.year}&type={self.type}&wk={self.week}']
        self.data_to_json = []

    def parse(self, response):
        team_urls = response.xpath('//table//a[starts-with(@href, "/teams/nfl/") and not(contains(@href, "teamvsteam"))]/@href').getall()
        team_urls = list(dict.fromkeys(team_urls))
        
        history_urls = response.xpath('//a[contains(@href, "teamvsteam?opp=")]/@href').getall()

        tables = response.css('table')
        match_count = min(len(team_urls) // 2, len(history_urls))

        for i in range(match_count):
            match_data = {
                "match_number": i + 1,
                "away_team": team_urls[i * 2] if i * 2 < len(team_urls) else None,
                "home_team": team_urls[i * 2 + 1] if i * 2 + 1 < len(team_urls) else None,
                "history": history_urls[i] if i < len(history_urls) else None
            }
            self.data_to_json.append(match_data)

            away_url = response.urljoin(match_data["away_team"])
            home_url = response.urljoin(match_data["home_team"])
            history_url = response.urljoin(match_data["history"])

            yield scrapy.Request(away_url, callback=self.parse_team, meta={'match_data': match_data, 'team_type': 'away_team'})
            yield scrapy.Request(home_url, callback=self.parse_team, meta={'match_data': match_data, 'team_type': 'home_team'})
            if match_data["history"]:
                yield scrapy.Request(history_url, callback=self.parse_history, meta={'match_data': match_data})

    def parse_team(self, response):
        match_data = response.meta['match_data']
        team_type = response.meta['team_type']

        # Extract rankings as usual
        rankings_table = response.css('div.section_third table')
        rankings = {}

        for row in rankings_table.css('tr'):
            category = row.css('td:nth-child(1)::text').get()
            offense = row.css('td:nth-child(2)::text').get()
            defense = row.css('td:nth-child(3)::text').get()
            if category and offense and defense:
                rankings[category.strip()] = {"offense": offense.strip(), "defense": defense.strip()}

        # Update match data with rankings
        match_data[team_type] = {
            "url": match_data[team_type],
            "rankings": rankings
        }

        # Construct the stats URL for the team
        team_url = match_data[team_type]["url"]
        team_name = team_url.split('/')[-1]  # Extract team name from URL
        stats_url = f"https://www.footballdb.com/teams/nfl/{team_name}/stats/{self.year}?type={self.type}"
        
        # Make a request to fetch the statistics page
        yield scrapy.Request(stats_url, callback=self.parse_team_stats, meta={'match_data': match_data, 'team_type': team_type})

    def parse_team_stats(self, response):
        match_data = response.meta['match_data']
        team_type = response.meta['team_type']

        # Extract the first three tables for passing, rushing, and receiving statistics
        stats_tables = response.css('table')[:3]
        stats_categories = ['passing', 'rushing', 'receiving']
        stats_data = {}

        for i, table in enumerate(stats_tables):
            category_name = stats_categories[i]
            category_data = []

            # Extract headers to use as keys
            headers = [header.get().strip() for header in table.css('tr th::text')]

            # Extract rows, ensuring player names are captured without href
            for row in table.css('tr')[1:]:  # Skip header row
                player_data = {}
                for j, cell in enumerate(row.css('td')):
                    # Get the plain text or the text from an <a> tag if it exists
                    cell_text = cell.css('::text').get() or cell.css('a::text').get()
                    if cell_text:
                        player_data[headers[j]] = cell_text.strip()
                if player_data:
                    category_data.append(player_data)

            # Add category data to stats_data
            stats_data[category_name] = category_data

        # Add the structured stats data to match_data under the appropriate team
        match_data[team_type]["statistics"] = stats_data

        # Print stats to confirm they're correctly formatted
        print(f"Statistics for {team_type} (Match {match_data['match_number']}):")
        for category, players in stats_data.items():
            print(f"\n{category.capitalize()} Stats:")
            for player in players:
                print(player)

        # Save JSON output if all data is gathered
        if "rankings" in match_data["away_team"] and "rankings" in match_data["home_team"] and "games" in match_data:
            with open("output.json", "w") as f:
                json.dump(self.data_to_json, f, indent=4)


    def parse_history(self, response):
        match_data = response.meta['match_data']
        games = []

        rows = response.css('table.tvttable tbody tr')[:5]
        for row in rows:
            date = row.css('td:nth-child(1) span.hidden-xs::text').get()
            visitor_team = row.css('td:nth-child(2) span.hidden-xs::text').get()
            visitor_score = row.css('td:nth-child(3)::text').get()
            home_team = row.css('td:nth-child(5) span.hidden-xs::text').get()
            home_score = row.css('td:nth-child(6)::text').get()
            result = row.css('td:nth-child(7) b::text').get()

            if date and visitor_team and visitor_score and home_team and home_score and result:
                games.append({
                    "date": date.strip(),
                    "visitor_team": visitor_team.strip(),
                    "visitor_score": visitor_score.strip(),
                    "home_team": home_team.strip(),
                    "home_score": home_score.strip(),
                    "result": result.strip()
                })
                
        match_data["games"] = games

        if "rankings" in match_data["away_team"] and "rankings" in match_data["home_team"]:
            with open("output.json", "w") as f:
                json.dump(self.data_to_json, f, indent=4)
