from snscrape.modules import twitter
import json
from datetime import datetime
import pytz
#Sacar los IDS de todas las respuestas de un usuario en un rango de fechas
usuarios = ['AlejandraDMV', 'delfinagomeza', 'RicardoMeb', 'leninperezr', 'aguadiana','manolojim']
start_date = datetime(2023, 5, 25).replace(tzinfo=pytz.UTC)
end_date = datetime(2023, 6, 4, 23, 59, 59).replace(tzinfo=pytz.UTC)

for usuario in usuarios:
    output_file = usuario+"IDS.txt"
    with open(output_file, 'w') as f:
        print(usuario)
        scraper = twitter.TwitterUserScraper(usurio)
        i=0
        for tweet in scraper.get_items():
            tweet_date = tweet.date
            if start_date <= tweet_date < end_date:
                tweet_json = json.loads(tweet.json())
                print(f"\n{tweet_json['id']}")
                f.write(tweet_json['id'])
                f.write('\n')
                f.flush()
                i+=1
            elif tweet_date < end_date :
                # print(f"Fueron {i} twits")
                break

