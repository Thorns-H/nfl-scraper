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
        url_list = response.css('a::attr(href)').getall()
        filter_index = url_list.index(f'/scores/index.html?lg=NFL&yr={self.year}&type={self.type}&wk=18')
        filtered_url_list = url_list[filter_index + 1:-4]

        tables = response.css('table')
        url_index = 0

        for i, table in enumerate(tables, start=1):
            match_data = {
                "match_number": i,
                "away_team": filtered_url_list[url_index] if url_index < len(filtered_url_list) else None,
                "home_team": filtered_url_list[url_index + 1] if url_index + 1 < len(filtered_url_list) else None,
                "history": filtered_url_list[url_index + 3] if url_index + 3 < len(filtered_url_list) else None
            }
            self.data_to_json.append(match_data)

            away_url = response.urljoin(match_data["away_team"])
            home_url = response.urljoin(match_data["home_team"])
            history_url = response.urljoin(match_data["history"])
            
            yield scrapy.Request(away_url, callback=self.parse_team, meta={'match_data': match_data, 'team_type': 'away_team'})
            yield scrapy.Request(home_url, callback=self.parse_team, meta={'match_data': match_data, 'team_type': 'home_team'})
            yield scrapy.Request(history_url, callback=self.parse_history, meta={'match_data': match_data})

            url_index += 4

    def parse_team(self, response):
        match_data = response.meta['match_data']
        team_type = response.meta['team_type']

        rankings_table = response.css('div.section_third table')
        stats = {}

        for row in rankings_table.css('tr'):
            category = row.css('td:nth-child(1)::text').get()
            offense = row.css('td:nth-child(2)::text').get()
            defense = row.css('td:nth-child(3)::text').get()
            if category and offense and defense:
                stats[category.strip()] = {"offense": offense.strip(), "defense": defense.strip()}

        match_data[team_type] = {
            "url": match_data[team_type],
            "rankings": stats
        }

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
