#!/bin/sh
for file in `cat ~/Desktop/sage_testing/trac_10183_filenames.txt`; do 
    ./sage -t devel/sage/sage/$file | \
    tee -a ~/Desktop/sage_testing/trac_10183_after.txt; 
    ./sage -t --long devel/sage/sage/$file | \
    tee -a ~/Desktop/sage_testing/trac_10183_after.txt; 
done
