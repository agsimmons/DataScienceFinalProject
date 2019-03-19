import sqlite3
import pathlib
import sys
import pickle

import config

import numpy as np
import pandas as pd
import tables


# def _check_for_existing_db():
#     if config.DATA_DB.exists():
#         while True:
#             choice = input('Database must be deleted to proceed. Would you like to delete the database file? (y/n): ').lower()
#             if choice == 'y':
#                 config.DATA_DB.unlink()
#                 break
#             elif choice == 'n':
#                 sys.exit()

def _connect_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    return conn, c


def _create_db(db_path):
    conn, c = _connect_db(db_path)

    # Create table
    c.execute('''CREATE TABLE data (date TEXT, serial_number TEXT, model TEXT, capacity_bytes INTEGER, failure INTEGER, smart_1_normalized INTEGER, smart_1_raw INTEGER, smart_2_normalized INTEGER, smart_2_raw INTEGER, smart_3_normalized INTEGER, smart_3_raw INTEGER, smart_4_normalized INTEGER, smart_4_raw INTEGER, smart_5_normalized INTEGER, smart_5_raw INTEGER, smart_7_normalized INTEGER, smart_7_raw INTEGER, smart_8_normalized INTEGER, smart_8_raw INTEGER, smart_9_normalized INTEGER, smart_9_raw INTEGER, smart_10_normalized INTEGER, smart_10_raw INTEGER, smart_11_normalized INTEGER, smart_11_raw INTEGER, smart_12_normalized INTEGER, smart_12_raw INTEGER, smart_13_normalized INTEGER, smart_13_raw INTEGER, smart_15_normalized INTEGER, smart_15_raw INTEGER, smart_22_normalized INTEGER, smart_22_raw INTEGER, smart_23_normalized INTEGER, smart_23_raw INTEGER, smart_24_normalized INTEGER, smart_24_raw INTEGER, smart_177_normalized INTEGER, smart_177_raw INTEGER, smart_179_normalized INTEGER, smart_179_raw INTEGER, smart_181_normalized INTEGER, smart_181_raw INTEGER, smart_182_normalized INTEGER, smart_182_raw INTEGER, smart_183_normalized INTEGER, smart_183_raw INTEGER, smart_184_normalized INTEGER, smart_184_raw INTEGER, smart_187_normalized INTEGER, smart_187_raw INTEGER, smart_188_normalized INTEGER, smart_188_raw INTEGER, smart_189_normalized INTEGER, smart_189_raw INTEGER, smart_190_normalized INTEGER, smart_190_raw INTEGER, smart_191_normalized INTEGER, smart_191_raw INTEGER, smart_192_normalized INTEGER, smart_192_raw INTEGER, smart_193_normalized INTEGER, smart_193_raw INTEGER, smart_194_normalized INTEGER, smart_194_raw INTEGER, smart_195_normalized INTEGER, smart_195_raw INTEGER, smart_196_normalized INTEGER, smart_196_raw INTEGER, smart_197_normalized INTEGER, smart_197_raw INTEGER, smart_198_normalized INTEGER, smart_198_raw INTEGER, smart_199_normalized INTEGER, smart_199_raw INTEGER, smart_200_normalized INTEGER, smart_200_raw INTEGER, smart_201_normalized INTEGER, smart_201_raw INTEGER, smart_220_normalized INTEGER, smart_220_raw INTEGER, smart_222_normalized INTEGER, smart_222_raw INTEGER, smart_223_normalized INTEGER, smart_223_raw INTEGER, smart_224_normalized INTEGER, smart_224_raw INTEGER, smart_225_normalized INTEGER, smart_225_raw INTEGER, smart_226_normalized INTEGER, smart_226_raw INTEGER, smart_235_normalized INTEGER, smart_235_raw INTEGER, smart_240_normalized INTEGER, smart_240_raw INTEGER, smart_241_normalized INTEGER, smart_241_raw INTEGER, smart_242_normalized INTEGER, smart_242_raw INTEGER, smart_250_normalized INTEGER, smart_250_raw INTEGER, smart_251_normalized INTEGER, smart_251_raw INTEGER, smart_252_normalized INTEGER, smart_252_raw INTEGER, smart_254_normalized INTEGER, smart_254_raw INTEGER, smart_255_normalized INTEGER, smart_255_raw INTEGER)''')

    conn.commit()
    conn.close()


