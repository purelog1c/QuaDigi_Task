from doctest import Example
from utils.SampleDataGenerator import SampleDataGenerator
from validators.FileInputValidator import FileInputValidator

class Main(object):
    sampleDataGenerator = SampleDataGenerator()
    fileInputValidator = FileInputValidator()

    def pipeLineRun(self):
        startFile = input("To start generating dataset enter a fileName as starting Date (example : 2022-09-29) \n")
        if(self.fileInputValidator.FileNameValidator(startFile, 10)):
            # if(fileInputValidator.FileDateValidator(fileName)):
            endFile = input("Enter end date to start generating file (example: 2022-10-01) \n")
            if(self.fileInputValidator.FileNameValidator(endFile, 10)):
                dataSetLength = int(input("Please enter dataset length \n"))
                self.sampleDataGenerator.generateCSVFile(startFile, endFile, dataSetLength)

                    
if __name__ == "__main__":
    Main().pipeLineRun()