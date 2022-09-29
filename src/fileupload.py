import requests
import json
import os
class FileUpload(object):

    localpath = os.getcwd()+"\\Output_Samples\\"
    
    def makeValidFileList(self, fileList:list):
        valid_list:list = [None] * len(fileList)
        i = -1
        for file in fileList:
            if not(file.endswith('.csv')):
                file = file +".csv"
                print(file)
            
            if(os.path.exists(self.localpath + file)):
              i = i + 1
              valid_list[i] = ('files[]', (file, open(self.localpath + file,'rb')))

# multiple_files = [('files[]', ('test1.csv', open(filepath, 'rb'))),
#             ('files[]', ('test2.csv', open(filepath2, 'rb')))]


        filteredList = list(filter(None, valid_list))
        
        return filteredList

    def fileUpload(self, fileNameList : list):
        
        filteredList = self.makeValidFileList(fileNameList)
        print(filteredList)
        
        url = "http://127.0.0.1:5000//upload"

        # filepath = os.getcwd()+"\\Output_Samples\\2022-09-20T09-05-00.csv"


        response = requests.post(url, files = filteredList)
        
        print("Status Code", response.status_code)
        print("JSON Response ", response.json())
