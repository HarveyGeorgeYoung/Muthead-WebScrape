from bs4 import BeautifulSoup
import requests
import csv
import re
import math
import csv
import requests 


def menu():
    print("Welcome to Harvey's MUTHEAD Scraper!\nPlease select an option:\n1. Best training/coin rating and price.\n2. Player price search.\n3. Set calculator.")
    userMenuChoice = input()

    if (userMenuChoice == "1"): print("Your choice was 1")
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

    for i in range(numberOfPages + 1):      # Number of pages plus one 

        playerSearchSource = "https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page={}&summary_price__gte=1".format(i)
        playerSearchRequest = requests.get(playerSearchSource).text
        playerSearchSoup = BeautifulSoup(playerSearchRequest, 'lxml')

        for a in playerSearchSoup.find_all('a', href=True, class_="player-listing__link"):

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

            print(playerName + " - " + playerDetails + " - " + str(playerPrice))

def main():
    menu()

if __name__ == "__main__":
    main()
