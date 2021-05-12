import random
import pandas as pd
from time import time, sleep

df = pd.read_csv('./Datasets/Tabular/heart/heart.csv')
print(df.head())

predictions = []


for i in range(df.shape[0]):
    sleep(1)
    pred = random.randrange(0,10) # need use model
    print(df.values[i])

    if pred < 9:
        predictions.append(0)
    else:
        predictions.append(0)

    if len(predictions) == 5:
        cont = 0
        for p in predictions:
            if p == 0:
                cont += 1
        if cont >= 4:
            print('HEART ATTACK')
        predictions.remove(predictions[0])


#start = time()

'''while True:

    sleep(1)
    pred = random.randrange(0,10) # need use model

    if pred < 8:
        predictions.append(0)
    else:
        predictions.append(0)

    if len(predictions) == 5:
        cont = 0
        for p in predictions:
            if p ==1:
                cont += 1
        if cont >= 4:
            print('HEART ATTACK')
        predictions.remove(predictions[0])'''