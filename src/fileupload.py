import requests
import json
import os
class FileUpload(object):

    localpath = os.getcwd()+"\\Output_Samples\\"
    
    def make_valid_file_list(self, file_list:list):
        valid_list:list = [None] * len(file_list)
        i = -1
        for file in file_list:
            if not(file.endswith('.csv')):
                file = file +".csv"
            
            if(os.path.exists(self.localpath + file)):
              i = i + 1
              valid_list[i] = ('files[]', (file, open(self.localpath + file,'rb')))

        filtered_list = list(filter(None, valid_list))
        
        return filtered_list

    def file_upload(self, file_name_list : list):
        
        filtered_list = self.make_valid_file_list(file_name_list)

        url = "http://127.0.0.1:5000//upload"

        # filepath = os.getcwd()+"\\Output_Samples\\2022-09-20T09-05-00.csv"


        response = requests.post(url, files = filtered_list)
        
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())
