from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
import logging

def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.StreamHandler()
        ]
    )


def get_data(config_path):
    try: 
        config = read_yaml(config_path)
        logging.info("Configuration file read successfully.")

        remote_data_path = config["data_source"]
        df = pd.read_csv(remote_data_path, sep=";")
        logging.info(f"Data fetched successfully from {remote_data_path}.")

        # save dataset in the local directory
        # create path to directory: artifacts/raw_local_dir/data.csv
        artifacts_dir = config["artifacts"]['artifacts_dir']
        raw_local_dir = config["artifacts"]['raw_local_dir']
        raw_local_file = config["artifacts"]['raw_local_file']

        raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)

        create_directory(dirs= [raw_local_dir_path])
        logging.info(f"Directory {raw_local_dir_path} created successfully.")

        raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
        
        df.to_csv(raw_local_file_path, sep=",", index=False)
        logging.info(f"Data saved successfully at {raw_local_file_path}.")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        raise

if __name__ == '__main__':
    setup_logging()
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)

