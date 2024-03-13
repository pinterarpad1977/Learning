#!/bin/bash

for current_number in  1 2 3 4 5 6 7 8 9 10
do
    echo $current_number
    sleep 1
done

echo "This is outside of the for loop."

# ----- Improvement 1 --------------------

for n in  {1..10}
do
    echo $n
    sleep 1
done

echo "This is outside of the for loop."

# ----- Improvement 2 --------------------
# this will create a tarball of all the log files within the logfiles dir

for file in logfiles/*.log
do
    tar -czvf $file.tar.gz $file
done




