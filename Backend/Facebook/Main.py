from datetime import date
from GraphAPI import GraphAPI
from StoreClickhouse import storeClickhouse
from CreateTableName import createTableName
from GetTimeStampFromDate import getTimeStampFromDate
import Credentials

        
def main():
    obj = GraphAPI(Credentials.pageAccessToken)

    # User input parameters. These can be changed
    url = "https://www.facebook.com/permalink.php?story_fbid=105714230769897&id=102699651071355&__xts__[0]=68.ARAEBnhLZdlUsh2Oi41UniA8QH8PFLzB0I-VGiFuiUSY9rOyHQLbgNtFa3D4Rnleg30mCOo7bJ7hFtmJeYYc7WkJcVN8P3McD7xr3KAhxvPEyXUa0XmHRmKgrz0we0e_qitsqrvOHn0Be1zZNkw14KLQzFm-XBndbD47Z2PFpvAUoC97jFVKdalnUGXk_R93tMdXPGY5h3t5bUpqm4yzAUWqv64p_APawkDV457igEn1qyAt5FOyRN-6dVbCMhKfPFPndXl-tXCXiZQVQdZATL5187hm7fE8CJ-iWuT_oCdjqktHYr0IFA4Oere5BUYQOb15rPYavnhoXF2zu-U&__tn__=-R"
    
    startingDate = "2019-05-01"
    endingDate = "2019-12-31"
    #######

    # Creating database table name
    tableName = createTableName(obj,url,startingDate,endingDate)

    # Storing fetched data into Clickhouse
    storeClickhouse(obj,"10.0.0.30",url,tableName,startingDate,endingDate)

if __name__ == '__main__':
    main()

