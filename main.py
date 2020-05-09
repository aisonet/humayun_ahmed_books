import urllib.request
from bs4 import BeautifulSoup
import os
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
import requests
bookpath = 'book.list'
booklist = [line1.rstrip('\r\n') for line1 in open(bookpath)]
for book in booklist:
    if book.startswith("http"):
        
        # url = book
        # print(url)
        headers={'User-Agent':user_agent,} 
        request=urllib.request.Request(book,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        data = response.read()
        soup = BeautifulSoup(data, 'html.parser')
        a=soup.select_one("a[href*=pdf]")
        link=a['href']
        command= "wget '"+link+"'"
        print (command)
        try:
            os.system(command)
        except:
            print("failed to download")
