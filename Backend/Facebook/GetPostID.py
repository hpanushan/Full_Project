from Credentials import pageAccessToken
import GraphAPI

def findSubstringIndex(string, substring):
    # Get the starting index of substring
    index = 0
    if substring in string: 
        c = substring[0]
        for ch in string:
            if ch == c:
                if string[index:index+len(substring)] == substring:
                    return index
            index += 1
    return -1

def getPostID(url):
    # Get the id of fb post
    startingIndex = findSubstringIndex(url, "story_fbid") + len("story_fbid") + 1
    endingIndex = findSubstringIndex(url, "&id=")
    return url[startingIndex:endingIndex]

