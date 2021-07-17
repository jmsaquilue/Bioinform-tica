#!/bin/bash
# Autor: José Manuel Sánchez Aquilué
# align.bash
# 14/4/21

DIR="datosPractica5"

time mafft --maxiterate 1000 --6merpair --thread -1 --addfragments $DIR/gisaid_hcov-19_2021_03_23_B117.fasta $DIR/RefSeqWuhan.fasta > foo.fasta
time mafft --maxiterate 1000 --6merpair --thread -1 --addfragments $DIR/gisaid_hcov-19_2021_03_23_catHC3.fasta foo.fasta > aligment.fasta
rm foo.fasta
