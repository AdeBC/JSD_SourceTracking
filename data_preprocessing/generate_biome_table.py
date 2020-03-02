import pandas as pd
import os




def load_ids(Dir):
    with open(Dir, 'r') as f:
        return map(lambda x: x.rstrip'.tsv\n', f.readlines())

def load_tab(Dir):
    biomes = os.listdir(Dir)
    samps = map(lambda x: os.listdir(x), biomes)
    tab = {key.rstrip('.tsv').split('-')[1]: biomes[val_i] for val_i in range(len(biomes)) for key in samps[val_i]}
    return tab


samps_ids = '' 
biomes = ''
ids = load_ids(samps_ids)
print(ids)
tab = load_tab(biomes)
print(tab)
samps = map(lambda x: [x]+[tab[x], 'Source', '1'], ids)

df = pd.DataFrame(columns = ['SampleID','Env','SourceSink','id'])
df.append(samps, columns = ['SampleID','Env','SourceSink','id'])
df.to_csv('/mnt/c/Users/ch379/Documents/JSD_sourcetracking/Data_files/metadata_ONN_sources.txt', sep = '\t', index = False)





