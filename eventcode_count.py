# -*- coding: utf-8 -*-
import pandas as pd
import os 
import itertools
from glob import glob
from os.path import join, abspath
from os import listdir, getcwd
from pathlib import Path
import csv

dict = {} 


def countEventsCode(data_frame, current_date): 
    if current_date not in dict:
        dict[current_date] = {}

    for row in data_frame.itertuples(): 
        country1 = str(row.Actor1CountryCode)
        country2 = str(row.Actor2CountryCode)
        eventCode = str(row.EventCode)

        # country doesnt exist  
        if country1 not in dict[current_date]:
            dict[current_date][country1] = {} 
        if country2 not in dict[current_date]:
            dict[current_date][country2] = {} 

        # check eventCode per country    
        if eventCode not in dict[current_date][country1]: 
            dict[current_date][country1][eventCode] = 1
        else:
            dict[current_date][country1][eventCode] += 1

        if eventCode not in dict[current_date][country2]: 
            dict[current_date][country2][eventCode] = 1
        else:
            dict[current_date][country2][eventCode] += 1


def outputCSV():
    fields = ['date', 'country', 'eventCode', 'amount']
    
    with open('output.csv', 'w') as csv_file: 
        csvwriter = csv.writer(csv_file, delimiter='\t')

        for date in dict: 
            for country in dict[date]:
                for event in dict[date][country]:  
                    count = dict[date][country][event]
                    csvwriter.writerow([dict[date], dict[date][country], dict[date][country][event], count])


# with open('output.csv', 'w') as csv_file:
#     csvwriter = csv.writer(csv_file, delimiter='\t')
#     for session in users_item:
#         for item in users_item[session]:
#             csvwriter.writerow([session, item, users_item[session][item]])



def extract(): 
    params=['GLOBALEVENTID', 'SQLDATE', 'MonthYear', 'Year', 'FractionDate', 
     'Actor1Code', 'Actor1Name', 'Actor1CountryCode', 
     'Actor1KnownGroupCode', 'Actor1EthnicCode', 'Actor1Religion1Code', 
     'Actor1Religion2Code', 'Actor1Type1Code', 'Actor1Type2Code', 
     'Actor1Type3Code', 'Actor2Code', 'Actor2Name', 'Actor2CountryCode', 
     'Actor2KnownGroupCode', 'Actor2EthnicCode', 'Actor2Religion1Code', 
     'Actor2Religion2Code', 'Actor2Type1Code', 'Actor2Type2Code', 
     'Actor2Type3Code', 'IsRootEvent', 'EventCode', 'EventBaseCode', 
     'EventRootCode', 'QuadClass', 'GoldsteinScale', 'NumMentions', 
     'NumSources', 'NumArticles', 'AvgTone', 'Actor1Geo_Type', 
     'Actor1Geo_FullName', 'Actor1Geo_CountryCode', 'Actor1Geo_ADM1Code', 
     'Actor1Geo_Lat', 'Actor1Geo_Long', 'Actor1Geo_FeatureID', 
     'Actor2Geo_Type', 'Actor2Geo_FullName', 'Actor2Geo_CountryCode', 
     'Actor2Geo_ADM1Code', 'Actor2Geo_Lat', 'Actor2Geo_Long', 
     'Actor2Geo_FeatureID', 'ActionGeo_Type', 'ActionGeo_FullName', 
     'ActionGeo_CountryCode', 'ActionGeo_ADM1Code', 'ActionGeo_Lat', 
     'ActionGeo_Long', 'ActionGeo_FeatureID', 'DATEADDED', 'SOURCEURL']

    csvs_path = "unzipped_csvs"
    full_path = join(abspath(getcwd()), csvs_path, "*.CSV") 
     
    # for testing 1 file  
    # test = pd.read_csv("/Users/timothylee/School/data-mining-project/src/unzipped_csvs/20190101.export.CSV", names=params, index_col=False, low_memory=False)
    # countEventsCode(test, 20190101)
    # end for testing 1 files 

    # reading all csv files in folder 
    for csv in glob(full_path):
        p = Path(csv)
        split_date = p.name.split('.')
        current_date = split_date[0]

        csv_reader = pd.read_csv(csv, names=params, index_col=False, low_memory=False)

        countEventsCode(csv_reader, current_date)

        # print(dict)
        

if __name__ == "__main__":
    extract()
    # outputCSV()
    # print(dict)
    
