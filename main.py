### Importing libraries ###
from bs4 import BeautifulSoup
import grequests
import requests
import time
import discord
import numpy as np


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$price'):
        priceArray = []
        priceOrderArray = []

        start_time = time.time()
        await message.channel.send("Please wait...")
        reqs = (grequests.get(link) for link in trainingLinks)
        resp=grequests.imap(reqs, grequests.Pool(20))

        for r in resp:
            soup = BeautifulSoup(r.text, 'lxml')
            ovr = textCleaner(soup.find("div", class_="list-info-player__ovr").span.text)
            ratingPrice = round(priceCleaner(soup.find("div", class_="player-listing__price-value").text))
            trainingCostValueW = ratingPrice/qsCheck(float(ovr))
            trainingCostValue = round(trainingCostValueW, 2)
            priceOrderArray.append(str(trainingCostValueW))
            priceArray.append(("[Rated: " + str(ovr) + "]" + "[Buying at: " + str(ratingPrice) + "]" + "[C/T: " + str(trainingCostValue) + "]"))

        CheapestPriceIndex = priceOrderArray.index(min(priceOrderArray))

        await message.channel.send("....Here you are: ")
        await message.channel.send("\n".join(priceArray))
        await message.channel.send("The cheapest option is this: \n")
        await message.channel.send(priceArray[(20 - (priceOrderArray.index(min(priceOrderArray))))])
        
        totalTime = time.time() - start_time
        await message.channel.send("--- %s seconds ---" % (round(totalTime,2)))

        
def discordTest():
    client.run('ODA5MzA4MDY5OTU5Njk2Mzg0.YCTM4A.Keq3d0AvETbZH8_qOdfwtkfhxSM')

def menu():
    print("---------------------------------------")
    print("Welcome to Harvey's MUTHEAD Scraper!\nPlease select an option:\n1. Best training/coin rating and price.\n2. Player price search.\n3. Set calculator.\n4. Discord Bot")
    print("---------------------------------------")
    userMenuChoice = input()

    if (userMenuChoice == "1"):
        trainingCost()
        menu()
    if (userMenuChoice == "2"): 
        playerSearch()
        menu()
    if (userMenuChoice == "3"): 
        print("---------------------------------------------------")
        print("Welcome to the set management in Harvey's software.\nPlease select an option: \n1. Input new set.\n2. View created sets.\n3. Delete a set\n4. Back to menu.")
        print("---------------------------------------------------")
        usersetCreateChoice = input()
        if usersetCreateChoice == "1":
            setCreate()
            pass
        if usersetCreateChoice == "2":
            pass
        if usersetCreateChoice == "3":
            pass
        if usersetCreateChoice == "4":
            menu()
        else:
            menu()
    if (userMenuChoice == "4"): discordTest()
    else:
        print("Please choose a valid option!")
        menu()
### Starting the timer ###




def playerSearch():
    
    print("First name search: ")
    userFirstName = input()
    print("Second name search: (Leave blank if none)")
    userSecondName = input()

    pageSearch = autoBS("https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page=1&summary_price__gte=1")
    numberOfPages = pageTxtCleaner(pageSearch.find('ul', class_="pagination").text)
    print(str(numberOfPages) + " number of pages")

    for i in range(numberOfPages + 1):

        playerSearch = autoBS("https://www.muthead.com/21/players/?name__icontains=" + userFirstName + "%20"+ userSecondName + "&page={}&summary_price__gte=1".format(i))

        for a in playerSearch.find_all('a', href=True, class_="player-listing__link"):
            
            playerRating = textCleaner(a.find('div', class_="list-info-player__ovr").span.text)
            playerName = textCleaner(a.find('div', class_="list-info-player__player-name").text)
            playerDetails = textCleaner(a.find('div', class_="list-info-player__player-info").text)
            playerPrice = priceCleaner(a.find('div', class_="player-listing__price-value").text)

            print(playerRating,playerName,playerDetails,playerPrice)

def setCreate():
    setTotalPlayers = get("how many players are needed in the set: ")
    numberOfPlayers=setTotalPlayers
    for i in (float(setTotalPlayers) + 1):
        setR = "C:/Users/harve/Documents/GITHUB/Muthead-WebScrape/Sets/"
        completeName = os.path.join(setR, get("What would you like to call this set: ") + ".txt")
        ratingMin = get("What is the minimum rating: ")
        ratingMax = get("What is the maximum rating: ")
        program = programCheck(get("What program is the card from: "))
        position = get("What position: ")
        team = get("What team do they play for: ")
        numberOfPlayers = get("How many of this type: ")
        setTotalPlayers = float(setTotalPlayers) - float(numberOfPlayers)


    f = open(completeName, "w")
    f.write(ratingMin + "\n" + ratingMax + "\n" + program + "\n" + position + "\n" + team)
    f.close()

