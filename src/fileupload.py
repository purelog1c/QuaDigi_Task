import requests
import json
import os

url = "http://127.0.0.1:5000//upload"
headers = {"Content-Type": "application/json; charset=utf-8"}

filepath = os.getcwd()+"\\Output_Samples\\2022-09-20T09-05-00.csv"
filepath2 = os.getcwd()+"\\Output_Samples\\2022-09-20T09-05-01.csv"

print(os.path.exists(filepath))

multiple_files = [('files[]', ('test1.csv', open(filepath, 'rb'))),
                      ('files[]', ('test2.csv', open(filepath2, 'rb')))]

response = requests.post(url, files = multiple_files)
 
print("Status Code", response.status_code)
print("JSON Response ", response.json())