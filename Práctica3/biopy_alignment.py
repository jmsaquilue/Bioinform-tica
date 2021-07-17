# Bioinformatica practica 3 
# Jose Manuel Sanchez Aquilue, 759267
# 10-3-21

from Bio import SeqIO, Seq


from Bio.Align import MultipleSeqAlignment, PairwiseAligner
from Bio.pairwise2 import format_alignment


def get_gap_positions(ref):
	positions = set([])

	for i in range(len(ref)):
		if ref[i] == '-':
			positions.add(i)

	return positions


def aligment(records, c, filename):
	
	c = c[0]

	numSeq = len(records)
	# Alinear todas las secuencias con la de referencia
	alignments = []
	for i in range(numSeq):
		print("Aligning sequence "+str(i))
		aligner = PairwiseAligner(match_score=1.0,mismatch_score=-3.0,target_internal_open_gap_score=-5.0,target_internal_extend_gap_score=-2.0)
		al = aligner.align(c.seq, (records[i]).seq)
		alignments.append(al[0])
	

	string = str(format(alignments[0]))
	ref_alfa = string.split('\n')[0]
	S1 = string.split('\n')[2]

	positionsRef = get_gap_positions(ref_alfa)

	MSA = MultipleSeqAlignment([]) # Alineamiento grande

	MSA.add_sequence("NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",ref_alfa)

	MSA.add_sequence("S1",S1)



	for i in range(1,numSeq):
		
		ref_alfa = MSA[0]
		string = str(format(alignments[i]))
		ref_beta = string.split('\n')[0]
		S1 = string.split('\n')[2]

		positions = get_gap_positions(ref_beta)

		diference = positions - positionsRef

		inverse_diference = positionsRef - positions

		positionsRef = positionsRef.union(positions)

		for pos in diference:	
			shift = len([el for el in inverse_diference if el < pos])
			shift += pos 
			ref_alfa.seq = (ref_alfa.seq)[:shift] + '-' + (ref_alfa.seq)[shift:]

		for pos in inverse_diference:
			shift = len([el for el in diference if el < pos])
			shift += pos
			S1 = S1[:shift] + '-' + S1[shift:]


		new_alignment = MultipleSeqAlignment([])
		new_alignment.add_sequence("NC_045512.2 Severe acute respiratory syndrome coronavirus 2 isolate Wuhan-Hu-1, complete genome",str(ref_alfa.seq))
		
		print("Adding sequence "+str(i))

		for j in range(1,len(MSA)):
			for pos in diference:
				shift = len([el for el in inverse_diference if el < pos])
				shift += pos 
				# shift = pos

				(MSA[j]).seq = ((MSA[j]).seq)[:shift] + '-' + ((MSA[j]).seq)[shift:]

			new_alignment.add_sequence("S"+str(j+1),str((MSA[j]).seq))

		new_alignment.add_sequence("S1",S1)

		MSA = new_alignment


	with open(filename, "w") as output_handle:
		for record in MSA:
			SeqIO.write(record, output_handle, "fasta")


		
import time
start_time = time.time()
aligment(list(SeqIO.parse("secuencias/Aragon1_gisaid_hcov-19_2021_03_02.fasta", "fasta")),list(SeqIO.parse("secuencias/RefSeqWuhan.fasta", "fasta")),"alineamientos/biopy_Aragon1.fasta")
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
aligment(list(SeqIO.parse("secuencias/Aragon2_gisaid_hcov-19_2021_03_02.fasta", "fasta")),list(SeqIO.parse("secuencias/RefSeqWuhan.fasta", "fasta")),"alineamientos/biopy_Aragon2.fasta")
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
aligment(list(SeqIO.parse("secuencias/Todo_Aragon_gisaid_hcov-19_2021_03_02.fasta", "fasta")),list(SeqIO.parse("secuencias/RefSeqWuhan.fasta", "fasta")),"alineamientos/biopy_TodoAragon.fasta")
print("--- %s seconds ---" % (time.time() - start_time))
