#!/bin/bash
# Run nearest neighbor for bulgaria dataset with 10 villages.
# b10out is the working directory for this script.
# b10fin contain saved results that were posted onto the report and slides.
python nearestneighbor.py;
output='bulgaria10'
outdir='b10out'
vertex='bulgaria/bulgaria10.tsp'
edges='bulgaria/bulgaria10-edges.tsp'
# start at each vertex from 1 to 10, and save results.
for i in {01..10}; do
    python nearestneighbor.py $vertex $edges $i > $outdir/result-$output-$i.txt;
done
# Concatenate results to a single output file.
tail -n15 $outdir/result-$output*.txt > $outdir/results-$output.txt
