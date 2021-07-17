import pandas as pd

df = pd.read_csv("results.csv")
THREADHOLD = 0.5

ORF1A = sum([ 1 for seq in df[265:13483]['C'] if seq != 0.0])
print("No. of alterations in ORF1A " + str(ORF1A))
print("Percentage of alterations in ORF1A " + str(ORF1A/(13484-266)))
maxORF1A = max(df[265:13483]['C'])
print("High-conservation positions" + str([(i+1,df.loc[i,'C']) for i in range(265,13483)  if df.loc[i,'C'] > THREADHOLD]))

Spike = sum([ 1 for seq in df[21562:25384]['C'] if seq != 0.0])
print("No. of alterations in Spike protein " + str(Spike))
print("Percentage of alterations in Spike protein " + str(Spike/(25384-21562)))
print("High-conservation positions" + str([(i+1,df.loc[i,'C']) for i in range(21562,25384)  if df.loc[i,'C'] > THREADHOLD]))

ORF3A = sum([ 1 for seq in df[25394:26222]['C'] if seq != 0.0])
print("No. of alterations in ORF3A gene " + str(ORF3A))
print("Percentage of alterations in ORF3A gene " + str(ORF3A/(26220-25392)))
print("High-conservation positions" + str([(i+1,df.loc[i,'C']) for i in range(25394,26222)  if df.loc[i,'C'] > THREADHOLD]))

N = sum([ 1 for seq in df[28276:29535]['C'] if seq != 0.0])
print("No. of alterations in N gene " + str(N))
print("Percentage of alterations in N gene " + str(N/(29535-28276)))
print("High-conservation positions" + str([(i-2,df.loc[i,'C']) for i in range(28276,29535)  if df.loc[i,'C'] > THREADHOLD]))


print("\nB.1.1.7 strain?")
print("C3267T "+ str(df.loc[3266,'ft']))
print("C5388A "+ str(df.loc[5387,'fa']))
print("T6954C "+ str(df.loc[6953,'fc']))
print("A23063T "+ str(df.loc[23062,'ft']))
print("C23271A "+ str(df.loc[23270,'fa']))
print("C23604A "+ str(df.loc[23603,'fa']))
print("C23709T "+ str(df.loc[23708,'ft']))
print("T24506G "+ str(df.loc[24505,'fg']))
print("G24914C "+ str(df.loc[24913,'fc']))
print("C27972T "+ str(df.loc[27974,'ft']))
print("G28048T "+ str(df.loc[28050,'ft']))
print("A28111G "+ str(df.loc[28113,'fg']))
print("28280 GAT->CTA "+ str((df.loc[28282,'fc']+df.loc[28283,'ft']+df.loc[28284,'fa'])/3))
print("C28977T "+ str(df.loc[28979,'ft']))