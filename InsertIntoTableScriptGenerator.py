#This code generates only one script at a time
import os
import pandas as pd

extension = '.csv'

#create a list of csv files and get the path+name of the first file from the list
file_name = 'src/' + [file for file in os.listdir('src') if file.endswith(extension)][0]

#read the csv file in pandas
df = pd.read_csv(file_name)
#===========================IF REQUIRED===========================
#drop the last n columns from the data frame
# df_cleaned = df.drop(df.columns.values[-5:], axis = 1)

if 'df_cleaned' not in globals():
    df_cleaned = df

#name of the data load script file
loadingFileName = file_name[:-4] + '.sql'

#create a file
#the script will be created in src/GENERATED SCRIPTS/fileName.sql
insertFileName = 'src/GENERATED SCRIPT/' + loadingFileName[4:] 
insertFile = open(insertFileName, "w")

#table file from which insert into part of the script will be taken
tableColumnHeaderFile = open('src/Table Column Headers.sql','r')
tableColumnHeaders = tableColumnHeaderFile.read()

#print the rows from the dataframe as columns into the sql script file
for index, row in df_cleaned.iterrows():
    print("(", end = '', file = insertFile)
    for i in row:
        print(f"'{i}'", end = ',', file = insertFile)
    print(")", end = "", file = insertFile)

    #check if it is the last row, if yes, print ; instead of new lines and comma
    if index == df_cleaned.index[-1]:
        print(";", end = "", file = insertFile)
    else:
        print(",\n", file = insertFile)
    
#close the file
insertFile.close()

#open the file in read text mode
fin = open(insertFileName, "rt")

#read the file and store the text in a variable called data
data = fin.read()

#replace the last "'nan'," of each line with '' in the data variable
data = data.replace("'nan',","''")

#save changes and close the file
fin.close()

#open the file in write text mode
fin = open(insertFileName, "wt")

#overwrite the data in the file with the text stored in the data variable
fin.write(data)

#save changes and close the file
fin.close()