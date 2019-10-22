from GoogleAPI import gcpNLP

def addSentimentProperties(listOfTuples):
    # Add sentiment score and sentiment magnitude into the tuples

    output = []                                             # Output list
    for i in listOfTuples:
        sentiment = gcpNLP(i[-1])
        sentimentScore = sentiment.score
        sentimentMagnitude = sentiment.magnitude

        i = i + (sentimentScore,sentimentMagnitude)         # Add sentiment score and magnitude into the tuple
        output.append(i)

    return output

#var = [('Fri Sep 06 07:40:45 +0000 2019', '1151806655744450562', 'croatengi', '1169878084759089152', '@wavenlp who knows'), ('Fri Sep 06 07:40:45 +0000 2019', '1151806655744450512', 'croatengi1', '1169878084759089152', '@wavenlp who knows'), ('Fri Sep 06 07:40:45 +0000 2019', '1151806655744450123', 'dexter', '1169878084759089152', '@wavenlp damn it')]

#print(addSentimentProperties(var))

