import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

gites_holidays = []

for x in range(1,59):

   
    url = "https://www.gites.co.uk/search/"

    r = requests.get(url+str(x))
    soup = bs(r.content,'html.parser')

    contents = soup.find_all('div',class_="listing_item clearfix")

    for content in contents:
        try:
            hotel_name = content.find('div',class_="li_header").text
            hotel_price = content.find('div',class_="li_price").text
            hotel_bedrooms = content.find('div',class_="li_meta").text
            hotel_summery = content.find('div',class_="li_summary").text
            hotel_update_date = content.find('div',class_="li_footer").text

            hotel_info = {
                'Hotel Name':hotel_name,
                'Hotel Price':hotel_price,
                'Hotel Bedrooms':hotel_bedrooms,
                'Hotel Summery':hotel_summery,
                'Hotel Update Date':hotel_update_date
            }

            gites_holidays.append(hotel_info)
        except:
            gites_holidays = 'None'
    print('Holidays Found : ',len(gites_holidays))
    time.sleep(2)
        

df = pd.DataFrame(gites_holidays)
print(df.head())
df.to_csv('gites_website_holidays.csv')