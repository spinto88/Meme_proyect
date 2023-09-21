import pandas as pd 
import os

fp = open('data_original_Leskovec.txt', 'r')

lines = fp.readlines()[6:]

indexes_clust = [i for i in range(len(lines)) if lines[i].split('\t')[0] != '' and lines[i].split('\t')[0] != '\n']

try:
    os.system("mkdir Data_Disgregada")
except:
    pass
 
for j in range(len(indexes_clust)):
    
    try:
        lines_clust = lines[indexes_clust[j]:indexes_clust[j+1]]
    except:
        lines_clust = lines[indexes_clust[j]:]

    root = lines_clust[0].split('\t')[2]
    fileid = int(lines_clust[0].split('\t')[-1])

    index_subphrases = [i for i in range(len(lines_clust)) if lines_clust[i].split('\t')[0] == '' and lines_clust[i].split('\t')[1] != '']
    lines_subphrases = []
    phrases = []
    for k in range(len(index_subphrases)):
        phrase = lines_clust[index_subphrases[k]].split('\t')[3]
        try:
            lines_subphrase = lines_clust[index_subphrases[k]:index_subphrases[k+1]][1:-1]
        except:
            lines_subphrase = lines_clust[index_subphrases[k]:][1:-1]
            
        phrases += [phrase] * len(lines_subphrase)
        lines_subphrases += lines_subphrase
    
    roots = [root] * len(lines_subphrases)
    
    df = pd.DataFrame()
    df['time'] = [l.split('\t')[2] for l in lines_subphrases]
    df['frequency'] = [l.split('\t')[3] for l in lines_subphrases]
    df['media'] = [l.split('\t')[4] for l in lines_subphrases]
    df['url'] = [l.split('\t')[5].replace('\n','') for l in lines_subphrases]
    df['phrase'] = phrases
    df['root'] = roots

   
    df.to_csv(f'Data_Disgregada/Lkvec_id{fileid}.csv', index = False)
