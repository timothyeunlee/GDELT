# -*- coding: utf-8 -*-
import pandas as pd
import os 
import itertools
from glob import glob
from os.path import join, abspath
from os import listdir, getcwd
from pathlib import Path
import csv
import pandas as pd

dict1 = {} 


def countEventsCode(data_frame, current_date): 
    if current_date not in dict1:
        dict1[current_date] = {}

    for row in data_frame.itertuples(): 
        country1 = str(row.Actor1CountryCode)
        country2 = str(row.Actor2CountryCode)
        eventCode = str(row.EventCode)

        # country doesnt exist  
        if country1 not in dict1[current_date]:
            dict1[current_date][country1] = {} 
        if country2 not in dict1[current_date]:
            dict1[current_date][country2] = {} 

        # check eventCode per country    
        if eventCode not in dict1[current_date][country1]: 
            dict1[current_date][country1][eventCode] = 1
        else:
            dict1[current_date][country1][eventCode] += 1

        if eventCode not in dict1[current_date][country2]: 
            dict1[current_date][country2][eventCode] = 1
        else:
            dict1[current_date][country2][eventCode] += 1


def outputCSV():
    
    total_dataframe=pd.DataFrame()

    print(total_dataframe)

    with open('output.csv', 'w',newline='') as csv_file: 
        csvwriter = csv.writer(csv_file, delimiter='\t')
        for date in dict1:
            for country in dict1[date]:
                country_frame=pd.DataFrame(dict1[date][country],index=[country])
                
                total_dataframe=pd.concat([total_dataframe,country_frame])
                
    return(total_dataframe)

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
     
    test = pd.read_csv("C:/Users/Omar/documents/comp_541/unzipped_csvs/20190101.export.CSV", names=params, index_col=False, low_memory=False)
    countEventsCode(test, 20190101)


def frame_from_dict():
#    for country in dict1[]
    frame=pd.DataFrame.from_dict(dict1)
    print(frame)

if __name__ == "__main__":
    extract()
    total_dataframe=outputCSV()
#    print(dict1)
    