def programCheck(program):
    if program == "AllRookie": program = "197"
    if program == "AutumnAces": program = "177"
    if program == "AutumnAllStars": program = "179"
    if program == "AutumnBlast": program = "178"
    if program == "BlackHistoryMonth": program = "195"
    if program == "Blitz": program = "181"
    if program == "CampusHeroes": program = "182"
    if program == "CoreBronze": program = "155"
    if program == "CoreElite": program = "152"
    if program == "CoreGold": program = "153"
    if program == "CoreRookie": program = "154"
    if program == "CoreSilver": program = "156"
    if program == "DerwinvstheWorld": program = "172"
    if program == "Flashbacks": program = "173"
    if program == "GhostsofMadden": program = "186"
    if program == "Heavyweights": program = "167"
    if program == "Legends": program = "164"
    if program == "LevelMaster": program = "159"
    if program == "LimitedEdition": program = "168"
    if program == "M21Reward": program = "147"
    if program == "M21Tribute": program = "189"
    if program == "MaddenClubChampionship": program = "188"
    if program == "Master": program = "148"
    if program == "MCSDeluxeEdition": program = "158"
    if program == "MostFeared": program = "176"
    if program == "MUTHeroes": program = "198"
    if program == "MUTMaster": program = "160"
    if program == "NFLEpics": program = "149"
    if program == "NFLHonors": program = "194"
    if program == "NFLPlayoffs": program = "187"
    if program == "OOP": program = "185"
    if program == "PizzaHut": program = "180"
    if program == "PowerUp": program = "151"
    if program == "ProBowl": program = "190"
    if program == "RisingStars": program = "174"
    if program == "Rivalz": program = "146"
    if program == "RookiePremiere": program = "163"
    if program == "SeriesRedux": program = "170"
    if program == "SnowBeasts": program = "183"
    if program == "SuperBowlPast": program = "192"
    if program == "SuperBowlPresent": program = "193"
    if program == "SuperstarMVPs": program = "162"
    if program == "TeamBuilders": program = "150"
    if program == "TeamCaptains": program = "143"
    if program == "TeamDiamonds": program = "161"
    if program == "TeamoftheWeek": program = "166"
    if program == "TeamoftheYear": program = "191"
    if program == "TeamStandouts": program = "175"
    if program == "The50": program = "171"
    if program == "UltimateKickoff": program = "165"
    if program == "UltimateLegends": program = "196"
    if program == "Veterans": program = "169"
    if program == "ZeroChill": program = "184"
    return program

def get(question):
    print(question)
    question = input()
    return question

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
    if ovr == 80: qsValue = 160
    if ovr == 81: qsValue = 230
    if ovr == 82: qsValue = 320
    if ovr == 83: qsValue = 450
    if ovr == 84: qsValue = 640
    if ovr == 85: qsValue = 900
    if ovr == 86: qsValue = 1300
    if ovr == 87: qsValue = 1800
    if ovr == 88: qsValue = 2500
    if ovr == 89: qsValue = 3600
    if ovr == 90: qsValue = 5000
    if ovr == 91: qsValue = 7100
    if ovr == 92: qsValue = 10000
    if ovr == 93: qsValue = 14100
    if ovr == 94: qsValue = 19900
    if ovr == 95: qsValue = 25500
    if ovr == 96: qsValue = 36000
    if ovr == 97: qsValue = 50700
    if ovr == 98: qsValue = 71500
    if ovr == 99: qsValue = 100000
    return qsValue

def trainingCost():
    start_time = time.time()

    priceOrderArray = []
    priceArray = []

    reqs = (grequests.get(link) for link in trainingLinks)
    resp=grequests.imap(reqs, grequests.Pool(20))

    for r in resp:
        soup = BeautifulSoup(r.text, 'lxml')
        ovr = textCleaner(soup.find("div", class_="list-info-player__ovr").span.text)
        ratingPrice = round(priceCleaner(soup.find("div", class_="player-listing__price-value").text))
        trainingCostValue = ratingPrice/qsCheck(float(ovr))
        trainingCostValue = round(trainingCostValue, 2)
        priceOrderArray.append(str(trainingCostValue))
        priceArray.append(("[Rated: " + str(ovr) + "]" + "[Buying at: " + str(ratingPrice) + "]" + "[C/T: " + str(trainingCostValue) + "]"))

    CheapestPriceIndex = priceOrderArray.index(min(priceOrderArray))

    print("....Here you are: ")
    print("\n".join(priceArray))
    print("The cheapest option is this: \n")
    print(priceArray[(20 - (priceOrderArray.index(min(priceOrderArray))))])
    totalTime = time.time() - start_time
    print("--- %s seconds ---" % (round(totalTime,2)))

trainingLinks = [
    "https://www.muthead.com/21/players/?overall__gte=80&overall__lte=80&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=81&overall__lte=81&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=82&overall__lte=82&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=83&overall__lte=83&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=84&overall__lte=84&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=85&overall__lte=85&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=86&overall__lte=86&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=87&overall__lte=87&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=88&overall__lte=88&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=89&overall__lte=89&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=90&overall__lte=90&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=91&overall__lte=91&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=92&overall__lte=92&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=93&overall__lte=93&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=94&overall__lte=94&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=95&overall__lte=95&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=96&overall__lte=96&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=97&overall__lte=97&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=98&overall__lte=98&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    "https://www.muthead.com/21/players/?overall__gte=99&overall__lte=99&price_platform=1&sort_by=summary_price&summary_price__gte=300",
    ]

def main():
    
    menu()

if __name__ == "__main__":
    main()
