from bs4 import BeautifulSoup
import requests
page_link ='https://russiarunning.com'
# fetch the content from url
response = requests.get(page_link).text
# parse html
soup = BeautifulSoup(response, "lxml")
event=soup.find('div',{'class':"event-info"})
date=event.find('span',{'class':"date"}).text
location=event.find('span',{'class':"location"}).text
name=event.find('a',{'class':"title ellipsis"}).text
distance=event.find('span',{'class':"race-event-item"}).text
#with open ("1.html","w", encoding="utf-8") as file:
#    file.write(response)
print(name, location, date, distance)
#event.find('span',{'class':"date"}).text
