#!/bin/bash

# Check if python3 is installed
python3 --version >> /dev/null 2>&1
if [[ $? -gt 0 ]]
  then 
    echo " Python3 need to be installed before tests can run"
    exit
  fi
# verify dependencies  exist 
declare -a packages=(pytest pytest-html)
for i in "${packages[@]}"
do 
  pip3 show $i >> /dev/null 2>&1
  if [[ $? -gt 0 ]]
  then 
    echo "$i need to be installed before tests can run"
    exit
  fi
done
# create results folder if it does not exist
#create timestamped folder under results 
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
if [[ ! -d "../results" ]]
then 
  echo "creating results and timestamp folders"
  mkdir ../results
fi
  mkdir ../results/$timestamp
#run the tests 
pytest test_parcel_loader.py --html=../results/$timestamp/report.html
