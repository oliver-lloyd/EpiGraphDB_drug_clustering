#!/bin/bash

for directory in $(ls raw)
do
    cd raw/$directory

    # Unzip list
    gunzip *.gz 

    # Stitch header to list
    touch temp
    cat *.header >> temp
    cat $directory.csv >> temp
    mv temp $directory.csv

    cd ../..
done