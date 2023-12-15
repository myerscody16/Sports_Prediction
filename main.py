from code.data_ingestion import DataRetriever
from code.data_processing import DataProcessor
import os


#### User defined variables
# Minimum year of 2020 due to API constraints
start_of_season_year = 2023
ingest_data = False
process_data = False
process_historic_data = True
####


if __name__ == '__main__':
    raw_dir_path = 'data/raw/'
    source_data_dir_path = 'data/source/'
    if ingest_data:
        data_retriever = DataRetriever(start_of_season_year, raw_dir_path)
        data_retriever.getMatchData()
        data_retriever.getStandingsData()
    if process_data:
        data_processor = DataProcessor(start_of_season_year, raw_dir_path, source_data_dir_path)
        data_processor.extract_data()
    if process_historic_data:
        seasons = os.listdir(raw_dir_path)
        match_seasons = [path.split('_')[0] for path in seasons if 'match' in path]
        for season in match_seasons:
            data_processor = DataProcessor(season, raw_dir_path, source_data_dir_path)
            data_processor.process_selected_season_data()
        standings_seasons = [path.split('_')[0] for path in seasons if 'standings' in path]
        for season in standings_seasons:
            data_processor = DataProcessor(season, raw_dir_path, source_data_dir_path)
            data_processor.process_standings_data()