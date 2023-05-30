import pandas as pd
import numpy as np
url = 'https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv'
df = pd.read_csv(url)

def dist(q,p):
    q = q[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
    p = p[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
    return np.sqrt(np.sum((q-p)**2))

def range_search(q, r):
    return df[df.apply(lambda p: dist(q,p), axis=1) < r]

def experiment(qn, r):
    q = df.iloc[qn]
    result = range_search(q, r)
    pr = result[result.variety == q.variety].shape[0] / result.shape[0]
    return pr 


ndf = pd.DataFrame(columns=['q15', 'q82', 'q121'])

for r in [0.8, 1.5, 2.6]:
    ls = []
    for qn in [15, 82, 121]:

        ls.append(experiment(qn, r))
    ndf.loc[r] = ls
ndf