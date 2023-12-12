import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


class DataRetriever:
    def __init__(self, season):
        self.url = f'https://api.football-data.org/v4/competitions/2021/matches/?season={season}&status=FINSHED'
        self.headers = {'X-Auth-Token': os.getenv("FOOTBALL-ORG_API_TOKEN")}
        self.file_name = f'../data/{season}_premier_league_match_data.jsonl'


    def writeDataToOutputFile(self, response):
        if os.path.exists(self.file_name):
            mode = 'a'
        else:
            mode = 'w'
        with open(self.file_name, mode) as output_file:
            for json_object in response.json()['matches']:
                json_str = json.dumps(json_object)
                output_file.write(json_str + '\n')


    def getMatchData(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            res_code = response.raise_for_status()
            if res_code == '200':
                self.writeDataToOutputFile(response)
                

    
