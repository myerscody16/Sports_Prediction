from code.data_ingestion import DataRetriever
from code.data_processing import DataProcessor

#### User defined variables

# Minimum year of 2019 due to API constraints
start_of_season_year = 2023
ingest_data = False
process_data = True
process_historic_data = False

####


if __name__ == '__main__':
    raw_dir_path = f'data/raw/'
    source_data_dir_path = f'data/source/'
    if ingest_data:
        data_retriever = DataRetriever(start_of_season_year, raw_dir_path)
        data_retriever.getMatchData()
    if process_data:
        data_processor = DataProcessor(process_historic_data, start_of_season_year, raw_dir_path, source_data_dir_path)
        data_processor.extract_data()