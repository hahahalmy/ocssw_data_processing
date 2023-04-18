#!/bin/bash

destination=/home/dell/zhujiang/ # cp destination
satellite_file=/home/dell/satellite.txt # satellite_file maybe txt is good

array=(2002 2003 2004 2005 2006 2007)
array1=(2008 2009 2010 2011 2012 2013 2014)
array3=(2015 2016 2017 2018 2019 2020 2021 2022)

houzhui=".bz2"

# Define the function to copy a single file
function copy_file {
  filename="$1"
  year=${filename:1:4}
  name=${filename:0:22} # delete \n
  echo "Copying ${filename}.bz2"
  if [[ "${array[@]}" =~ "${filename:1:4}" ]]
  then
    cp -i /data/global_aqua/${year}/${name}.bz2 $destination
  elif [[ "${array1[@]}" =~ "${filename:1:4}" ]]
  then
    cp -i /data1/global_aqua/${year}/${name}.bz2 $destination
  elif [[ "${array3[@]}" =~ "${filename:1:4}" ]]
  then
    cp -i /data3/global_aqua/${year}/${name}.bz2 $destination
  else
    echo "error: copy ${filename}.bz2"
  fi
}

# Export the function so it can be used by parallel
export -f copy_file

# Use parallel to copy the files in parallel
cat ${satellite_file} | parallel -j4 --line-buffer copy_file {}

echo "Finished copying all files"
