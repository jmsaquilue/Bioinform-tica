#!/bin/bash
for iter in 0 2 4 8
do
	for i in 1 2 3
	do
	echo "Alineamiento del apartado $i con $iter iteraciones."
	time clustalo --force -i secuencias/apartado$i.fasta -o alineamientos/apartado$i\_$iter.fasta  --iter=$iter --full --distmat-out=matrices/apartado$i\_$iter.txt
	done
done

echo "Alineamiento del apartado 6."
time clustalo --force -i secuencias/apartado6.gb -o alineamientos/apartado6.fasta  --full --distmat-out=matrices/apartado6.txt
