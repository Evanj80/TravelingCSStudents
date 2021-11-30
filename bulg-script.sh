#!/bin/bash
python nearestneighbor.py;
for i in {1..10}; do
    echo === Start at $i ===;
    echo python nearestneighbor.py bulgaria-small.tsp bulgaria-small-edges.tsp $i;
    python nearestneighbor.py bulgaria-small.tsp bulgaria-small-edges.tsp $i > result-bsmall-$i.txt;
    echo -e =============='\n';
done
