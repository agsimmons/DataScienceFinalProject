import pathlib
import math

import tqdm

import numpy as np
import pandas as pd

input_broken_path = pathlib.Path('processed_data/seagate_broken.csv')
input_working_path = pathlib.Path('processed_data/seagate_working.csv')

output_path = pathlib.Path('processed_data/seagate_combined.csv')

chunk_size = 10000

num_chunks = 600


def main():
    print('Getting number of broken drives...')
    num_broken = 0
    for data in tqdm.tqdm(pd.read_csv(input_broken_path, iterator=True, chunksize=chunk_size)):
        num_broken += len(data.index)

    print('Getting number of working drives...')
    num_working = 0
    for data in tqdm.tqdm(pd.read_csv(input_working_path, iterator=True, chunksize=chunk_size)):
        num_working += len(data.index)

    print()

    broken_chunk_size = math.ceil(num_broken / num_chunks)
    working_chunk_size = math.ceil(num_working / num_chunks)

    print(f'Num broken: {num_broken}')
    print(f'Num working: {num_working}')
    print(f'Broken chunk size: {broken_chunk_size}')
    print(f'Working chunk size: {working_chunk_size}')

    with open(output_path, 'w') as f:
        broken_iterator = pd.read_csv(input_broken_path, iterator=True, chunksize=broken_chunk_size)
        working_iterator = pd.read_csv(input_working_path, iterator=True, chunksize=working_chunk_size)

        counter = 0
        for _ in range(num_chunks):
            broken_data = next(broken_iterator)
            working_data = next(working_iterator)
            combined_data = pd.concat((broken_data, working_data))

            combined_data = combined_data.sample(frac=1)

            if counter == 0:
                combined_data.to_csv(f, index=False, header=True)
            else:
                combined_data.to_csv(f, index=False, header=False)

            counter += 1


if __name__ == '__main__':
    main()
