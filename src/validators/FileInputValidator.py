import re
import sys

from numpy import datetime_as_string

class FileInputValidator():
    date_validator = re.compile("^([0-9]{4}[-/]?((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00)[-/]?02[-/]?29)$")
    time_validator = re.compile("^(T|t)(?:(?:([01]?\d|2[0-3]):)([0-5]?\d):)?([0-5]?\d)$")

    def file_name_validator(self, file_lookup, length):
        if len(file_lookup) != length:
            return False
        return True

    def file_date_validator(self, file_lookup):
        date_string = file_lookup[:10]
        # x = re.match(self.dateValidator, dateString)
        if re.match(self.date_validator, date_string) is not None:
            date_string = date_string.replace(":", "-")
            date_string  = date_string.replace(".", "-")
            date_string  = date_string.replace("/", "-")

            return True, date_string 
        else:
            return False
        
    def reorder_date(self, date_start, date_end):
        if(date_start > date_end):
            temp_date = date_end
            date_end = date_start
            date_start = temp_date
            return date_start, date_end
        else:
            return date_start, date_end


    # def TimeValidator(self, fileLookup):
    def file_time_validator(self,  file_look_up):
        time_string = file_look_up[10:19]
        if re.match(self.time_validator, time_string) is not None:
            return True, time_string[1:9]
        else:
            return False

    def type_validator(self, measurement_type : str):
        if(measurement_type.lower() not in {"SpO2".lower(),"HeartRate".lower(), "temperature".lower()}):
            return False
        else:
            return True


# a = FileInputValidator()
# b = a.FileDateValidator("2017:01:03")
# print(b)

