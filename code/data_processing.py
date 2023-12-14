import pandas as pd
from io import StringIO

class DataProcessor:
    def __init__(self, process_historic_data, season, raw_dir_path, source_data_dir_path):
        self.season = season
        self.raw_directory_path = raw_dir_path
        self.source_directory_path = source_data_dir_path
        self.process_historic_data = process_historic_data


    def process_all_data(self):
        pass

    
    def processStandingsData(self):
        # for json_object in response.json()['standings']:
        #     if json_object['type'] == 'TOTAL':
        #         standings_df = pd.json_normalize(json_object['table'])
        #         standings_df.to_csv(self.st)
        pass


    def process_selected_season_data(self):
        with open(f'{self.raw_directory_path}{self.season}_premier_league_match_data_raw.jsonl', 'r') as file:
            jsonl_string = file.read()
        json_io = StringIO(jsonl_string)
        data = pd.read_json(json_io, lines=True)
        matches = pd.DataFrame({
            'id': data['id'],
            'date_played': data['utcDate'],
            'home_team_id': data['homeTeam'].apply(lambda x: x.get('id')),
            'home_team_name': data['homeTeam'].apply(lambda x: x.get('name')),
            'away_team_id': data['awayTeam'].apply(lambda x: x.get('id')),
            'away_team_name': data['awayTeam'].apply(lambda x: x.get('name')),
            'winner': data['score'].apply(lambda x: x.get('winner')),
            'home_goals': data['score'].apply(lambda x: x.get('fullTime').get('home')),
            'away_goals': data['score'].apply(lambda x: x.get('fullTime').get('away'))
        })
        matches.to_csv(f'{self.source_directory_path}{self.season}_premier_league_match_data_matches.csv', sep=',')


    def extract_data(self):
        if self.process_historic_data:
            self.process_all_data()
        else:
            self.process_selected_season_data()

