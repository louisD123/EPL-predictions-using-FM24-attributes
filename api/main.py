import json
import csv
import requests
import os
from dotenv import load_dotenv

# Load values from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

BOOKMAKER = "pinnacle"

# --- Fetch EPL odds ---
odds_response = requests.get(
    "https://api.the-odds-api.com/v4/sports/soccer_epl/odds",
    params={
        "api_key": API_KEY,
        "regions": "eu",
        "markets": "h2h",
        "oddsFormat": "decimal",
        "dateFormat": "iso",
        "bookmakers": BOOKMAKER
    }
)

if odds_response.status_code != 200:
    print("Failed:", odds_response.text)
    exit()

raw_data = odds_response.json()

# --- Extract fixtures table ---
fixtures = []

for event in raw_data:
    # get only the selected bookmaker
    bookies = [b for b in event["bookmakers"] if b["key"] == BOOKMAKER]
    if not bookies:
        continue

    markets = bookies[0]["markets"]
    h2h = next((m for m in markets if m["key"] == "h2h"), None)
    if not h2h:
        continue

    outcomes = h2h["outcomes"]

    home_odds = None
    draw_odds = None
    away_odds = None

    for o in outcomes:
        if o["name"] == event["home_team"]:
            home_odds = o["price"]
        elif o["name"] == event["away_team"]:
            away_odds = o["price"]
        elif o["name"].lower() == "draw":
            draw_odds = o["price"]

    fixtures.append({
        "commence_time": event["commence_time"],
        "home_team": event["home_team"],
        "away_team": event["away_team"],
        "win_odds": home_odds,
        "draw_odds": draw_odds,
        "lose_odds": away_odds
    })


# --- Save to CSV ---
filename = "upcoming_fixtures.csv"

with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "commence_time",
            "home_team",
            "away_team",
            "win_odds",
            "draw_odds",
            "lose_odds"
        ]
    )
    writer.writeheader()
    writer.writerows(fixtures)

print(f"Saved to {filename}")