def _get_data_frame():
    return pd.DataFrame(columns=['date', 'serial_number', 'model', 'capacity_bytes', 'failure', 'smart_1_normalized', 'smart_1_raw', 'smart_2_normalized', 'smart_2_raw', 'smart_3_normalized', 'smart_3_raw', 'smart_4_normalized', 'smart_4_raw', 'smart_5_normalized', 'smart_5_raw', 'smart_7_normalized', 'smart_7_raw', 'smart_8_normalized', 'smart_8_raw', 'smart_9_normalized', 'smart_9_raw', 'smart_10_normalized', 'smart_10_raw', 'smart_11_normalized', 'smart_11_raw', 'smart_12_normalized', 'smart_12_raw', 'smart_13_normalized', 'smart_13_raw', 'smart_15_normalized', 'smart_15_raw', 'smart_22_normalized', 'smart_22_raw', 'smart_23_normalized', 'smart_23_raw', 'smart_24_normalized', 'smart_24_raw', 'smart_177_normalized', 'smart_177_raw', 'smart_179_normalized', 'smart_179_raw', 'smart_181_normalized', 'smart_181_raw', 'smart_182_normalized', 'smart_182_raw', 'smart_183_normalized', 'smart_183_raw', 'smart_184_normalized', 'smart_184_raw', 'smart_187_normalized', 'smart_187_raw', 'smart_188_normalized', 'smart_188_raw', 'smart_189_normalized', 'smart_189_raw', 'smart_190_normalized', 'smart_190_raw', 'smart_191_normalized', 'smart_191_raw', 'smart_192_normalized', 'smart_192_raw', 'smart_193_normalized', 'smart_193_raw', 'smart_194_normalized', 'smart_194_raw', 'smart_195_normalized', 'smart_195_raw', 'smart_196_normalized', 'smart_196_raw', 'smart_197_normalized', 'smart_197_raw', 'smart_198_normalized', 'smart_198_raw', 'smart_199_normalized', 'smart_199_raw', 'smart_200_normalized', 'smart_200_raw', 'smart_201_normalized', 'smart_201_raw', 'smart_220_normalized', 'smart_220_raw', 'smart_222_normalized', 'smart_222_raw', 'smart_223_normalized', 'smart_223_raw', 'smart_224_normalized', 'smart_224_raw', 'smart_225_normalized', 'smart_225_raw', 'smart_226_normalized', 'smart_226_raw', 'smart_235_normalized', 'smart_235_raw', 'smart_240_normalized', 'smart_240_raw', 'smart_241_normalized', 'smart_241_raw', 'smart_242_normalized', 'smart_242_raw', 'smart_250_normalized', 'smart_250_raw', 'smart_251_normalized', 'smart_251_raw', 'smart_252_normalized', 'smart_252_raw', 'smart_254_normalized', 'smart_254_raw', 'smart_255_normalized', 'smart_255_raw'])


def main():
    # if not config.DATA_DB.exists():
    #     _create_db(config.DATA_DB)
    #
    # conn, c = _connect_db(config.DATA_DB)

    store = pd.HDFStore('store.h5')

    # Get paths to all csv data files
    csv_files = list(config.DATA_DIR.glob('**/*.csv'))
    length = len(csv_files)

    for i, file in enumerate(csv_files):
        print(f'Processing csv file {i + 1}/{length}')

        data_frame = _get_data_frame()
        csv_frame = pd.read_csv(file)
        data_frame = pd.concat([data_frame, csv_frame], sort=False)

        store.append('df', data_frame)

    store.close()


if __name__ == '__main__':
    main()
