#!/bin/bash
# verify dependencies  exist 

# create results folder if it does not exist
#create timestamped folder under results 
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")
if [[ ! -d "./results" ]]
then 
  echo "does not exist "
  mkdir ../results
  mkdir ../results/$timestamp
else 
  mkdir ../results/$timestamp
  echo "$timestamp"
fi
#run the tests 
pytest test_parcel_loader.py --html=../results/$timestamp/report.html
