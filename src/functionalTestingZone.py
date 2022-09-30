# multiple_files = [('files[]', (1)),
#                     ('files[]', (2))]

# print(multiple_files)



# import os

# class TestingZone(object):

#     localpath = os.getcwd()+"\\Output_Samples\\"
    
#     def makeValidFileList(self,fileList:list):
#         valid_list:list = [None] * len(fileList)
#         i = -1
#         for file in fileList:
#             if not(file.endswith(".csv")):
#                 file = file +".csv"
            
#             # print(self.localpath + file)
#             if(os.path.exists(self.localpath + file)):
#                 i = i + 1
#                 valid_list[i] = ('files[]', self.localpath + file)

#             filteredList = list(filter(None, valid_list))

#         return filteredList

# a = TestingZone()

# myList = ["2022-09-29T04-05-00.csv","2022-09-29T04-05-01.csv","2022-09-29T04-05-02.csv","2022-09-29T04-05-08.csv"]
# b = a.makeValidFileList(myList)

# print(b)

