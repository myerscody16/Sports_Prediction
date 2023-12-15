import pandas as pd
from io import StringIO


class DataProcessor:
    def __init__(self, season, raw_dir_path, source_data_dir_path):
        self.season = season
        self.raw_directory_path = raw_dir_path
        self.source_directory_path = source_data_dir_path


    def form_value_calculation(self, form_string):
        form_string = form_string.replace(',', '')
        value_dict = {
            'w': 1,
            'l': -1,
            'd': 0
        }
        form_value = 0
        for char in form_string:
            form_value += value_dict[char.lower()]
        return form_value

    
    def process_standings_data(self):
        with open(f'{self.raw_directory_path}{self.season}_premier_league_standings_raw.jsonl', 'r') as file:
            jsonl_string = file.read()
        json_io = StringIO(jsonl_string)
        data = pd.read_json(json_io, lines=True)
        for row in data.iterrows():
            if row[1]['type'] == 'TOTAL':
                standings_df = pd.json_normalize(row[1]['table'])
                standings_df['form_value'] = standings_df['form'].apply(lambda x: self.form_value_calculation(x))
                standings_df.drop(['form', 'team.crest', 'team.shortName', 'team.tla'], axis = 1, inplace=True)
                standings_df.to_csv(f'{self.source_directory_path}{self.season}_premier_league_standings.csv', sep=',')


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
