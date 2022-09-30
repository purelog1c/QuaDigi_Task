from DataSampleExtraction import DataSampleExtraction
from fileupload import FileUpload
from utils.SampleDataGenerator import SampleDataGenerator
from validators.FileInputValidator import FileInputValidator

class Main(object):
    sample_data_generator = SampleDataGenerator()
    file_input_validator = FileInputValidator()
    data_sample_extraction = DataSampleExtraction()
    file_upload = FileUpload()

    def is_valid_data_length(self, data_length):
        if data_length>100:
            if data_length > 5000:
                print("It is a testing environment, maybe input smaller length like from 500 to 5000")
                return False
            return True
        else:
            print("Data length should be between 100 - 5000")
            return False

              
    def pipe_line_create_sample(self):
        file_name = input("input full filename as given example input: (2022-09-20T09:31:05)\n20")
        while not(self.file_input_validator.file_name_validator(file_name, 19)):
             file_name = input("Incorrect input, input full filename with Date-T-Time to create 5 min interval output sample.Example input: (2022-09-20T09:31:05)\n")

        input_type = input("Specify type as SpO2, HeartRate or temperature\n")
        while not(self.file_input_validator.type_validator(input_type)):
            input_type = input("Specify type as SpO2, HeartRate or temperature (example : SpO2)\n")

        input_value = float(input("What value are you looking for at that time and type ?\n"))
        self.data_sample_extraction.read_data_set(file_name, input_type, input_value)


    def pipe_line_generate(self):
        start_file = input("To start generating dataset enter a fileName as starting Date (example : 2022-09-29) \n")
        while not(self.file_input_validator.file_name_validator(start_file, 10)):
            start_file = input("To start generating dataset enter a fileName as starting Date (example : 2022-09-29) \n")
            # if(fileInputValidator.FileDateValidator(fileName)):
        end_file = input("Enter the ending date: (example: 2022-10-01) \n")
        while not(self.file_input_validator.file_name_validator(end_file, 10)):
            end_file = input("Incorrect date expression, Enter the ending date: (example: 2022-10-01) \n") 
            
        while not(self.file_input_validator.file_date_validator(end_file)):
            end_file = input("Date format is incorrect please follow the date format as shown -> YYYY-MM-DD \n")  
        
        start_file, end_file = self.file_input_validator.reorder_date(start_file, end_file)
        
        data_set_length = int(input("Please enter dataset length \n"))

        while not(self.is_valid_data_length(data_set_length)):
            data_set_length = int(input("Please enter dataset length \n"))

        self.sample_data_generator.generate_csv_file(start_file, end_file, data_set_length)
        

    def generator_or_creator(self):
        file_operation_or_file_upload = input('Would you like to make file operation or fileUpload ? (Op/Upload) \n')

        if(file_operation_or_file_upload.lower() == "Upload".lower()):
            amount_of_files = int(input("how many files will you upload ?\n"))

            while not(amount_of_files <= 10 and amount_of_files > 0):
                amount_of_files = int(input("file upload should in range of 1 and 10. Input number of files to be uploaded: \n"))
            
            all_file_list:list = ["None"] * amount_of_files
            for i in range(amount_of_files):
                file = input('write the FileName for file number: ' + str(i) + ' (Not the full path).\n')
                all_file_list[i] = file  
                               
                self.file_upload.file_upload(all_file_list)
        elif(file_operation_or_file_upload.lower() == "Op".lower()):
            generator_or_creator = input('Would you like to generate or extract file sample ? (G/C) \n')
            if(generator_or_creator.lower() == "g" ):
                self.pipe_line_generate()
            if(generator_or_creator.lower()== "c"):
                self.pipe_line_create_sample()            


if __name__ == "__main__":
    Main().generator_or_creator()