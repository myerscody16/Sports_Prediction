from pandas import read_json


class DataProcessor:
    def __init__(self, process_historic_data, season, raw_dir_path, source_data_dir_path):
        self.season = season
        self.raw_directory_path = raw_dir_path
        self.source_directory_path = source_data_dir_path
        self.process_historic_data = process_historic_data


    def process_all_data(self):
        pass

    
    def process_selected_season_data(self):
        print(self.raw_directory_path + f'{self.season}_premier_league_match_data_raw.jsonl')
        data = read_json(self.raw_directory_path + f'{self.season}_premier_league_match_data_raw.jsonl', lines=True)
        print(data.columns)


    def extract_data(self):
        if self.process_historic_data:
            self.process_all_data()
        else:
            self.process_selected_season_data()

