#!/bin/sh
python3 toulbar_generate.py
cd ..
gawk -f cp2wcsp.awk prototype1/theoutfile.txt > problem.wcsp
toulbar2-0.9.8-x86_64/bin/toulbar2 -s problem.wcsp |tee problemout.txt
python3 toulbar_display.py problemout.txt prototype1/theoutfile.txt prototype1/removedvars.txt
