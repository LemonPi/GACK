## GaCK: Garden Creation Kit

### Setup

Toulbar2 is required to run this program. Run

`./setup_toulbar.sh`

to download and install Toulbar2 in the current directory.

### Running GaCK

There are two versions of the program: Prototype1 (older) and Prototype2 (newer). To use:

```
cd prototype1
./toulbar_run.sh
```

replace prototype1 with prototype2 to run prototype2.

Currently there's no way to specify user preferences - the two protytypes have a hardcoded preference for the 3 cell to bloom red in summer to simulate a user preference.

To visualize the results, paste the result into the source of draw_results.html, and click "Spring", "Summer", or "Fall" to visualize the colours of the garden in each respective season.

### Other experiments

We developed our own weighted CSP solver; this is located in cspbase.py. Unfortunately the performance was not sufficient for this assignment, so Toulbar2 was used instead. More information can be found in our report.

Three benchmarks of this solver is included:

- ourcsp_warehouse.py: port of Toulbar2's validation/default/warehouse.cp

To run ourcsp_warehouse.py:

`python3 ourcsp_warehouse.py`

To run the equivalent test using Toulbar2:

`time ./toulbar_translateandrun.sh toulbar2-0.9.8-x86_64/share/doc/validation/default/warehouse.cp`

- ourcsp_warehouse_allsoft.py: warehouse with all hard constraints converted to soft constraints of 10000 weight each

To run ourcsp_warehouse_allsoft.py:

`python3 ourcsp_warehouse_allsoft.py`

To run the equivalent test using Toulbar2:

`time ./toulbar_translateandrun.sh warehouse_allsoft.cp`

- ourcsp_celar.py: port of Toulbar2's validation/default/celar6sub0.cp

To run ourcsp_celar.py:

`python3 ourcsp_celar.py`

To run the equivalent test using Toulbar2:

`time ./toulbar_translateandrun.sh toulbar2-0.9.8-x86_64/share/doc/validation/default/celar6sub0.cp`
