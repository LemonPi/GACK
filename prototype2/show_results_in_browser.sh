#!/bin/bash
set -m
cd ..
python3 -m http.server &
sleep 1
firefox http://localhost:8000/prototype2/draw_results.html
echo "Ctrl+C to exit."
fg
