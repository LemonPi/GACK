#!/bin/sh
rm problem.wcsp
set -e
gawk -f cp2wcsp.awk $1 >problem.wcsp
toulbar2-0.9.8-x86_64/bin/toulbar2 -s problem.wcsp
