import pandas as pd
from Bio import SeqIO
import numpy as np

# paser sequences to df
records = pd.DataFrame(list(SeqIO.parse("aligment.fasta", "fasta")))

# output
df = pd.DataFrame(columns=['fa','fc','fg','ft','C'])

# iterate multialignment by columns
for column in records.columns:
	
	# get frequences
	frequences = records[column].value_counts()

	# disregard symbols other than ACGT 
	for sym in ['-','k','m','n','r','s','w','y']:
		if sym in frequences.index:
			frequences = frequences.drop([sym])

	n = frequences.sum()

	# calculate frequences
	vals = []
	for sym in ['a','c','g','t']:
		vals.append(frequences[sym]/n if sym in frequences.index else 0)

	# calculate entropy
	C = sum(map(lambda x: x * np.log(x) if x != 0 else 0,vals))
	if C != 0: C = -C 

	df = df.append({'fa': vals[0], 'fc': vals[1], 'fg': vals[2], 'ft': vals[3], 'C': C}, ignore_index=True)

#save
df.to_csv("results.csv")
