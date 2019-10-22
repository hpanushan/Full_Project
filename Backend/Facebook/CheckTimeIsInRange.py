from datetimerange import DateTimeRange
from GetTimeStampFromDate import getTimeStampFromDate

def checkTimeIsInRange(startingTime,endingTime,time):   
    # Time range creation
    timeRange = DateTimeRange(startingTime,endingTime)

    result = time in timeRange

    return result


#print(checkTimeIsInRange("2019-03-22T10:10:00+0900","Thu Aug 22 05:41:23 +0000 2019","2019-10-22T10:10:00+0900"))




