import pathlib

import tqdm

import numpy as np
import pandas as pd

input_data_path = pathlib.Path('processed_data/seagate_cleaned_02.csv')

output_working_path = pathlib.Path('processed_data/seagate_working.csv')
output_broken_path = pathlib.Path('processed_data/seagate_broken.csv')

chunk_size = 10000


def main():
    print('Separating data...')
    broken_drives = pd.DataFrame()
    with open(output_working_path, 'w') as f:
        counter = 0
        for data in tqdm.tqdm(pd.read_csv(input_data_path, iterator=True, chunksize=chunk_size)):
            broken_drives = pd.concat((broken_drives, data[data['failure'] == 1]))

            if counter == 0:
                data[data['failure'] == 0].to_csv(f, index=False, header=True)
            else:
                data[data['failure'] == 0].to_csv(f, index=False, header=False)

            counter += 1

    print('Writing broken data...')
    broken_drives.to_csv(output_broken_path, index=False)


if __name__ == '__main__':
    main()
