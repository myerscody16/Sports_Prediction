import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()


class DataRetriever:
    def __init__(self, season, raw_dir_path):
        self.url = f'https://api.football-data.org/v4/competitions/2021/matches/?season={season}&?status=FINSHED'
        self.headers = {'X-Auth-Token': os.getenv("FOOTBALL-ORG_API_TOKEN")}
        self.file_name = raw_dir_path + f'{season}_premier_league_match_data_raw.jsonl'


    def writeDataToOutputFile(self, response):
        mode = 'a' if os.path.exists(self.file_name) else 'w+'
        with open(self.file_name, mode) as output_file:
            for json_object in response.json()['matches']:
                json_str = json.dumps(json_object)
                output_file.write(json_str + '\n')


    def getMatchData(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            self.writeDataToOutputFile(response)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Request Error:", err)
