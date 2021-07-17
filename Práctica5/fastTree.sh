#!/bin/bash
# Autor: José Manuel Sánchez Aquilué
# fastTree.sh
# 14/4/21

# ./FastTreeMP  -nt ../aligment.fasta > CAT/JC.nwk
# ./FastTreeMP ../aligment.fasta > CAT/JTT.nwk
# ./FastTreeMP -gtr -nt ../aligment.fasta > CAT/GTR.nwk
./FastTreeMP -lg ../aligment.fasta > CAT/LG.nwk
./FastTreeMP -wag ../aligment.fasta > CAT/WAG.nwk

# ./FastTreeMP  -nt  -gamma ../aligment.fasta > GAMMA/JC_GAMMA.nwk
# ./FastTreeMP ../aligment.fasta > GAMMA/JTT_GAMMA.nwk
# ./FastTreeMP -gtr -nt  -gamma ../aligment.fasta > GAMMA/GTR_GAMMA.nwk
./FastTreeMP -lg -gamma ../aligment.fasta > GAMMA/LG_GAMMA.nwk
./FastTreeMP -wag -gamma ../aligment.fasta > GAMMA/WAG_GAMMA.nwk
