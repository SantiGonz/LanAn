from snscrape.modules import twitter
import json
from datetime import datetime
import pytz

usuarios = ['AlejandraDMV']
start_date = datetime(2023, 5, 25).replace(tzinfo=pytz.UTC)
end_date = datetime(2023, 6, 4, 23, 59, 59).replace(tzinfo=pytz.UTC)

def scrape_user(user):
    return twitter.TwitterUserScraper(user)

for usuario in usuarios:
    output_file = usuario.replace(" ", "_") + "_id.txt"
    with open(output_file, 'w') as f:
        print(usuario)
        scraper = scrape_user(usuario)
        i=0
        for tweet in scraper.get_items():
            tweet_date = tweet.date
            if start_date <= tweet_date < end_date:
                tweet_json = json.loads(tweet.json())
                print(f"\nScraped tweet: {tweet_json['id']}")
                f.write(tweet.json())
                f.write('\n')
                f.flush()
                i+=1
            elif  tweet_date < end_date :
                print("Fueron {} twits".format( i))
                break

