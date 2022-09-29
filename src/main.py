from DataSampleExtraction import DataSampleExtraction
from fileupload import FileUpload
from utils.SampleDataGenerator import SampleDataGenerator
from validators.FileInputValidator import FileInputValidator

class Main(object):
    sampleDataGenerator = SampleDataGenerator()
    fileInputValidator = FileInputValidator()
    dataSampleExtraction = DataSampleExtraction()
    fileUpload = FileUpload()

    def isValidDataLength(self, dataLength):
        if dataLength>100:
            if dataLength > 5000:
                print("It is a testing environment, maybe input smaller length like from 500 to 5000")
                return False
            return True
        else:
            print("Data length should be between 100 - 5000")
            return False

              
    def pipeLineCreateSample(self):
        fileName = input("input full filename as given example input: (2022-09-20T09:31:05)\n")
        while not(self.fileInputValidator.FileNameValidator(fileName, 19)):
             fileName = input("Incorrect input, input full filename with Date-T-Time to create 5 min interval output sample.Example input: (2022-09-20T09:31:05)\n")

        inputType = input("Specify type as SpO2, HeartRate or temperature\n")
        while not(self.fileInputValidator.TypeValidator(inputType)):
            inputType = input("Specify type as SpO2, HeartRate or temperature (example : SpO2)\n")

        inputValue = float(input("What value are you looking for at that time and type ?\n"))
        self.dataSampleExtraction.ReadDataSet(fileName,inputType,inputValue)


    def pipeLineGenerate(self):
        startFile = input("To start generating dataset enter a fileName as starting Date (example : 2022-09-29) \n")
        while not(self.fileInputValidator.FileNameValidator(startFile, 10)):
            startFile = input("To start generating dataset enter a fileName as starting Date (example : 2022-09-29) \n")
            # if(fileInputValidator.FileDateValidator(fileName)):
        endFile = input("Enter the ending date: (example: 2022-10-01) \n")
        while not(self.fileInputValidator.FileNameValidator(endFile, 10)):
            endFile = input("Incorrect date expression, Enter the ending date: (example: 2022-10-01) \n") 
            
        while not(self.fileInputValidator.FileDateValidator(endFile)):
            endFile = input("Date format is incorrect please follow the date format as shown -> YYYY-MM-DD \n")  
        
        dataSetLength = int(input("Please enter dataset length \n"))

        while not(self.isValidDataLength(dataSetLength)):
            dataSetLength = int(input("Please enter dataset length \n"))

        self.sampleDataGenerator.generateCSVFile(startFile, endFile, dataSetLength)
        

    def fileString2fileList(self, fileString:str):
        fileList = fileString.split(",")
        return fileList

    def generatorOrCreator(self):
        fileOperationOrFileUpload = input('Would you like to make file operation or fileUpload ? (Op/Upload) \n')

        if(fileOperationOrFileUpload.lower() == "Upload".lower()):
            files = input('write the FileName (Not full path). If multiple files, seperate each Filename with ",".\n') 
            fileList = self.fileString2fileList(files)
            print(fileList)
            self.fileUpload.fileUpload(fileList)
        elif(fileOperationOrFileUpload.lower() == "Op".lower()):
            generatorOrCreator = input('Would you like to generate or extract file sample ? (G/C) \n')
        if( generatorOrCreator.lower() == "g" ):
            self.pipeLineGenerate()
        if(generatorOrCreator.lower()== "c"):
            self.pipeLineCreateSample()            


if __name__ == "__main__":
    Main().generatorOrCreator()