import pandas as pd
import datetime
import os

class SampleDataGenerator():
    def generateDate(startDate, endDate):
        #"27-09-2022" follow this format
        start = datetime.datetime.strptime(startDate, "%d-%m-%Y")
        end = datetime.datetime.strptime(endDate, "%d-%m-%Y")
        date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        return date_generated
        # for date in date_generated:
        #     print(date.strftime("%d-%m-%Y"))
#  def generateTimeStamp(startTime, endTime):
    def generateTimeStamp():
        localDirectory = os.getcwd()+"\\Samples"
        # fileNameList = SampleDataGenerator.generateDate(startTime, endTime)
        if os.path.exists(localDirectory):
            print("Yes")
        #"09:30:00" follow this format
        # for fileName in fileNameList:

        # a = pd.date_range(startTime, endTime, freq="1s").strftime('%H:%M:%S')
        # return a

    # def generateXMLFile(startDate, endDate, startTime, endTime, setLength):



SampleDataGenerator.generateTimeStamp()



# x = SampleDataGenerator.generateDate("27-09-2022", "30-09-2022")
# for date in x:
#     print(date.strftime("%d-%m-%Y"))


