#!/bin/bash
# Run nearest neighbor starting at r with some test cases.
# Prints the results to stdout for testing purposes.
python nearestneighbor.py;
r=0;
for i in {1..5}; do
    echo === Test $i ===;
    echo python nearestneighbor.py testcases/test$i-vertices.txt testcases/test$i-edges.txt $r;
    python nearestneighbor.py testcases/test$i-vertices.txt testcases/test$i-edges.txt $r;
    echo -e =============='\n';
done
