import pandas as pd
import random
import os
from sklearn.model_selection import LeaveOneOut
import numpy as np


def split_8(samples):
  random.shuffle(samples)
  result = {i:[] for i in range(8)}
  [result[i].append(val.copy()) for index,val in enumerate(samples) for i in range(8) if index % 8 == i]
  return np.array([i for i in result.values()])


def merge(ls):
  l = []
  [l.extend(i) for i in ls]
  return l


def merge_sinks_sources(sinks, sources):
  sources = merge(sources)
  sources = list(map(lambda x: x + ['Source'], sources))
  groups = {i:sources.copy() for i in range(len(sinks))}
  sinks = map(lambda x: x + ['Sink'], sinks[0])
  sinks = [sink+[str(i+1)] for i, sink in enumerate(sinks)]
  sources = list(map(lambda x: x+[str(len(sinks))], sources))
  tab = sinks + sources
  #print(tab[0:10])
  new_metadata = pd.DataFrame(columns=['SampleID','Env','SourceSink','id'])
  new_metadata = new_metadata.append(pd.DataFrame(tab, columns=['SampleID','Env','SourceSink','id']))
  # new_metadata = new_metadata.append(pd.DataFrame(sinks, columns=['SampleID','Env','SourceSink','id']))
 
  return new_metadata


def leaveOneOut(pies):
  loo = LeaveOneOut()
  loo.get_n_splits(pies)
  #ret = [[train_i, test_i] for train_i, test_i in loo.split(pies)]
  ret = [[list(pies[train_i]), list(pies[test_i])] for train_i, test_i in loo.split(pies)]
  return ret


Dir = '/mnt/c/Users/ch379/Documents/JSD_sourcetracking/Data_files'

metadata_file = os.path.join(Dir, 'metadata_example_multi.txt')
metadata = pd.read_csv(metadata_file, header=0, sep='\t')
metadata = metadata.drop(columns=['SourceSink', 'id'])
samps = metadata.values.tolist() 
pies = split_8(samps)
loo = leaveOneOut(pies)

for index, ss in enumerate(loo):
  df = merge_sinks_sources(ss[1].copy(), ss[0].copy())
  df.to_csv(os.path.join(Dir, 'metadata_ONN_'+str(index)+'.txt'), sep='\t', index=False)
   #print(r)
#tab_all = [merge_sinks_sources(sinks.copy(), sources.copy()) for source, sinks in loo]



