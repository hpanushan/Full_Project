from GetPostID import getPostID

def createTableName(GraphAPIObject,url,startingDate,endingDate):
    pageID = GraphAPIObject.getPageID()                                 # Get the page ID from GraphAPI
    postID = pageID + "_" + getPostID(url)                              # Combine page ID with postID to get correct post ID

    # To remove dashes and concatenate all the elements
    newStartingDate = ''.join((startingDate.split('-')))
    newEndingDate = ''.join((endingDate.split('-')))

    tableName = "F_" + postID + "_" + newStartingDate + '_' + newEndingDate

    return tableName

