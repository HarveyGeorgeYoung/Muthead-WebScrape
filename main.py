from bs4 import BeautifulSoup
import requests
import csv
import re
import math
import csv
import requests 
from tabulate import tabulate

def menu():
    print("Welcome to Harvey's MUTHEAD Scraper!\nPlease select an option:\n1. Best training/coin rating and price.\n2. Player price search.\n3. Set calculator.")
    userMenuChoice = input()

    if (userMenuChoice == "1"):
        for i in range(80,100):
            trainingPrice(i)
    if (userMenuChoice == "2"): playerSearch()
    if (userMenuChoice == "3"): print("Your choice was 3")

def playerSearch():

    print("First name search: ")
    userFirstName = input()
    print("Second name search: (Leave blank if none)")
    userSecondName = input()

    pageSearch = autoBS("https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page=1&summary_price__gte=1")
    numberOfPages = pageTxtCleaner(pageSearch.find('ul', class_="pagination").text)
    print(str(numberOfPages) + " number of pages")

    for i in range(numberOfPages + 1):      # Number of pages plus one 

        playerSearch = autoBS("https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page={}&summary_price__gte=1".format(i))

        for a in playerSearch.find_all('a', href=True, class_="player-listing__link"):
            
            playerRating = textCleaner(a.find('div', class_="list-info-player__ovr").span.text)
            playerName = textCleaner(a.find('div', class_="list-info-player__player-name").text)
            playerDetails = textCleaner(a.find('div', class_="list-info-player__player-info").text)
            playerPrice = priceCleaner(a.find('div', class_="player-listing__price-value").text)

            print(playerRating,playerName,playerDetails,playerPrice)

def trainingPrice(ovr):
    ratingValue = autoBS('https://www.muthead.com/21/players/?overall__gte=' + str(ovr) + '&overall__lte=' + str(ovr) + '&quicksell_currency=Training&show_training_ratio=true&summary_price__gte=500&sort_by=training_ratio&tier__in=1%2C2%2C3%2C4')
    ratingPrice = round(priceCleaner(ratingValue.find("div", class_="player-listing__price-value").text))
    trainingCostValue = ratingPrice/qsCheck(ovr)
    trainingCostValue = round(trainingCostValue, 2)
    print("[Rated: " + str(ovr) + "]" + "[Buying at: " + str(ratingPrice) + "]" + "[C/T: " + str(trainingCostValue) + "]")

def autoBS(src):
    rq = requests.get(src).text
    sp = BeautifulSoup(rq, 'lxml')
    return sp
def pageTxtCleaner(txt):
    txt = txt.replace(" ", "")
    txt = txt.replace("of", "")
    txt = txt[10:]
    txt = int(txt)
    return txt

def textCleaner(txt):
    txt = txt.replace("  ", "")
    txt = txt.replace("\n", "")       
    return txt

def priceCleaner(value):
    if "K" in value:
        value = value.replace("K", "")
        value = float(value) * 1000
        value = round(value)
    return value

def qsCheck(ovr):
    if ovr == 80:
        qsValue = 160
    if ovr == 81:
        qsValue = 230
    if ovr == 82:
        qsValue = 320
    if ovr == 83:
        qsValue = 450
    if ovr == 84:
        qsValue = 640
    if ovr == 85:
        qsValue = 900
    if ovr == 86:
        qsValue = 1300
    if ovr == 87:
        qsValue = 1800
    if ovr == 88:
        qsValue = 2500
    if ovr == 89:
        qsValue = 3600
    if ovr == 90:
        qsValue = 5000
    if ovr == 91:
        qsValue = 7100
    if ovr == 92:
        qsValue = 10000
    if ovr == 93:
        qsValue = 14100
    if ovr == 94:
        qsValue = 19900
    if ovr == 95:
        qsValue = 25500
    if ovr == 96:
        qsValue = 36000
    if ovr == 97:
        qsValue = 50700
    if ovr == 98:
        qsValue = 71500
    if ovr == 99:
        qsValue = 100000
    return qsValue

def main():
    menu()

if __name__ == "__main__":
    main()
