from ClickhouseClient import ClickhouseClient
from GetPostID import getPostID
from CheckTimeIsInRange import checkTimeIsInRange
from CreateTableName import createTableName
from AddSentimentProperties import addSentimentProperties
from GetListOfDict import getListOfDict
from GetTimeStampFromDate import getTimeStampFromDate

def storeClickhouse(GraphAPIObject,ipAddress,url,tableName,startingDate,endingDate):
    # Retrieve page comments and store them in Clickhouse
    pageID = GraphAPIObject.getPageID()                                 # Get the page ID from GraphAPI                                     
    postID = pageID + "_" + getPostID(url)                              # Combine page ID with postID to get correct post ID
    postCommentsList = GraphAPIObject.getPostCommentsList(postID)       # Get list of post comments
  
    # Connect with Clickhouse
    dbObject = ClickhouseClient(ipAddress)

    # Create the table
    dbObject.createTable('facebook',tableName)
    
    # List of tuples
    listOfTuples = []

    for i in postCommentsList:
        # Read each comment one by one
        if (checkTimeIsInRange(getTimeStampFromDate(startingDate),getTimeStampFromDate(endingDate),i['created_time'])==True):
                date_time = i['created_time']
                user_id = int(i['from']['id'])
                user_name = i['from']['name']
                text_id = i['id']
                text = i['message']
                # Tuple
                dataTuple = (date_time,user_id,user_name,text_id,text)
                # Adding created tuple into the list
                listOfTuples.append(dataTuple)
        else: pass

    # Add sentiment properties into the data tuples
    sentimentAddedList = addSentimentProperties(listOfTuples)

    # Convert list of tuples into the list of dictionaries
    listOfDict = getListOfDict(['date_time','user_id','user_name','text_id','text','score','magnitude'],sentimentAddedList)

    # Data insertion into the Clickhouse table
    dbObject.insertData("facebook",tableName,listOfDict)


        


