import pathlib

import numpy as np
import pandas as pd

INPUT_PATH = pathlib.Path('processed_data/wdc.csv')
OUTPUT_PATH = pathlib.Path('processed_data/wdc_cleaned.csv')


def main():
    # Load in S.M.A.R.T data
    smart_data = pd.read_csv(INPUT_PATH, dtype={
        'capacity_bytes': 'Int64',
        'failure': np.int8
    })

    # Drop unecessary columns
    smart_data.drop(labels=['id', 'date', 'serial_number', 'model'], axis=1, inplace=True)

    # Drop empty columns
    smart_data.dropna(axis=1, how='all', inplace=True)

    # Drop mostly empty rows
    smart_data.dropna(axis=0, how='all', subset=['smart_1_normalized', 'smart_1_raw',
                                                 'smart_3_normalized', 'smart_3_raw', 'smart_4_normalized',
                                                 'smart_4_raw', 'smart_5_normalized', 'smart_5_raw',
                                                 'smart_7_normalized', 'smart_7_raw', 'smart_9_normalized',
                                                 'smart_9_raw', 'smart_10_normalized', 'smart_10_raw',
                                                 'smart_12_normalized', 'smart_12_raw', 'smart_192_normalized',
                                                 'smart_192_raw', 'smart_194_normalized', 'smart_194_raw',
                                                 'smart_197_normalized', 'smart_197_raw', 'smart_198_normalized',
                                                 'smart_198_raw', 'smart_199_normalized', 'smart_199_raw'],
                      inplace=True)

    # Remove raw columns
    smart_data.drop(labels=['smart_1_raw', 'smart_3_raw', 'smart_4_raw', 'smart_5_raw', 'smart_7_raw', 'smart_9_raw', 'smart_10_raw', 'smart_12_raw', 'smart_192_raw', 'smart_194_raw', 'smart_197_raw', 'smart_198_raw', 'smart_199_raw'], axis=1, inplace=True)

    # Export cleaned data to CSV
    smart_data.to_csv(OUTPUT_PATH, index=False)


if __name__ == '__main__':
    main()
