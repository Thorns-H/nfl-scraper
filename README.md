# 🏈 NFL-Scraper

I use the [Football Database](https://www.footballdb.com/) to get information about a specific week on the National Football League, this information can be used to analyze
the matches.

Example from a match data from the 2024 regular season.

```
python3 main.py year=2024 week=11 type=reg
```

## output.json

```
[
    {
        "match_number": 1,
        "away_team": {
            "url": "/teams/nfl/washington-commanders",
            "rankings": {
                "Yds/Game": {
                    "offense": "377.0 (4th)",
                    "defense": "324.9 (14th)"
                },
                "Rush Yds/Game": {
                    "offense": "153.5 (4th)",
                    "defense": "142.7 (28th)"
                },
                "Pass Yds/Game": {
                    "offense": "223.5 (11th)",
                    "defense": "182.2 (5th)"
                },
                "Pts/Game": {
                    "offense": "29.0 (3rd)",
                    "defense": "21.7 (12th)"
                }
            }
        },
        "home_team": {
            "url": "/teams/nfl/philadelphia-eagles",
            "rankings": {
                "Yds/Game": {
                    "offense": "373.9 (6th)",
                    "defense": "274.1 (2nd)"
                },
                "Rush Yds/Game": {
                    "offense": "176.1 (2nd)",
                    "defense": "100.7 (5th)"
                },
                "Pass Yds/Game": {
                    "offense": "197.8 (20th)",
                    "defense": "173.4 (3rd)"
                },
                "Pts/Game": {
                    "offense": "25.9 (7th)",
                    "defense": "17.9 (5th)"
                }
            }
        },
        "history": "/teams/nfl/philadelphia-eagles/teamvsteam?opp=32",
        "games": [
            {
                "date": "10/29/2023",
                "visitor_team": "Philadelphia Eagles",
                "visitor_score": "38",
                "home_team": "Washington Commanders",
                "home_score": "31",
                "result": "W"
            },
            {
                "date": "10/01/2023",
                "visitor_team": "Washington Commanders",
                "visitor_score": "31",
                "home_team": "Philadelphia Eagles",
                "home_score": "34",
                "result": "W/OT"
            },
            {
                "date": "11/14/2022",
                "visitor_team": "Washington Commanders",
                "visitor_score": "32",
                "home_team": "Philadelphia Eagles",
                "home_score": "21",
                "result": "L"
            },
            {
                "date": "09/25/2022",
                "visitor_team": "Philadelphia Eagles",
                "visitor_score": "24",
                "home_team": "Washington Commanders",
                "home_score": "8",
                "result": "W"
            },
            {
                "date": "01/02/2022",
                "visitor_team": "Philadelphia Eagles",
                "visitor_score": "20",
                "home_team": "Washington Football Team",
                "home_score": "16",
                "result": "W"
            }
        ]
    }
]
```
