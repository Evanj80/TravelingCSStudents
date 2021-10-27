#!/bin/bash
python nearestneighbor.py;
r=0;
for i in {1..5}; do
    echo === Test $i ===;
    python nearestneighbor.py test$i-vertices.txt test$i-edges.txt $r;
    echo -e === Test $i ==='\n';
done
