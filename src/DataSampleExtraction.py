import string
from validators import FileInputValidator as FIV
import os
import pandas as pd
import numpy as np
# from validators import FileInputValidator as FIV

class DataSampleExtraction():

    fileInputValidator = FIV.FileInputValidator()

    def ReadDataSet(self, fileLookUpValue : string, type : string, value : float):

        nameValidator = self.fileInputValidator.FileNameValidator(fileLookUpValue)
        dateValidator = self.fileInputValidator.FileDateValidator(fileLookUpValue)
        timeValidator = self.fileInputValidator.FileTimeValidator(fileLookUpValue)

        if(nameValidator and dateValidator[0] and timeValidator[0] and isinstance(type, str) and isinstance(value, float)):
            localDirectory = os.getcwd()+"\\Samples"
            if (os.path.exists(localDirectory + "\\" + dateValidator[1] + '.csv')):
                localDirectory = localDirectory + "\\" + dateValidator[1] + '.csv'
                df = pd.read_csv(localDirectory) 
                self.ExtractDataSet(df, timeValidator[1])
                # print(df.to_string())

            else:
                x= 12
                print(x)
        
    def ExtractDataSet(self, completeDataFrame : pd.DataFrame, timeString : string):

        #Unoptimized Python solutions for data lookup ->  Hopefully time to optimize using my function.

        singleDataPoint = completeDataFrame.loc[completeDataFrame['TIME'] == timeString]
        print(type(singleDataPoint.values[0,1]))
        time = singleDataPoint.values[0,0]
        interValResult = self.CalculateDataSetInterval(time)
        lookupFormat = self.FormatTimeFromInteger(interValResult[0], interValResult[1])
        print("LOOKUP FORMAT " + lookupFormat)
        lookupDataPoint = completeDataFrame.loc[completeDataFrame['TIME'] == lookupFormat]

        if(pd.isna(singleDataPoint.iloc[0,1])):
            print("HEY!")
   
    def CalculateDataSetInterval(self, dataInput : pd.DataFrame):
            print(dataInput)
            minutes = int(dataInput[3:5])
            seconds = int(dataInput[6:8])
            hour = int(dataInput[:2])
        
            boundry = ((5) - ((minutes + 5) % 5)) + minutes
            currentBoundry = minutes % 5
            # Definetely needs to return Boolean from function, do it if time left.
            # If Interval call hits on current boundry go and take intervals of 5 minutes back from current.

            if(currentBoundry == 0 and seconds == 0):
                boundry = minutes
                boundry = (boundry-5)
                # minutes = (minutes - 5)
                if(boundry < 0):
                    hour = hour - 1
                    boundry = 55
                    if hour < 0:
                        hour = 23
                print(minutes)

            elif(boundry == 60):
                seconds = 0
                boundry = 0
                hour = hour + 1
                if(hour == 24):
                    hour = "00"

            return hour, boundry, seconds

    def FormatTimeFromInteger(self, hrs : int, minutes : int):
        tempList = [hrs, minutes]
        newList = [""] * 2
        print(newList)
        for i in range(len(tempList)):
            if(len(str(tempList[i])) < 2):
                newList[i] = "0" + str(tempList[i])
            else:
                newList[i] = str(tempList[i])
        return str(newList[0]+":"+newList[1]+":"+"00")
                
x = DataSampleExtraction()
y = x.ReadDataSet("2022-09-20T09:01:00","temperature", 2.1)
