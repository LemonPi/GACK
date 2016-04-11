#!/bin/sh
set -e
PYTHONHASHSEED=1000 python3 toulbar_generate.py
cd ..
gawk -f cp2wcsp.awk prototype2/theoutfile.txt > problem.wcsp
toulbar2-0.9.8-x86_64/bin/toulbar2 -timer=90 -s problem.wcsp |tee problemout.txt
python3 toulbar_display.py problemout.txt prototype2/theoutfile.txt prototype2/removedvars.txt | tee prototype2/solutionout.txt
cd prototype2
python3 generate_flower_list.py
cpp -P -o draw_results.html template_draw_results.html
echo "Results saved to draw_results.html"
echo "Visualize results by running:"
echo "./show_results_in_browser.sh"
echo "which will start an HTTP server at port 8000 and open Firefox with the results"
