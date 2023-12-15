import requests
import json
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


class DataRetriever:
    def __init__(self, season, raw_dir_path):
        self.match_url = f'https://api.football-data.org/v4/competitions/2021/matches/?season={season}&?status=FINSHED'
        self.standings_url = f'http://api.football-data.org/v4/competitions/PL/standings/?season={season}'
        self.headers = {'X-Auth-Token': os.getenv("FOOTBALL-ORG_API_TOKEN")}
        self.match_file_name = raw_dir_path + f'{season}_premier_league_match_data_raw.jsonl'
        self.standings_file_name = raw_dir_path + f'{season}_premier_league_standings_raw.jsonl'


    def writeDataToOutputFile(self, response, file_name, index):
        mode = 'a' if os.path.exists(file_name) else 'w+'
        with open(file_name, mode) as output_file:
            for json_object in response.json()[index]:
                json_str = json.dumps(json_object)
                output_file.write(json_str + '\n')


    def getMatchData(self):
        try:
            response = requests.get(self.match_url, headers=self.headers)
            response.raise_for_status()
            self.writeDataToOutputFile(response, self.match_file_name, 'matches')
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Request Error:", err)
    

    def getStandingsData(self):
        try:
            response = requests.get(self.standings_url, headers=self.headers)
            response.raise_for_status()
            self.writeDataToOutputFile(response, self.standings_file_name, 'standings')
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Request Error:", err)
