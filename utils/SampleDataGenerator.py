import pandas as pd
import datetime
import numpy as np
import random
import os
import itertools

class SampleDataGenerator():

    # This Function generates DataSet for Data Type and value individually for each corresponding [Column, Row]
    def generateDataWithDataType(self, dataLength):
        dataArray = np.empty([2,dataLength], dtype=object)
        for i in range(dataLength):
            percentage = random.randrange(0,101)
            if (percentage >= 90):
                typeRandomIndex = random.randrange(0,3)
                 #Lambda Operation Start
                # Just to show that Lambas are created just for similar purposes, If required ofcourse additional functions could be created for each type or depending on structure
                check = lambda temp, spo2, HR : temp if(typeRandomIndex == 0) else spo2 if(typeRandomIndex == 1) else HR
                # Advantage of lambdas continue by how we can extract list from lamba inputs. Here we have a long line but we would probably have much larger LODs if not lambdas  
                typeValue = check(["temperature", round(random.uniform(35.0, 42.0),2)], 
                ["SpO2", round(random.uniform(92.0, 98.0),2)], 
                ["HeartRate", round(random.uniform(40.0, 120.0),2)])
                #Lambda Operation Ends

                dataArray[0,i] = typeValue[0]
                dataArray[1,i] = typeValue[1]
            else:
                typeValue = np.nan
                dataArray[0,i] = typeValue
                dataArray[1,i] = typeValue

        return dataArray

    def generateDate(self, startDate, endDate):
        #"27-09-2022" follow this format
        start = datetime.datetime.strptime(startDate, "%d-%m-%Y")
        end = datetime.datetime.strptime(endDate, "%d-%m-%Y")
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        print(date_generated)
        return date_generated


    def generateTimeStamp(self, dataLength):
        startTime = random.randrange(0, 23)
        endTime = random.randrange(0, 23)

        if(startTime == endTime):
            self.generateTimeStamp(dataLength=dataLength)
        elif(startTime > endTime):
            tempTime = startTime
            startTime = endTime
            endTime = tempTime

        dataSet = pd.date_range(str(startTime)+":00:00", str(endTime)+":00:00", freq="1s").strftime('%H:%M:%S')
        dataFrame = pd.DataFrame(dataSet[:dataLength],columns=["TIME"])   
        
        return dataFrame

    

    def generateXMLOrCSVFile(self, startDate, endDate, dataLength,xmlOrCSV):
        localDirectory = os.getcwd()+"\\Samples"
        fileNames = self.generateDate(startDate, endDate)
        for fileName in fileNames:
            fileName = fileName.strftime("%d-%m-%Y")

            print(fileName)
            if not(os.path.exists(localDirectory + "\\" + fileName)):
                dataSet2DList = a.generateDataWithDataType(dataLength=dataLength)
                typeAndValueDataSet = {'measurement_type': np.hstack(np.array(dataSet2DList[0,:], dtype=object)).tolist(), 
                'measurement_value':np.hstack(np.array(dataSet2DList[1,:], dtype=object)).tolist()}   
                typeAndValueDataSet = pd.DataFrame(typeAndValueDataSet)
                generatedDataSet = self.generateTimeStamp(dataLength)
                generatedDataSet = pd.concat([generatedDataSet, typeAndValueDataSet],axis=1)
                if(str(xmlOrCSV).lower() == "csv"):
                    generatedDataSet.to_csv(localDirectory + '\\' + fileName +'.csv',encoding='utf-8', index=False)
                if(str(xmlOrCSV).lower() == "xlsx"):
                    generatedDataSet.to_excel(localDirectory + '\\' + fileName +'.xlsx')

# value = np.nan
# typeArray = np.array([np.concatenate([([i]*7) for i in [None]]),"temperature", "SpO2", "HeartRate"])  
# typeArrayExtended = np.hstack(np.array(typeArray, dtype=object)).tolist()
# print(typeArrayExtended[9])

a = SampleDataGenerator()
# dataSet2DList = a.generateDataWithDataType(100)
# dataSet2DDataFrame = {'measurement_type': np.hstack(np.array(dataSet2DList[0,:], dtype=object)).tolist()}
# print(dataSet2DDataFrame)
# b = a.generateDataWithDataType(100)
# print(b)
b = a.generateXMLOrCSVFile("27-09-2022","30-09-2022",10000, "csv")
print(b)