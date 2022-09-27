import pandas as pd
import datetime
# import openpyxl
import random
import os

class SampleDataGenerator():

    def generateDate(startDate, endDate):
        #"27-09-2022" follow this format
        start = datetime.datetime.strptime(startDate, "%d-%m-%Y")
        end = datetime.datetime.strptime(endDate, "%d-%m-%Y")
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        print(date_generated)
        return date_generated
    

    def generateTimeStamp(self, dataLength):
        startTime = random.randrange(1, 24)
        endTime = random.randrange(1, 24)

        if(startTime == endTime):
            self.generateTimeStamp(dataLength=dataLength)
        if(startTime > endTime):
            tempTime = startTime
            startTime = endTime
            endTime = tempTime
        
        

        dataSet = pd.date_range(str(startTime)+":00:00", str(endTime)+":00:00", freq="1s").strftime('%H:%M:%S')
        dataFrame = pd.DataFrame([dataSet[:dataLength]],columns=["TIME"])   
        
        return dataFrame

    

    def generateXMLOrCSVFile(self, startDate, endDate, dataLength,xmlOrCSV):
        localDirectory = os.getcwd()+"\\Samples"
        fileNames = SampleDataGenerator.generateDate(startDate,endDate)
        for fileName in fileNames:
            fileName = fileName.strftime("%d-%m-%Y")
            print(fileName)
            if not(os.path.exists(localDirectory + "\\" + fileName)):
                generatedDataSet = self.generateTimeStamp(dataLength)
                if(str(xmlOrCSV).lower() == "csv"):
                    generatedDataSet.to_csv(localDirectory + '\\' + fileName +'.csv',encoding='utf-8', index=False)
                if(str(xmlOrCSV).lower() == "xlsx"):
                    generatedDataSet.to_excel(localDirectory + '\\' + fileName +'.xlsx')

                
a = SampleDataGenerator()
b = a.generateXMLOrCSVFile("27-09-2022","30-09-2022",10000, "csv")
# print(b)