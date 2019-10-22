
def getListOfDict(keys, list_of_tuples):
     # This will get a list of tuples and return a list of dictionaries
     list_of_dict = [dict(zip(keys, values)) for values in list_of_tuples]
     return list_of_dict

#var = [('Fri Sep 06 07:40:45 +0000 2019', '1151806655744450562', 'croatengi', '1169878084759089152', '@wavenlp who knows'), ('Fri Sep 06 07:40:45 +0000 2019', '1151806655744450512', 'croatengi1', '1169878084759089152', '@wavenlp who knows'), ('Fri Sep 06 07:40:45 +0000 2019', '1151806655744450123', 'dexter', '1169878084759089152', '@wavenlp damn it')]

#print(getListOfDict(['date_time','user_id','user_name','text_id','text'],var))

