import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(return_X_y=False) #If True, returns (data, target) instead of a Bunch object.

def sklearn_to_df(sklearn_dataset):
    df = pd.DataFrame(sklearn_dataset.data, columns=sklearn_dataset.feature_names)
    df['target'] = pd.Series(sklearn_dataset.target)
    return df

df = sklearn_to_df(data)

df5 = df[['mean radius', 'mean texture','mean perimeter','mean area','mean smoothness']]



for col in df5.columns:
    for row in df5.index:
        if df5.loc[row,col] >=df[col].mean():
            df5.loc[row,col] = 1
        else:
            df5.loc[row,col] = 0

target_list = df.loc[:,'target']
df5['target'] = target_list # getting SettingWithCopyWarning why ??

def cartesian_coord(*arrays):
    grid = np.meshgrid(*arrays)        
    coord_list = [entry.ravel() for entry in grid]
    points = np.vstack(coord_list).T
    return points

a = np.arange(2)  # 0,1
prob_list = cartesian_coord(*5*[a])

df_prob = pd.DataFrame(prob_list, columns=['mean radius', 'mean texture','mean perimeter','mean area','mean smoothness'])

target_prob_list = []
for row in df_prob.index:
    list_holder = df5[(df5['mean radius'] == df_prob.iloc[row,0])& 
                    (df5['mean texture'] == df_prob.iloc[row,1]) &
                    (df5['mean perimeter'] == df_prob.iloc[row,2]) &
                    (df5['mean area'] == df_prob.iloc[row,3]) &
                    (df5['mean smoothness'] == df_prob.iloc[row,4])]


    sample_count = len(list_holder)

    event_1_or_0 = list_holder['target'].value_counts()
    
    if len(event_1_or_0) != 0:
        if event_1_or_0.index.any() == 1:
            event_prob = event_1_or_0[1]/sample_count
        else:
            event_prob = 0
    else:
        event_prob = 0
    
    target_prob_list.append(event_prob)

df_prob['target_prob_1'] = target_prob_list
