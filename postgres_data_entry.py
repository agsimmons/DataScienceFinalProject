import numpy as np
import pandas as pd

import psycopg2

import config
import models


conn = psycopg2.connect(database='smart', user='smart_user')
cur = conn.cursor()


def _get_column_data_type(name):
    if name == 'date' or name == 'serial_number' or name == 'model':
        return 'TEXT'
    return 'INTEGER'


def _create_insert_query(row_data, column_labels):
    column_labels = [label for label in column_labels if not isinstance(row_data[label], float)]

    query = 'INSERT INTO data ('

    for label in column_labels:
        query += label + ', '
    query = query[:-2]

    query += ') VALUES ('

    for label in column_labels:
        if _get_column_data_type(label) == 'TEXT':
            query += "'" + str(row_data[label]) + "', "
        else:
            query += str(row_data[label]) + ", "
    query = query[:-2]

    return query + ');'


def main():
    # Get list of CSV files
    csv_files = sorted(list(config.DATA_DIR.glob('**/*.csv')))
    num_csv_files = len(csv_files)

    # Insert CSV data into DB
    for i, csv_file in enumerate(csv_files):
        print(f'Processing csv file {i + 1}/{num_csv_files}')

        csv_dataframe = pd.read_csv(csv_file)
        csv_dataframe['failure'] = csv_dataframe['failure'].astype(bool)

        for row in csv_dataframe.itertuples():
            row_data = row._asdict()
            del row_data['Index']

            cur.execute(_create_insert_query(row_data, csv_dataframe.columns.values))

        conn.commit()


if __name__ == '__main__':
    main()
