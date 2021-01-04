#!/bin/bash

# verify dependencies  exist 
declare -a packages=(python3 pytest)
for i in "${packages[@]}"
do
  command -v $i
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
  mkdir ../results/$timestamp
else 
  mkdir ../results/$timestamp
fi
#run the tests 
pytest test_parcel_loader.py --html=../results/$timestamp/report.html
