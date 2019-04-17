import pathlib
import shutil
import collections

import numpy as np
import pandas as pd


input_data_path = pathlib.Path('processed_data/seagate.csv')
output_data_path = pathlib.Path('processed_data/seagate_cleaned_01.csv')

headers_path = pathlib.Path('processed_data/seagate_headers.csv')

chunk_size = 100000

unnecesary_columns = ['id', 'date', 'serial_number', 'model']


def main():
    # Add raw SMART data columns to list of removable columns
    headers_dataframe = pd.read_csv(headers_path)
    headers = headers_dataframe.columns.values
    raw_headers = [x for x in headers if "raw" in x]
    removable_headers = unnecesary_columns + raw_headers

    # Add empty columns to list of removable columns
    common_headers = set()
    for data_frame in pd.read_csv(input_data_path, iterator=True, chunksize=chunk_size):
        data_frame.dropna(axis=1, how='all', inplace=True)
        common_headers = common_headers | set(data_frame.columns.values)
    removable_headers = list(set(removable_headers + list(set(headers) - common_headers)))

    # Delete output file if it already exists
    if output_data_path.exists():
        output_data_path.unlink()

    # Drop unnecessary rows from table, and write to new file
    iter_csv = pd.read_csv(input_data_path, iterator=True, chunksize=chunk_size)
    counter = 0
    with open(output_data_path, 'a') as f:
        for data_frame in iter_csv:
            data_frame.dropna(axis=0, subset=['failure'], inplace=True)
            data_frame.drop(labels=removable_headers, axis=1, inplace=True)
            if counter == 0:
                data_frame.to_csv(f, index=False, header=True)
            else:
                data_frame.to_csv(f, index=False, header=False)
            counter += 1


if __name__ == '__main__':
    main()
