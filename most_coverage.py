import pandas as pd
import itertools
import csv
import sys
import os 
from os import listdir, getcwd
from os.path import join, abspath
from glob import glob
from pathlib import Path


def findMostCoverage(mostCoverage, csv): 
    for row in csv.itertuples():
        eventCode = int(row.EventCode)
        numMentions = int(row.NumMentions)
        numSources = int(row.NumSources)
        numArticles = int(row.NumArticles) 

        # adds eventcode to dictionary without duplicates 
        # initialize the keys 
        if eventCode not in mostCoverage: 
            mostCoverage[eventCode] = {} 
            mostCoverage[eventCode]['NumMentions'] = 0 
            mostCoverage[eventCode]['NumSources'] = 0
            mostCoverage[eventCode]['NumArticles'] = 0

        if numMentions not in mostCoverage[eventCode]: 
            mostCoverage[eventCode]['NumMentions'] += numMentions 
      
        if numSources not in mostCoverage[eventCode]:
            mostCoverage[eventCode]["NumSources"] += numSources 

        if numArticles not in mostCoverage[eventCode]:
            mostCoverage[eventCode]["NumArticles"] += numArticles 

def extract(): 
    # path to johns outputs directory 
    csv_path = "from_john"
    full_path = join(abspath(getcwd()), csv_path, "*.csv")

    # DICTIONARY 
    mostCoverage = {} 
    for csv in glob(full_path):
        print(csv)
        csv_reader = pd.read_csv(csv, index_col=False, low_memory=False)
        findMostCoverage(mostCoverage, csv_reader)
        
    # # make csv 
    print(sorted(mostCoverage.items()))
    outputCSV(mostCoverage)

    # for testing 1 csv 
    # csv_reader = pd.read_csv("/Users/timothylee/School/data-mining-project/src/from_john/20191020_Mentions_Sources_Articles_by_EventCode.csv", index_col=False, low_memory=False)
    # findMostCoverage(mostCoverage, csv_reader)
    # print(sorted(mostCoverage.items()))

def outputCSV(mostCoverage):
    fields = ['EventCode', 'NumMentions', 'NumSources', 'NumArticles']

    outputfile_path = './most_coverage/most_coverage.csv'
    os.makedirs(os.path.dirname(outputfile_path), exist_ok=True)

    with open(outputfile_path, "w", newline='') as f:
        w = csv.DictWriter(f, fields) 
        w.writeheader()
        for key, val in sorted(mostCoverage.items()):
            row = {'EventCode' : key}
            row.update(val)
            w.writerow(row)


if __name__ == "__main__":
    extract() 