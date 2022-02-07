from twarc import Twarc2, expansions
import json
import datetime
from twitter_credential import *

client = Twarc2(bearer_token=bearer_token)


def main():

    start_time = datetime.datetime(2021, 6, 10, 0, 0, 0, 0, datetime.timezone.utc)
    end_time = datetime.datetime(2021, 7, 13, 0, 0, 0, 0, datetime.timezone.utc)

    query = "lang:it (#BLM OR #BLACKLIVESMATTER OR #BLACKLIVESMETTER) (#FIGC OR #EURO2020 OR #EURO2021 OR #ITATUR OR #ITALIATURCHIA OR #ITASWI OR #ITASUI OR #ITALIASVIZZERA OR #ITAGAL OR #ITAWAL OR #ITALIAGALLES OR #ITALIAAUSTRIA OR #ITAAUS OR #ITAAUT OR #BELITA OR #ITALIABELGIO OR #BELGIOITALIA OR #ITABEL OR #ITALIAINGHILTERRA OR #ITAENG OR #ITAING OR #ITASPA OR #ITAESP OR #ITALIASPAGNA OR #ITSCOMINGTOROME) OR #INGINOCCHIARSI lang:it OR #IONONMIINGINOCCHIO lang:it OR #IOMIINGINOCCHIO lang:it"

    file_name = 'data_complete.json'

    # The search_all method call the full-archive search endpoint to get Tweets based on the query, start and end times
    search_results = client.search_all(query=query, start_time=start_time, end_time=end_time, max_results=100)

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The Twitter API v2 returns the Tweet information and the user, media etc. separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        
        with open(file_name, 'a+') as filehandle:
            for tweet in result:
                filehandle.write('%s\n' % json.dumps(tweet))


if __name__ == "__main__":
    main()