#!/bin/bash
# Bioinformatica practica 3 
# Jose Manuel Sanchez Aquilue, 759267
# 10-3-21


for name in "Aragon1" "Aragon2" "Todo_Aragon"
do
	echo $name
	echo "Métodos progresivos."
	echo "FTT-NS-1"
	time mafft --retree 1 --6merpair --addfragments secuencias/$name\_gisaid\_hcov-19\_2021\_03\_02.fasta secuencias/RefSeqWuhan.fasta > alineamientos/$name/FTT-NS-1.fasta

	echo "FTT-NS-2"
	time mafft --retree 2 --6merpair --addfragments secuencias/$name\_gisaid\_hcov-19\_2021\_03\_02.fasta secuencias/RefSeqWuhan.fasta > alineamientos/$name/FTT-NS-2.fasta

	echo "Refinamiento iterativo."
	echo "2 iteraciones"
	time mafft --maxiterate 2 --6merpair --addfragments secuencias/$name\_gisaid\_hcov-19\_2021\_03\_02.fasta secuencias/RefSeqWuhan.fasta > alineamientos/$name/2iter.fasta
	echo "1000 iteraciones"
	time mafft --maxiterate 1000 --6merpair --addfragments secuencias/$name\_gisaid\_hcov-19\_2021\_03\_02.fasta secuencias/RefSeqWuhan.fasta > alineamientos/$name/1000iter.fasta

	echo "Iterativo con puntuaciones consistentes."
	echo "E-INS"
	time mafft --genafpair --maxiterate 1000 --6merpair --addfragments secuencias/$name\_gisaid\_hcov-19\_2021\_03\_02.fasta secuencias/RefSeqWuhan.fasta > alineamientos/$name/E-INS.fasta
	echo "L-INS"
	time mafft --localpair --maxiterate 1000 --6merpair --addfragments secuencias/$name\_gisaid\_hcov-19\_2021\_03\_02.fasta secuencias/RefSeqWuhan.fasta > alineamientos/$name/L-INS.fasta
	echo "G-INS"
	time mafft --globalpair --maxiterate 1000 --6merpair --addfragments secuencias/$name\_gisaid\_hcov-19\_2021\_03\_02.fasta secuencias/RefSeqWuhan.fasta > alineamientos/$name/G-INS.fasta
done