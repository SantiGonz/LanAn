from snscrape.modules import twitter
import json
from datetime import datetime
import pytz
#Sacar los IDS de todas las respuestas de un usuario en un rango de fechas
usuarios = ['AlejandraDMV', 'delfinagomeza', 'RicardoMeb', 'leninperezr', 'aguadiana','manolojim']

dias=[[4, 3], [6, 4], [6, 5]]


for dia in dias: 
    start_date = datetime(2023, dia[0], dia[1], 0, 0, 0).replace(tzinfo=pytz.timezone('Etc/GMT+6'))

    end_date = datetime(2023, dia[0], dia[1], 23, 59, 59).replace(tzinfo=pytz.timezone('Etc/GMT+6'))

    for usuario in usuarios:
        output_file = usuario+str(dia[0])+"-"+str(dia[1])+"IDS.txt"
        with open(output_file, 'w') as f:
            print(usuario)
            scraper = twitter.TwitterUserScraper(usuario)
            i=0
            for twit in scraper.get_items():
                twit_date = twit.date
                if start_date <= twit_date < end_date:
                    twit_json = json.loads(twit.json())
                    print(f"\n{twit_json['id']}")
                    f.write(str(twit_json['id']))
                    f.write('\n')
                    f.flush()
                    i+=1
                elif twit_date < end_date :
                    # print(f"Fueron {i} twits")
                    break
