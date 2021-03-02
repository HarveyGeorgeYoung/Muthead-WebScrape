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

    pageSearchSource = requests.get("https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page=1").text
    pageSearchSoup = BeautifulSoup(pageSearchSource, 'lxml')
    numberOfPages = pageSearchSoup.find('ul', class_="pagination").text
    numberOfPages = numberOfPages.replace(" ", "")
    numberOfPages = numberOfPages.replace("of", "")
    numberOfPages = numberOfPages[10:]
    numberOfPages = int(numberOfPages)

    print(str(numberOfPages))

def main():
    menu()

if __name__ == "__main__":
    main()
