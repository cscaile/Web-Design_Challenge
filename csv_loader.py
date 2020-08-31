from prettytable import PrettyTable
import os
import csv
import pandas as pd
# csvpath=pd.read_csv('C://Users/Curtis Caile/Desktop/DU Bootcamp/Web-Design_Challenge/resources/Spotfireloader.csv')
csvpath='C://Users/Curtis Caile/Desktop/DU Bootcamp/Web-Design_Challenge/resources/Spotfireloader.csv'
# csv_file = open(csvpath, 'r')
# csv_text = csv_file.readlines()
# line_1=csv_text[0]
# line_1=line_1.split(',')
# line_2=csv_text[1]
df=pd.read_csv(csvpath)
table=df.to_html()
print(table)