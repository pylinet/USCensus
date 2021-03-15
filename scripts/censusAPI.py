# import packages

from us import states
import pandas as pd
import requests


# import doc with API key

import config


# Census API Link References
# "https://api.census.gov/data/2019/acs/acs5/profile?get=NAME,DP05_0001E&for=state:36&key={0}".format(config.MY_API_KEY)
# "https://api.census.gov/data/2019/acs/acs5/profile?get=group(DP05)&for=school%20district%20(unified):29850&in=state:36&key={0}".format(config.MY_API_KEY)


# Get Table Names from Census API

# URL from Census API that lists all variables from American Community Survey as a JSON
# these are Census Detailed tables - the most detailed tables available from the ACS

detTabURL = "https://api.census.gov/data/2019/acs/acs5/variables"
dataProfURL = "https://api.census.gov/data/2019/acs/acs5/profile/variables"


# request method which will return data from URL

censusDetTabVarNames = requests.request("GET", detTabURL)
censusDatProfVarNames = requests.request("GET", dataProfURL)

# check to see if request method was successful by printing 6th object from JSON
# print(censusDetTabVarNames.json()[5])


# JSON data can be displayed in a pandas dataframe
# JSON data from Census API has headers included

censusDataDetailedTable = pd.DataFrame(columns=censusDetTabVarNames.json()[0], data=censusDetTabVarNames.json()[1:])
censusDataDetailedTable = (censusData.sort_values(by=['name'], axis=0))

# you must reset the index so that the first item is 0 rather than the random numbers the dataframe assigns to each object
censusDataDetailedTable.reset_index(drop = True, inplace = True)
censusDataDetailedTable


# filter table by name

def filterByTableName(string):
    x = censusDataDetailedTable[censusDataDetailedTable['name'].str.contains(string)]
    return x
# filterByTableName('B1')


# filter table by label

def filterByLabel(string):
    x = censusDataDetailedTable[censusDataDetailedTable['label'].str.contains(string)]
    return x
# filterByLabel('Median income')


# fitler table by list of table codes

def filterByTableName(tableList):
    df = censusDataDetailedTable[censusDataDetailedTable['name'].isin(tableList)]
    df.reset_index(drop = True, inplace = True)
    return df
# fitler table by index

def filterByIndex(indexList):
    df = censusDataDetailedTable[censusDataDetailedTable.index.isin(indexList)]
    df.reset_index(drop = True, inplace = True)
    return df

# Import CSV

# If a user is interested in looking at only select parts of the entire US Census set, save a separate text file with your list. 
# You can pick and choose which school districts after compiling all the data, but it helps to filter out the data earlier on to minimize the size of your data frame


# Returns the dataframe of school districts

def schoolDistrictCSV(CSVFile):
    schoolDistrict = pd.read_csv(CSVFile, names=['School District Name'])
    return schoolDistrict


# GEOIDs are going to be critical to using the Census API.

# Create a new Dataframe, which combines all rows based on their "School District Name."
# This will allow that first layer of filtering to happen -> you get the GEOIDs for all of the school districts you are interested in looking at.

# Need to further investigate and understand Pandas concat, merge, join. Not sure why merge worked - so need to dig into that.


# Read Census data set which lists GEOIDs per each school district in state
# For list of other states and other GEOID data sets, see URL https://www2.census.gov/geo/docs/reference/codes/files/

def schoolDistrictGEOID(URL):
    df = pd.read_csv(URL,names=['State', 'ID','GEOID','School District Name', 'Class'])
    return df


# Function that merges user CSV data frame with the GEOID data frame into a df

def mergedSchoolDist(df1, df2):
    CountiesGEOID = df1.merge(df2, on=['School District Name'],how='inner')
    return CountiesGEOID


# Get all GEOIDs in a single list
# Make all GEOIDs into a string only
# Need to be a single strin in order to run Census API call

def GEOIDonly(dataFrame):
    x = dataFrame['GEOID'].tolist()
    separator = ', '
    GEOIDsinglestring = separator.join(map(str, x))
    return GEOIDsinglestring


#Function to turn list of strings into a single string

def GEOIDonlyx(dataFrame):
    z = dataFrame['GEOID'].tolist()
    separator = ', '
    print(z)

# Need to be a single strin in order to run Census API call
# separator has to have no spaces between the values
# if there is a space, it won't work when inputting variables into Census API

def nameList(dataFrame):
    x = dataFrame['name'].tolist()
    separator = ','
    nameSingleString = separator.join(map(str, x))
    return str(nameSingleString)


def jsontodf(response):
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])


def dataProfSchDist(censusVariables,schoolDistricts):
    # first URL is for the detailed table. second URL is for the data profiles.
    # URL = "https://api.census.gov/data/2019/acs/acs5?get=NAME,{0}&for=school%20district%20(unified):{1}&in=state:36&key={2}".format(censusVariables,schoolDistricts,config.MY_API_KEY)

    URL = "https://api.census.gov/data/2019/acs/acs5/profile?get=NAME,{0}&for=school%20district%20(unified):{1}&in=state:36&key={2}".format(censusVariables,schoolDistricts,config.MY_API_KEY)
    return requests.request("GET", URL)



def deTabSchDist(censusVariables,schoolDistricts):
    # first URL is for the detailed table. second URL is for the data profiles.
    # URL = "https://api.census.gov/data/2019/acs/acs5?get=NAME,{0}&for=school%20district%20(unified):{1}&in=state:36&key={2}".format(censusVariables,schoolDistricts,config.MY_API_KEY)

    URL = "https://api.census.gov/data/2019/acs/acs5/?get=NAME,{0}&for=school%20district%20(unified):{1}&in=state:36&key={2}".format(censusVariables,schoolDistricts,config.MY_API_KEY)
    return requests.request("GET", URL)


# Mega Formula


def dataProfile(cenVar, schDisID):
    x = dataProfSchDist(cenVar,schDisID)
    return jsontodf(x)

def detailedTable(cenVar, schDisID):
    x = deTabSchDist(cenVar,schDisID)
    return jsontodf(x)

# take values in a data frame column and turn to list

def dfColToList(dataFrame,columnName):
    x = dataFrame[str(columnName)].tolist()
    return x

# convert data in column to integers

def dfColDataToInt(dataFrame1,dataFrame2,columnName):
    x = dataFrame1[str(columnName)].tolist()
    dataFrame2[x] = dataFrame2[x].astype(int)
    return dataFrame2