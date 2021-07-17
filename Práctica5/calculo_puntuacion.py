# Bioinformatica practica 3 
# Jose Manuel Sanchez Aquilue, 759267
# 10-3-21

from Bio import SeqIO

def calculate_EBI(records):
	score = 0.0
	numSeq = len(records)
	total = len((records[0]).seq) * numSeq * (numSeq-1)/2
	for i in range(0, numSeq):
		print ("Sequence "+ str(i), end="\r")
		dna1 = (records[i]).seq
		for j in range(i+1,numSeq):
			dna2 = (records[j]).seq
			for k in range(len(dna1)):
				if dna1[k] == dna2[k]: score += 1

	print("EBI: " + str(score/total))


def calculate_score(records):
	score = 0
	numSeq = len(records)
	total =  numSeq * (numSeq-1)/2
	for i in range(numSeq):
		print ("Sequence "+ str(i), end="\r")
		dna1 = (records[i]).seq
		for j in range(i+1,numSeq):
			dna2 = (records[j]).seq
			firstGap = True
			for k in range(len(dna1)):
				if dna1[k] == dna2[k]: 
					score += 1
					firstGap = True
				elif dna1[k] == '-' or '-' == dna2[k]: 
					if firstGap:
						score -= 5
						firstGap = False
					else:
						score -= 2
				elif dna1[k] != dna2[k]:
					score -= 3
					firstGap = True

	print("Score: "+str(score/total))


def calc_mafft():
	# mafft
	print("Method: mafft")
	directory = "alineamientos"
	for subdir in os.listdir(directory):
		for file in os.listdir(directory+"/"+ subdir):
			path = directory +"/"+ subdir +"/"+ file
			print(path)
			records = list(SeqIO.parse(path, "fasta"))
			calculate_EBI(records)
			calculate_score(records)


def calc_bio():
	print("Method: Biopython")
	for name in ["Aragon1","Aragon2","TodoAragon"]:
		print(name)
		records = list(SeqIO.parse("alineamientos/biopy_"+name+".fasta", "fasta"))
		calculate_EBI(records)
		calculate_score(records)


def main():
	records = list(SeqIO.parse("alineamiento3.fasta", "fasta"))
	calculate_EBI(records)
	calculate_score(records)





if __name__ == '__main__':
	main()
