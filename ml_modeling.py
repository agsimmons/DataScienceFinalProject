import pathlib

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt


INPUT_PATH = pathlib.Path('processed_data/seagate_combined.csv')


num_chunks = 30
broken_chunk_size = 12
working_chunk_size = 130885
chunk_size = broken_chunk_size + working_chunk_size


def main():
    for i in range(num_chunks):

        smart_data = pd.read_csv(INPUT_PATH, iterator=True, chunksize=chunk_size)
        model = GaussianNB()
        counter = 0

        test_y = pd.DataFrame()
        test_X = pd.DataFrame()

        for data in smart_data:
            # data_working = data[data['failure'] == 0]
            # data_broken = data[data['failure'] == 1]
            # data_working = data_working.sample(n=len(data_broken.index))
            # data = pd.concat((data_broken, data_working))
            # data = data.sample(frac=1)

            data_y = data['failure']
            data_X = data.drop(labels=['failure'], axis=1)

            if counter == i:
                test_y = data_y
                test_X = data_X
            else:
                model.partial_fit(data_X, data_y, classes=[0, 1])
            counter += 1

        predictions = model.predict(test_X)
        print(classification_report(test_y, predictions, output_dict=True))
        print(confusion_matrix(test_y, predictions))



    # print('Loading csv data')
    # smart_data = pd.read_csv(INPUT_PATH, dtype={
    #     'capacity_bytes': 'Int64',
    #     'failure': np.int8
    # })
    #
    # # Fill in nan values with the mean of that field
    # print('Filling in null values')
    # imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    # imp = imp.fit(smart_data)
    # smart_data = imp.transform(smart_data)
    # print(smart_data.head())
    #
    # print('Under-sampling')
    # # count_class_0, count_class_1 = smart_data['failure'].value_counts()
    # print(smart_data['failure'].value_counts())
    # print(smart_data['failure'].value_counts())
    #
    # # df_class_0 = smart_data[smart_data['failure'] == 0]
    # # df_class_1 = smart_data[smart_data['failure'] == 1]
    # #
    # # df_class_0_under = df_class_0.sample(count_class_1)
    # # df_test_under = pd.concat([df_class_0_under, df_class_1], axis=0)
    # #
    # # print(df_test_under.target.value_counts())
    #
    # # Separate out values and data
    # labels = smart_data['failure']
    # data = smart_data.drop(labels='failure', axis=1)
    #
    #
    #
    # # print('Splitting data into testing and training sets')
    # # X_train, X_test, y_train, y_test = train_test_split(data_imp, labels, test_size=0.5, random_state=42)
    # #
    # # print('Training model')
    # # model = GaussianNB()
    # # model.fit(X_train, y_train)
    # #
    # # predictions = model.predict(X_test)
    # #
    # #
    # #
    # # print(classification_report(y_test, predictions))
    #
    #
    # # scores = cross_val_score(model, data_imp, labels, cv=100)
    # # print(f'Accuracy: {scores.mean()} (+/- {scores.std() * 2})')


if __name__ == '__main__':
    main()
