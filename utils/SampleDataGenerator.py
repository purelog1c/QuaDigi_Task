import pandas as pd
import datetime
import openpyxl
import random
import os

class SampleDataGenerator():

    def generateDate(startDate, endDate):
        #"27-09-2022" follow this format
        start = datetime.datetime.strptime(startDate, "%d-%m-%Y")
        end = datetime.datetime.strptime(endDate, "%d-%m-%Y")
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        return date_generated

    def generateTimeStamp(self, dataLength):
        startTime = random.randrange(1, 24)
        endTime = random.randrange(1, 24)

        if(startTime == endTime):
            self.generateTimeStamp()
        if(startTime > endTime):
            tempTime = startTime
            startTime = endTime
            endTime = tempTime

        dataSet = pd.date_range(str(startTime)+":00:00", str(endTime)+":00:00", freq="1s").strftime('%H:%M:%S')
        dataFrame = pd.DataFrame(dataSet[:dataLength],columns=["TIME"])   
        
        return dataFrame

    def generateXMLOrCSVFile(self, startDate, endDate, dataLength):
        localDirectory = os.getcwd()+"\\Samples"
        fileNames = SampleDataGenerator.generateDate(startDate,endDate)
        for fileName in fileNames:
            if not(os.path.exists(localDirectory + "\\" + fileName)):
                generatedDataSet = self.generateTimeStamp(dataLength)


                
a = SampleDataGenerator()
b = a.generateTimeStamp(10)
print(b)