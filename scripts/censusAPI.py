# import packages

from us import states
import pandas as pd
import requests

# import doc with API key

import config

# import list of indexes to pull from Census API

from Data import censusIndex


# Import School District CSV
# If a user is interested in looking at only select parts of the entire US Census set, save a separate text file with your list. 

def schoolDistrictCSV(CSVFile):
    schoolDistrict = pd.read_csv(CSVFile, names=['School District Name'])
    return schoolDistrict


# GEOIDs are going to be critical to using the Census API.

# Create a new Dataframe, which combines all rows based on their "School District Name."
# This will allow that first layer of filtering to happen -> you get the GEOIDs for all of the school districts you are interested in looking at.
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
# Need to be a single string in order to run Census API call

def GEOIDonly(dataFrame):
    x = dataFrame['GEOID'].tolist()
    separator = ','
    y = separator.join(map(str, x))
    return y

# separator has to have no spaces between the values
# if there is a space, it won't work when inputting variables into Census API

def nameList(dataFrame):
    x = dataFrame['name'].tolist()
    separator = ','
    nameSingleString = separator.join(map(str, x))
    return str(nameSingleString)


# Get Table Names from Census API
# URL from Census API that lists all variables from American Community Survey as a JSON

detTabURL = "https://api.census.gov/data/2019/acs/acs5/variables"
dataProfURL = "https://api.census.gov/data/2019/acs/acs5/profile/variables"

# request method which will return data from URL

censusDetTabVarNames = requests.request("GET", detTabURL)
censusDatProfVarNames = requests.request("GET", dataProfURL)

# JSON data can be displayed in a pandas dataframe
# JSON data from Census API has headers included


def jsontodf(response):
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])

censusDataDetailedTable = jsontodf(censusDetTabVarNames)
    #pd.DataFrame(columns=censusDetTabVarNames.json()[0], data=censusDetTabVarNames.json()[1:])

# must sort by Census data name because the json function returns them randomized
# you must reset the index so that the first item is 0 rather than the random numbers the dataframe assigns to each object
censusDataDetailedTable = (censusDataDetailedTable.sort_values(by=['name'], axis=0))
censusDataDetailedTable.reset_index(drop = True, inplace = True)


# Filter censusDataDetailedTable by index, name, label, or concept

def filterByTableName(string):
    x = censusDataDetailedTable[censusDataDetailedTable['name'].str.contains(string)]
    return x

    # nameList = ['B01001_002E']
    # filterByTableNameNewList(nameList)

def filterByLabel(string):
    x = censusDataDetailedTable[censusDataDetailedTable['label'].str.contains(string)]
    return x
    # filterByLabel('Median income')


# fitler table by index

def filterByIndex(indexList):
    df = censusDataDetailedTable[censusDataDetailedTable.index.isin(indexList)]
    df.reset_index(drop = True, inplace = True)
    return df

# Census API CAlls

def dataProfile(nameAsList,schDisID,stateId):
    URL = "https://api.census.gov/data/2019/acs/acs5/profile?get=NAME,{0}&for=school%20district%20(unified):{1}&in=state:{2}&key={3}".format(nameAsList,schDisID,stateId,config.MY_API_KEY)
    return requests.request("GET", URL)
    # selectedDatProVar = 'DP05_0002E,DP05_0003E'
    # dataProfile(selectedDatProVar,NYGEOID,36).head()

def deTabSchDistYear(year,nameAsList,schDisID,stateId):
    URL = "https://api.census.gov/data/{0}/acs/acs5/?get=NAME,{1}&for=school%20district%20(unified):{2}&in=state:{3}&key={4}".format(year,nameAsList,schDisID,stateId,config.MY_API_KEY)
    return requests.request("GET", URL)
    # selectedDatProVar = 'DP05_0002E,DP05_0003E'
    # dataProfile(selectedDatProVar,NYGEOID,36).head()

def deTabSchDist(nameAsList,schDisID,stateId):
    URL = "https://api.census.gov/data/2019/acs/acs5/?get=NAME,{0}&for=school%20district%20(unified):{1}&in=state:{2}&key={3}".format(nameAsList,schDisID,stateId,config.MY_API_KEY)
    return requests.request("GET", URL)
    # selectedDetTabVar = 'B01001_002E,B01001_026E,B19013_001E'
    # detailedTable(selectedDetTabVar,NYGEOID,36).head(1)

def detailedTable(nameAsList,schDisID,stateId):
    x = deTabSchDist(nameAsList,schDisID,stateId)
    return jsontodf(x)

def detailedTableYear(year,nameAsList,schDisID,stateId):
    x = deTabSchDistYear(year,nameAsList,schDisID,stateId)
    return jsontodf(x)   
# Take values in a data frame column and turn to list

def dfColToList(dataFrame,columnName):
    x = dataFrame[str(columnName)].tolist()
    return x

# Convert data in column to integers

def dfColDataToInt(dataFrame,columnName):
    dataFrame[columnName] = dataFrame[columnName].astype(int)
    return dataFrame

# Only works from year 2015 onward

def cenDftranspose(year,indexList,descriptionList,schDisID,stateId):
    df = filterByIndex(indexList)
    nameAsList = nameList(df)
    df.insert(loc=0, column='description', value=descriptionList)
    dfDict = pd.Series(df.description.values,index=df.name).to_dict()
    dataFrame = df.transpose()
    dfState = detailedTableYear(year,nameAsList,schDisID,stateId)
    dfState.rename(columns=dfDict,inplace = True)
    firstColumn = dfState.pop('state')
    dfState.insert(0, 'state', firstColumn)
    secondColumn = dfState.pop('school district (unified)')
    dfState.insert(1, 'school district (unified)', secondColumn)
    dfState.iloc[:, 3:,] = dfState.iloc[:, 3:,].apply(pd.to_numeric)
    return dfState

def houseYrBlt(year,schDisID,stateId):
    indexList = censusIndex.houseYrBlt
    descriptionList = censusIndex.houseYrBltDescrp
    dfNew = cenDftranspose(year,indexList,descriptionList,schDisID,stateId)
    return dfNew

def householdSize(schDisID,stateId):
    indexList = censusIndex.householdSize
    descriptionList = censusIndex.householdSizeDescrp
    dfNew=cenDftranspose(indexList,descriptionList,schDisID,stateId)
    dfNew['Average Owner Occupied Household Size'] = (dfNew['Owner Occupied']/dfNew['Average Household Size'])
    dfNew['Average Owner Occupied Household Size'] = (dfNew['Renter Occupied']/dfNew['Average Household Size'])
    return dfNew

def houseOwnership(schDisID,stateId):
    indexList = censusIndex.houseType
    descriptionList = censusIndex.houseOwnershipDescrp
    dfNew=cenDftranspose(indexList,descriptionList,schDisID,stateId)
    dfNew['Percentage of Owner Occupied'] = (dfNew['Owner Occupied']/dfNew['Total Occupied Housing Units'])
    dfNew['Percentage of Renter Occupied'] = (dfNew['Renter Occupied']/dfNew['Total Occupied Housing Units'])
    return dfNew