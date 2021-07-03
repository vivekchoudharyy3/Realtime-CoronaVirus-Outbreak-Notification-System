from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r'C:\Users\91747\Desktop\Covid Notification\covid_icon.ico',
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text
if __name__ == "__main__":
    while True:
        notifyMe("Vivek", "Let's stop the spread of virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')
        print(myHtmlData)
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        print(soup.prettify().encode("utf-8")
        )
        myDataStr = ""
        for tr in soup.find_all('tbody')[1].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Madhya Pradesh', 'Maharastra', 'Delhi']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states: 
                nTitle = 'Cases of Covid-19'
                nText = f"State {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured :  {dataList[4]}\nDeaths :  {dataList[5]}"
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)