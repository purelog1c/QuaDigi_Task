import pandas as pd
import datetime
import numpy as np
import random
import os
import itertools

from validators.FileInputValidator import FileInputValidator

class SampleDataGenerator(object):
    file_input_validator = FileInputValidator()
    # This Function generates DataSet for {DataType and, value} individually for each corresponding [Column, Row]
    def generate_data_with_data_type(self, data_length):
        data_array = np.empty([2,data_length], dtype=object)
        for i in range(data_length):
            percentage = random.randrange(0,101)
            if (percentage >= 90):
                type_random_index = random.randrange(0,3)
                 #Lambda Operation Start
                # Just to show that Lambas are created just for similar purposes, If required ofcourse additional functions could be created for each type or depending on structure
                check_type_generate_number = lambda temp, spo2, HR : temp if(type_random_index == 0) else spo2 if(type_random_index == 1) else HR
                # Advantage of lambdas continue by how we can extract list from lamba inputs. Here we have a long line but we would probably have much larger LODs if not lambdas  
                type_value = check_type_generate_number(["temperature", round(random.uniform(35.0, 42.0),2)], 
                ["SpO2", round(random.uniform(92.0, 98.0),2)], 
                ["HeartRate", round(random.uniform(40.0, 120.0),2)])
                #Lambda Operation Ends

                data_array[0,i] = type_value[0]
                data_array[1,i] = type_value[1]
            else:
                type_value = np.nan
                data_array[0,i] = type_value
                data_array[1,i] = type_value

        return data_array

    def generate_date(self, start_date, end_date):
        #"27-09-2022" follow this format
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        delta = datetime.timedelta(days=1)
        # i = -1
        date_generated = []
        while start <= end:
            date_generated.append(start)
            start += delta
        # date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
        return date_generated


    def generate_time_stamp(self, data_length):
        start_time = random.randrange(0, 23)
        end_time = random.randrange(0, 23)

        if(start_time == end_time):
            self.generate_time_stamp(data_length = data_length)
        elif(start_time > end_time):
            tempTime = start_time
            start_time = end_time
            end_time = tempTime

        data_set = pd.date_range(str(start_time)+":00:00", str(end_time)+":00:00", freq="1s").strftime('%H:%M:%S')
        data_frame = pd.DataFrame(data_set[:data_length],columns=["TIME"])   
        
        return data_frame

    def generate_csv_file(self, start_date, end_date, data_length):
        local_directory = os.getcwd()+"\\Samples"
        
        start_date = self.file_input_validator.file_date_validator(start_date)[1]
        end_date = self.file_input_validator.file_date_validator(end_date)[1]
        file_names = self.generate_date(start_date, end_date)
        for file_name in file_names:
            file_name = file_name.strftime("%Y-%m-%d")

            if not(os.path.exists(local_directory + "\\" + file_name)):
                dataset_2D_list = self.generate_data_with_data_type(data_length=data_length)
                type_and_value_data_set = {'measurement_type': np.hstack(np.array(dataset_2D_list[0,:], dtype=object)).tolist(), 
                'measurement_value':np.hstack(np.array(dataset_2D_list[1,:], dtype=object)).tolist()}   
                type_and_value_data_set = pd.DataFrame(type_and_value_data_set)
                generated_dataset = self.generate_time_stamp(data_length)
                generated_dataset  = pd.concat([generated_dataset , type_and_value_data_set],axis=1)
                # if(str(xmlOrCSV).lower() == "csv"):
                generated_dataset .to_csv(local_directory + '\\' + file_name +'.csv',encoding='utf-8', index=False)
                # if(str(xmlOrCSV).lower() == "xlsx"):
                #     generatedDataSet.to_excel(localDirectory + '\\' + fileName +'.xlsx')


# a = SampleDataGenerator()
# b = a.generateXMLOrCSVFile("2022-09-20","2022-09-22",10000, "csv")
