import re

class FileInputValidator():
    dateValidator = re.compile("^([0-9]{4}[-/]?((0[13-9]|1[012])[-/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[-/]?31|02[-/]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048]|0[0-9]|1[0-6])00)[-/]?02[-/]?29)$")
    timeValidator = re.compile("^(T|t)(?:(?:([01]?\d|2[0-3]):)([0-5]?\d):)?([0-5]?\d)$")

    def FileNameValidator(self, fileLookup, length):
        print(len(fileLookup))
        if len(fileLookup) != length:
            return False
        return True

    def FileDateValidator(self, fileLookup):
        dateString = fileLookup[:10]
        print(dateString)
        # x = re.match(self.dateValidator, dateString)
        print(re.match(self.dateValidator, dateString))
        if re.match(self.dateValidator, dateString) is not None:
            return True, dateString
        else:
            return False

    # def TimeValidator(self, fileLookup):
    def FileTimeValidator(self,  fileLookup):
        timeString = fileLookup[10:19]
        if re.match(self.timeValidator, timeString) is not None:
            return True, timeString[1:9]
        else:
            return False



# a = FileInputValidator()
# b = a.FileDateValidator("2017-01-03T10:04:45")
# print(b)

