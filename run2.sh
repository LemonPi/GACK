#!/bin/sh
python3 cell.py
gawk -f cp2wcsp.awk theoutfile.txt > problem.wcsp
