# 🏈 NFL-Scraper

I use the [Football Database](https://www.footballdb.com/) to get information about a specific week on the National Football League, this information can be used to analyze
the matches.

Example from a match data from the 2024 regular season.

## Simple front-end to show the information

https://github.com/user-attachments/assets/c2184ee5-d67d-4421-a627-84b960bda844

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
            },
            "statistics": {
                "passing": [
                    {
                        "Player": "Jayden Daniels",
                        "Att": "262",
                        "Cmp": "180",
                        "Pct": "68.7",
                        "Yds": "2,147",
                        "YPA": "8.2",
                        "TD": "9",
                        "TD%": "3.4",
                        "Int": "2",
                        "Int%": "0.8",
                        "Lg": "66",
                        "Sack": "20",
                        "Loss": "111",
                        "Rate": "101.7"
                    },
                    {
                        "Player": "Marcus Mariota",
                        "Att": "26",
                        "Cmp": "19",
                        "Pct": "73.1",
                        "Yds": "203",
                        "YPA": "7.8",
                        "TD": "2",
                        "TD%": "7.7",
                        "Int": "0",
                        "Int%": "0.0",
                        "Lg": "25",
                        "Sack": "1",
                        "Loss": "4",
                        "Rate": "121.2"
                    },
                    {
                        "Player": "Washington",
                        "Att": "288",
                        "Cmp": "199",
                        "Pct": "69.1",
                        "Yds": "2,350",
                        "YPA": "8.2",
                        "TD": "11",
                        "TD%": "3.8",
                        "Int": "2",
                        "Int%": "0.7",
                        "Lg": "66",
                        "Sack": "21",
                        "Loss": "115",
                        "Rate": "103.5"
                    },
                    {
                        "Player": "Opponents",
                        "Att": "270",
                        "Cmp": "178",
                        "Pct": "65.9",
                        "Yds": "1,986",
                        "YPA": "7.4",
                        "TD": "17",
                        "TD%": "6.3",
                        "Int": "4",
                        "Int%": "1.5",
                        "Lg": "44",
                        "Sack": "27",
                        "Loss": "164",
                        "Rate": "102.5"
                    }
                ],
                "rushing": [
                    {
                        "Player": "Jayden Daniels",
                        "Gms": "10",
                        "Att": "85",
                        "Yds": "464",
                        "Avg": "5.46",
                        "YPG": "46.4",
                        "Lg": "46",
                        "TD": "4",
                        "FD": "29"
                    },
                    {
                        "Player": "Brian Robinson",
                        "Gms": "7",
                        "Att": "101",
                        "Yds": "461",
                        "Avg": "4.56",
                        "YPG": "65.9",
                        "Lg": "40",
                        "TD": "6",
                        "FD": "27"
                    },
                    {
                        "Player": "Austin Ekeler",
                        "Gms": "9",
                        "Att": "63",
                        "Yds": "326",
                        "Avg": "5.17",
                        "YPG": "36.2",
                        "Lg": "50",
                        "TD": "4",
                        "FD": "17"
                    },
                    {
                        "Player": "Jeremy McNichols",
                        "Gms": "10",
                        "Att": "38",
                        "Yds": "190",
                        "Avg": "5.00",
                        "YPG": "19.0",
                        "Lg": "28",
                        "TD": "4",
                        "FD": "10"
                    },
                    {
                        "Player": "Christopher Rodriguez",
                        "Gms": "4",
                        "Att": "13",
                        "Yds": "56",
                        "Avg": "4.31",
                        "YPG": "14.0",
                        "Lg": "17",
                        "TD": "0",
                        "FD": "3"
                    },
                    {
                        "Player": "Marcus Mariota",
                        "Gms": "2",
                        "Att": "13",
                        "Yds": "36",
                        "Avg": "2.77",
                        "YPG": "18.0",
                        "Lg": "11",
                        "TD": "0",
                        "FD": "3"
                    },
                    {
                        "Player": "Terry McLaurin",
                        "Gms": "10",
                        "Att": "2",
                        "Yds": "2",
                        "Avg": "1.00",
                        "YPG": "0.2",
                        "Lg": "2",
                        "TD": "0",
                        "FD": "0"
                    },
                    {
                        "Player": "Washington",
                        "Gms": "10",
                        "Att": "315",
                        "Yds": "1,535",
                        "Avg": "4.87",
                        "YPG": "153.5",
                        "Lg": "50",
                        "TD": "18",
                        "FD": "89"
                    },
                    {
                        "Player": "Opponents",
                        "Gms": "10",
                        "Att": "294",
                        "Yds": "1,427",
                        "Avg": "4.85",
                        "YPG": "142.7",
                        "Lg": "56t",
                        "TD": "10",
                        "FD": "79"
                    }
                ],
                "receiving": [
                    {
                        "Player": "Terry McLaurin",
                        "Gms": "10",
                        "Rec": "47",
                        "Yds": "711",
                        "Avg": "15.13",
                        "YPG": "71.1",
                        "Lg": "66",
                        "TD": "6",
                        "FD": "35",
                        "Tar": "66",
                        "YAC": "170"
                    },
                    {
                        "Player": "Zach Ertz",
                        "Gms": "10",
                        "Rec": "37",
                        "Yds": "381",
                        "Avg": "10.30",
                        "YPG": "38.1",
                        "Lg": "24",
                        "TD": "1",
                        "FD": "19",
                        "Tar": "54",
                        "YAC": "88"
                    },
                    {
                        "Player": "Noah Brown",
                        "Gms": "8",
                        "Rec": "25",
                        "Yds": "351",
                        "Avg": "14.04",
                        "YPG": "43.9",
                        "Lg": "52t",
                        "TD": "1",
                        "FD": "16",
                        "Tar": "38",
                        "YAC": "49"
                    },
                    {
                        "Player": "Austin Ekeler",
                        "Gms": "9",
                        "Rec": "23",
                        "Yds": "255",
                        "Avg": "11.09",
                        "YPG": "28.3",
                        "Lg": "33",
                        "TD": "0",
                        "FD": "10",
                        "Tar": "27",
                        "YAC": "293"
                    },
                    {
                        "Player": "Olamide Zaccheaus",
                        "Gms": "10",
                        "Rec": "22",
                        "Yds": "232",
                        "Avg": "10.55",
                        "YPG": "23.2",
                        "Lg": "42",
                        "TD": "0",
                        "FD": "12",
                        "Tar": "32",
                        "YAC": "147"
                    },
                    {
                        "Player": "Dyami Brown",
                        "Gms": "10",
                        "Rec": "13",
                        "Yds": "145",
                        "Avg": "11.15",
                        "YPG": "14.5",
                        "Lg": "41t",
                        "TD": "1",
                        "FD": "7",
                        "Tar": "18",
                        "YAC": "94"
                    },
                    {
                        "Player": "Luke McCaffrey",
                        "Gms": "10",
                        "Rec": "13",
                        "Yds": "134",
                        "Avg": "10.31",
                        "YPG": "13.4",
                        "Lg": "30",
                        "TD": "0",
                        "FD": "6",
                        "Tar": "16",
                        "YAC": "63"
                    },
                    {
                        "Player": "Brian Robinson",
                        "Gms": "7",
                        "Rec": "9",
                        "Yds": "79",
                        "Avg": "8.78",
                        "YPG": "11.3",
                        "Lg": "32",
                        "TD": "0",
                        "FD": "2",
                        "Tar": "12",
                        "YAC": "102"
                    },
                    {
                        "Player": "John Bates",
                        "Gms": "10",
                        "Rec": "3",
                        "Yds": "34",
                        "Avg": "11.33",
                        "YPG": "3.4",
                        "Lg": "20",
                        "TD": "0",
                        "FD": "1",
                        "Tar": "5",
                        "YAC": "25"
                    },
                    {
                        "Player": "Ben Sinnott",
                        "Gms": "10",
                        "Rec": "3",
                        "Yds": "18",
                        "Avg": "6.00",
                        "YPG": "1.8",
                        "Lg": "12",
                        "TD": "1",
                        "FD": "2",
                        "Tar": "3",
                        "YAC": "14"
                    },
                    {
                        "Player": "Jamison Crowder",
                        "Gms": "2",
                        "Rec": "1",
                        "Yds": "5",
                        "Avg": "5.00",
                        "YPG": "2.5",
                        "Lg": "5",
                        "TD": "0",
                        "FD": "0",
                        "Tar": "1",
                        "YAC": "8"
                    },
                    {
                        "Player": "Jeremy McNichols",
                        "Gms": "10",
                        "Rec": "1",
                        "Yds": "6",
                        "Avg": "6.00",
                        "YPG": "0.6",
                        "Lg": "6",
                        "TD": "0",
                        "FD": "0",
                        "Tar": "2",
                        "YAC": "9"
                    },
                    {
                        "Player": "Trenton Scott",
                        "Gms": "10",
                        "Rec": "1",
                        "Yds": "1",
                        "Avg": "1.00",
                        "YPG": "0.1",
                        "Lg": "1t",
                        "TD": "1",
                        "FD": "1",
                        "Tar": "1",
                        "YAC": "0"
                    },
                    {
                        "Player": "Brycen Tremayne",
                        "Gms": "1",
                        "Rec": "1",
                        "Yds": "-2",
                        "Avg": "-2.00",
                        "YPG": "-2.0",
                        "Lg": "-2",
                        "TD": "0",
                        "FD": "0",
                        "Tar": "1",
                        "YAC": "0"
                    },
                    {
                        "Player": "Washington",
                        "Gms": "10",
                        "Rec": "199",
                        "Yds": "2,350",
                        "Avg": "11.81",
                        "YPG": "235.0",
                        "Lg": "66",
                        "TD": "11",
                        "FD": "111",
                        "Tar": "276",
                        "YAC": "1,062"
                    },
                    {
                        "Player": "Opponents",
                        "Gms": "10",
                        "Rec": "178",
                        "Yds": "1,986",
                        "Avg": "11.16",
                        "YPG": "198.6",
                        "Lg": "44",
                        "TD": "17",
                        "FD": "102",
                        "Tar": "260",
                        "YAC": "899"
                    }
                ]
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
            },
            "statistics": {
                "passing": [
                    {
                        "Player": "Jalen Hurts",
                        "Att": "235",
                        "Cmp": "164",
                        "Pct": "69.8",
                        "Yds": "1,976",
                        "YPA": "8.4",
                        "TD": "12",
                        "TD%": "5.1",
                        "Int": "5",
                        "Int%": "2.1",
                        "Lg": "67t",
                        "Sack": "26",
                        "Loss": "193",
                        "Rate": "103.4"
                    },
                    {
                        "Player": "Kenny Pickett",
                        "Att": "3",
                        "Cmp": "1",
                        "Pct": "33.3",
                        "Yds": "5",
                        "YPA": "1.7",
                        "TD": "0",
                        "TD%": "0.0",
                        "Int": "0",
                        "Int%": "0.0",
                        "Lg": "5",
                        "Sack": "1",
                        "Loss": "8",
                        "Rate": "42.4"
                    },
                    {
                        "Player": "Philadelphia",
                        "Att": "238",
                        "Cmp": "165",
                        "Pct": "69.3",
                        "Yds": "1,981",
                        "YPA": "8.3",
                        "TD": "12",
                        "TD%": "5.0",
                        "Int": "5",
                        "Int%": "2.1",
                        "Lg": "67t",
                        "Sack": "27",
                        "Loss": "201",
                        "Rate": "102.6"
                    },
                    {
                        "Player": "Opponents",
                        "Att": "285",
                        "Cmp": "173",
                        "Pct": "60.7",
                        "Yds": "1,732",
                        "YPA": "6.1",
                        "TD": "8",
                        "TD%": "2.8",
                        "Int": "6",
                        "Int%": "2.1",
                        "Lg": "70t",
                        "Sack": "25",
                        "Loss": "171",
                        "Rate": "78.6"
                    }
                ],
                "rushing": [
                    {
                        "Player": "Saquon Barkley",
                        "Gms": "9",
                        "Att": "171",
                        "Yds": "991",
                        "Avg": "5.80",
                        "YPG": "110.1",
                        "Lg": "65t",
                        "TD": "6",
                        "FD": "39"
                    },
                    {
                        "Player": "Jalen Hurts",
                        "Gms": "9",
                        "Att": "93",
                        "Yds": "378",
                        "Avg": "4.06",
                        "YPG": "42.0",
                        "Lg": "24",
                        "TD": "10",
                        "FD": "40"
                    },
                    {
                        "Player": "Kenny Gainwell",
                        "Gms": "9",
                        "Att": "38",
                        "Yds": "154",
                        "Avg": "4.05",
                        "YPG": "17.1",
                        "Lg": "19",
                        "TD": "0",
                        "FD": "7"
                    },
                    {
                        "Player": "Will Shipley",
                        "Gms": "9",
                        "Att": "19",
                        "Yds": "46",
                        "Avg": "2.42",
                        "YPG": "5.1",
                        "Lg": "9",
                        "TD": "0",
                        "FD": "1"
                    },
                    {
                        "Player": "Jahan Dotson",
                        "Gms": "9",
                        "Att": "1",
                        "Yds": "13",
                        "Avg": "13.00",
                        "YPG": "1.4",
                        "Lg": "13",
                        "TD": "0",
                        "FD": "1"
                    },
                    {
                        "Player": "Ainias Smith",
                        "Gms": "3",
                        "Att": "1",
                        "Yds": "2",
                        "Avg": "2.00",
                        "YPG": "0.7",
                        "Lg": "2",
                        "TD": "0",
                        "FD": "0"
                    },
                    {
                        "Player": "Kenny Pickett",
                        "Gms": "2",
                        "Att": "1",
                        "Yds": "1",
                        "Avg": "1.00",
                        "YPG": "0.5",
                        "Lg": "1",
                        "TD": "0",
                        "FD": "1"
                    },
                    {
                        "Player": "Philadelphia",
                        "Gms": "9",
                        "Att": "324",
                        "Yds": "1,585",
                        "Avg": "4.89",
                        "YPG": "176.1",
                        "Lg": "65t",
                        "TD": "16",
                        "FD": "89"
                    },
                    {
                        "Player": "Opponents",
                        "Gms": "9",
                        "Att": "208",
                        "Yds": "906",
                        "Avg": "4.36",
                        "YPG": "100.7",
                        "Lg": "33t",
                        "TD": "6",
                        "FD": "52"
                    }
                ],
                "receiving": [
                    {
                        "Player": "DeVonta Smith",
                        "Gms": "8",
                        "Rec": "37",
                        "Yds": "487",
                        "Avg": "13.16",
                        "YPG": "60.9",
                        "Lg": "46",
                        "TD": "4",
                        "FD": "23",
                        "Tar": "50",
                        "YAC": "168"
                    },
                    {
                        "Player": "A.J. Brown",
                        "Gms": "6",
                        "Rec": "28",
                        "Yds": "553",
                        "Avg": "19.75",
                        "YPG": "92.2",
                        "Lg": "67t",
                        "TD": "3",
                        "FD": "23",
                        "Tar": "41",
                        "YAC": "171"
                    },
                    {
                        "Player": "Dallas Goedert",
                        "Gms": "6",
                        "Rec": "26",
                        "Yds": "326",
                        "Avg": "12.54",
                        "YPG": "54.3",
                        "Lg": "61",
                        "TD": "1",
                        "FD": "10",
                        "Tar": "32",
                        "YAC": "174"
                    },
                    {
                        "Player": "Saquon Barkley",
                        "Gms": "9",
                        "Rec": "21",
                        "Yds": "158",
                        "Avg": "7.52",
                        "YPG": "17.6",
                        "Lg": "27",
                        "TD": "2",
                        "FD": "9",
                        "Tar": "26",
                        "YAC": "132"
                    },
                    {
                        "Player": "Grant Calcaterra",
                        "Gms": "9",
                        "Rec": "17",
                        "Yds": "216",
                        "Avg": "12.71",
                        "YPG": "24.0",
                        "Lg": "34",
                        "TD": "0",
                        "FD": "12",
                        "Tar": "19",
                        "YAC": "116"
                    },
                    {
                        "Player": "Jahan Dotson",
                        "Gms": "9",
                        "Rec": "8",
                        "Yds": "98",
                        "Avg": "12.25",
                        "YPG": "10.9",
                        "Lg": "36",
                        "TD": "0",
                        "FD": "5",
                        "Tar": "15",
                        "YAC": "26"
                    },
                    {
                        "Player": "Britain Covey",
                        "Gms": "3",
                        "Rec": "7",
                        "Yds": "34",
                        "Avg": "4.86",
                        "YPG": "11.3",
                        "Lg": "11",
                        "TD": "0",
                        "FD": "2",
                        "Tar": "7",
                        "YAC": "28"
                    },
                    {
                        "Player": "Parris Campbell",
                        "Gms": "4",
                        "Rec": "6",
                        "Yds": "30",
                        "Avg": "5.00",
                        "YPG": "7.5",
                        "Lg": "7",
                        "TD": "1",
                        "FD": "1",
                        "Tar": "7",
                        "YAC": "9"
                    },
                    {
                        "Player": "Kenny Gainwell",
                        "Gms": "9",
                        "Rec": "6",
                        "Yds": "43",
                        "Avg": "7.17",
                        "YPG": "4.8",
                        "Lg": "11",
                        "TD": "0",
                        "FD": "2",
                        "Tar": "10",
                        "YAC": "34"
                    },
                    {
                        "Player": "Ainias Smith",
                        "Gms": "3",
                        "Rec": "3",
                        "Yds": "6",
                        "Avg": "2.00",
                        "YPG": "2.0",
                        "Lg": "5",
                        "TD": "0",
                        "FD": "0",
                        "Tar": "3",
                        "YAC": "7"
                    },
                    {
                        "Player": "Jack Stoll",
                        "Gms": "7",
                        "Rec": "2",
                        "Yds": "10",
                        "Avg": "5.00",
                        "YPG": "1.4",
                        "Lg": "6",
                        "TD": "0",
                        "FD": "0",
                        "Tar": "3",
                        "YAC": "2"
                    },
                    {
                        "Player": "Johnny Wilson",
                        "Gms": "9",
                        "Rec": "2",
                        "Yds": "14",
                        "Avg": "7.00",
                        "YPG": "1.6",
                        "Lg": "9",
                        "TD": "1",
                        "FD": "2",
                        "Tar": "7",
                        "YAC": "6"
                    },
                    {
                        "Player": "John Ross",
                        "Gms": "1",
                        "Rec": "1",
                        "Yds": "6",
                        "Avg": "6.00",
                        "YPG": "6.0",
                        "Lg": "6",
                        "TD": "0",
                        "FD": "1",
                        "Tar": "2",
                        "YAC": "2"
                    },
                    {
                        "Player": "Ben VanSumeren",
                        "Gms": "9",
                        "Rec": "1",
                        "Yds": "0",
                        "Avg": "0.00",
                        "YPG": "0.0",
                        "Lg": "0",
                        "TD": "0",
                        "FD": "0",
                        "Tar": "1",
                        "YAC": "0"
                    },
                    {
                        "Player": "Philadelphia",
                        "Gms": "9",
                        "Rec": "165",
                        "Yds": "1,981",
                        "Avg": "12.01",
                        "YPG": "220.1",
                        "Lg": "67t",
                        "TD": "12",
                        "FD": "90",
                        "Tar": "223",
                        "YAC": "875"
                    },
                    {
                        "Player": "Opponents",
                        "Gms": "9",
                        "Rec": "173",
                        "Yds": "1,732",
                        "Avg": "10.01",
                        "YPG": "192.4",
                        "Lg": "70t",
                        "TD": "8",
                        "FD": "86",
                        "Tar": "276",
                        "YAC": "850"
                    }
                ]
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
