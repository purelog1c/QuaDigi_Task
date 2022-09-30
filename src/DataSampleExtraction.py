import string
from validators import FileInputValidator as FIV
import os
import pandas as pd

class DataSampleExtraction():

    file_input_validator = FIV.FileInputValidator()


    def read_data_set(self, file_lookup_value : string, measurement_type : string, measurement_value : float):

        name_validator = self.file_input_validator.file_name_validator(file_lookup_value, 19)
        date_validator = self.file_input_validator.file_date_validator(file_lookup_value)
        time_validator = self.file_input_validator.file_time_validator(file_lookup_value)

        if(name_validator and date_validator[0] and time_validator[0] and isinstance(measurement_type , str) and isinstance(measurement_value, float)):
            local_directory = os.getcwd()+"\\Samples"
            if (os.path.exists(local_directory + "\\" + date_validator[1] + '.csv')):
                local_directory = local_directory + "\\" + date_validator[1] + '.csv'
                df = pd.read_csv(local_directory) 
                self.extract_data_set(df, time_validator[1],measurement_type = measurement_type , measurement_value = measurement_value, date = date_validator[1])

            else:
                x= 12
        
    def extract_data_set(self, complete_dataframe : pd.DataFrame, time_string : string, measurement_type: string, measurement_value:float, date:string):

        #Unoptimized Python solutions for data lookup ->  Hopefully time to optimize using my function.

        single_data_point = complete_dataframe.loc[complete_dataframe['TIME'] == time_string]
        # print(type(singleDataPoint.values[0,1]))
        time = single_data_point.values[0,0]
        # indexing = single_data_point.index.values
        # print("INDEX" + str(indexing[0]))
        inter_val_result = self.calculate_data_set_interval(time)
        current_interval = inter_val_result[3]


        # print(measurementType)
        # print(str(singleDataPoint.values[0 , 1]))
        if(pd.isna(single_data_point.iloc[0,1])):
            print("There is no data record at the requested location")
        elif(measurement_type == str(single_data_point.values[0 , 1])):
            if(str(measurement_value) == str(single_data_point.values[0 , 2])):
                lookup_format = self.format_time_from_integer(inter_val_result[0], inter_val_result[1])
                # print("LOOKUP FORMAT " + lookupFormat)
                lookup_data_point = complete_dataframe.loc[complete_dataframe['TIME'] == lookup_format]
                # print(lookupDataPoint)
                
                if(current_interval):
                    data_smple_output = complete_dataframe.iloc[lookup_data_point.index.values[0]:single_data_point.index.values[0]+1,[0,1,2]]
                else:
                    data_smple_output = complete_dataframe.iloc[single_data_point.index.values[0]:lookup_data_point.index.values[0]+1,[0,1,2]]

                data_smple_output = data_smple_output.sort_values('measurement_value')
                local_directory_out = os.getcwd()+"\\Output_Samples"

                if not(os.path.exists(local_directory_out + "\\" + date + "T" + lookup_format.replace(":","-") + ".csv")):
                    file_name = str(local_directory_out + "\\" + date + 'T' + lookup_format.replace(":","-") + '.csv')
                    data_smple_output.to_csv(file_name , index=False)
      

    def calculate_data_set_interval(self, data_input : pd.DataFrame):
            # print(dataInput)
            minutes = int(data_input[3:5])
            seconds = int(data_input[6:8])
            hour = int(data_input[:2])
            
            current_interval = False

            boundry = ((5) - ((minutes + 5) % 5)) + minutes
            current_boundry = minutes % 5
            # Definetely needs to return Boolean from function, do it if time left.
            # If Interval call hits on current boundry go and take intervals of 5 minutes back from current.

            if(current_boundry == 0 and seconds == 0):
                boundry = minutes
                boundry = (boundry-5)
                current_interval = True
                # minutes = (minutes - 5)
                if(boundry < 0):
                    hour = hour - 1
                    boundry = 55
                    if hour < 0:
                        hour = 23
                # print(minutes)

            elif(boundry == 60):
                seconds = 0
                boundry = 0
                hour = hour + 1
                if(hour == 24):
                    hour = "00"

            return hour, boundry, seconds, current_interval

    def format_time_from_integer(self, hrs : int, minutes : int):
        tempList = [hrs, minutes]
        new_list = [""] * 2
        # print(newList)
        for i in range(len(tempList)):
            if(len(str(tempList[i])) < 2):
                new_list[i] = "0" + str(tempList[i])
            else:
                new_list[i] = str(tempList[i])
        return str(new_list[0] + ":" + new_list[1] + ":" + "00")