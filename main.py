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

    if (userMenuChoice == "1"): trainingCost()
    if (userMenuChoice == "2"): playerSearch()
    if (userMenuChoice == "3"): print("Your choice was 3")

def playerSearch():

    print("First name search: ")
    userFirstName = input()
    print("Second name search: (Leave blank if none)")
    userSecondName = input()

    pageSearchSource = "https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page=1&summary_price__gte=1"
    pageSearchRequest = requests.get(pageSearchSource).text
    pageSearchSoup = BeautifulSoup(pageSearchRequest, 'lxml')
    numberOfPages = pageSearchSoup.find('ul', class_="pagination").text
    numberOfPages = numberOfPages.replace(" ", "")
    numberOfPages = numberOfPages.replace("of", "")
    numberOfPages = numberOfPages[10:]
    numberOfPages = int(numberOfPages)

    print(str(numberOfPages) + " number of pages")
    print(tabulate([['','','','']],headers=['Name','Details','Rating','Price'], tablefmt='orgtbl'))
    for i in range(numberOfPages + 1):      # Number of pages plus one 

        playerSearchSource = "https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page={}&summary_price__gte=1".format(i)
        playerSearchRequest = requests.get(playerSearchSource).text
        playerSearchSoup = BeautifulSoup(playerSearchRequest, 'lxml')

        for a in playerSearchSoup.find_all('a', href=True, class_="player-listing__link"):

            playerRating = a.find('div', class_="list-info-player__i")
            playerRating = playerRating.span.text
            playerRating = playerRating.replace("  ", "")
            playerRating = playerRating.replace("\n", "")

            playerName = a.find('div', class_="list-info-player__player-name")
            playerName = playerName.text
            playerName = playerName.replace("  ", "")
            playerName = playerName.replace("\n", "")

            playerDetails = a.find('div', class_="list-info-player__player-info")
            playerDetails = playerDetails.text
            playerDetails = playerDetails.replace("  ", "")
            playerDetails = playerDetails.replace("\n", "")

            playerPrice = a.find('div', class_="player-listing__price-value")
            playerPrice = playerPrice.text
            playerPrice = playerPrice.replace("K", "")
            playerPrice = float(playerPrice)
            playerPrice = playerPrice * 1000
            playerPrice = int(playerPrice)

            f = open('test.txt', 'w')
            f.write(playerName + playerDetails + playerRating + (str(playerPrice)))
            f.close()
            print(tabulate([[playerName,playerDetails,playerRating,str(playerPrice)]],headers=['Name','Details','Rating','Price'], tablefmt='orgtbl'))

def trainingPrice(ovr):
    ratingValueRequest = requests.get('https://www.muthead.com/21/players/?overall__gte=' + str(ovr) + '&overall__lte=' + str(ovr) + '&quicksell_currency=Training&show_training_ratio=true&summary_price__gte=500&sort_by=training_ratio&tier__in=1%2C2%2C3%2C4').text
    ratingValueSoup = BeautifulSoup(ratingValueRequest, 'lxml')
    ratingPrice = ratingValueSoup.find("div", class_="player-listing__price-value").text
    priceRaw = ratingPrice.replace("K", "")
    ratingPrice = float(priceRaw) * 1000
    ratingPrice = round(ratingPrice)
    trainingCostValue = ratingPrice/qsCheck(ovr)
    trainingCostValue = round(trainingCostValue, 2)
    print("[Rated: " + str(ovr) + "]" + "[Buying at: " + str(ratingPrice) + "]" + "[C/T: " + str(trainingCostValue) + "]")

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
    return qsValue

def trainingCost():
    for i in range(80,97):
        trainingPrice(i)

def main():
    menu()

if __name__ == "__main__":
    main()
