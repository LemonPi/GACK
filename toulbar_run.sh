#!/bin/sh
python3 toulbar_generate.sh
gawk -f cp2wcsp.awk theoutfile.txt > problem.wcsp
