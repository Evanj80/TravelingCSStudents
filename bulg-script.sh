#!/bin/bash
python nearestneighbor.py;
for i in {01..10}; do
    echo python nearestneighbor.py bulgaria-small.tsp bulgaria-small-edges.tsp $i;
    python nearestneighbor.py bulgaria-small.tsp bulgaria-small-edges.tsp $i > result-bsmall-$i.txt;
done
tail -n15 result-bsmall*.txt > results-bsmall.txt
