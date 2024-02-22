from bs4 import BeautifulSoup
import requests
import os

#Function to get a hardcoded url or custom url
def getURL():
    while True:
        usrInput = input("Do you have a custom URL: ").upper()
        clear_last_line()
        if usrInput == "yes".upper():
            url = input("Enter your URL: ")
            clear_last_line()
            break
        elif usrInput == "no".upper():
            url = "https://blog.enterprisedna.co/python-write-to-file/" #Enter your custom url here
            break
    return url

#Function to get hardcoded keywords or custom ones
def getKeywords():
    while True:
        usrInput = input("Do you have custom keywords: ").upper()
        clear_last_line()
        if usrInput == "yes".upper():
            keywords = input("Enter your keywords seperated by spaces: ").split()
            clear_last_line()
            break
        elif usrInput == "no".upper():
            keywords = ["software", "binary", "crucial"] #Enter your custom keywords here
            break
    return keywords

#Function to scrape data
def scrape(url, keywords, type):
    try:
        page = requests.get(url)
    except:
        print("------------------------------------------------")
        print("          | Error: Website Invalid |")
        print("------------------------------------------------")
        print()
        exit()

    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        print("          | Connection Established |")
        rawData = soup.find_all(type)
        data = []

        for i in rawData:
            for keyword in keywords:
                if keyword.lower() in i.get_text().lower():
                    data.append(i.get_text())
                    break
                    
    else:
        print("         | Failed to Retrieve Webpage |", page.status_code)
        exit()

    return data

#Function used to clear previous line in the terminal
def clear_last_line():
    # Clear last line based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems
        os.system('tput cuu1 && tput el')

def download(fileName, data):
    file = open(fileName + ".txt", "w")

    for d in data:
        file.write(d + "\n\n")

    file.close()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print("------------------------------------------------")
    print("           | Website Scraper v1.0 |")
    print("------------------------------------------------")
    print()

    #Gets url and keywords
    url = getURL()
    keywords = getKeywords()

    #Prints scrapper keywords and URL
    print("------------------------------------------------")
    print("                | Seach Info |")
    print()
    print("URL: " + url)
    print("Keywords: ", keywords)
    print("------------------------------------------------")
    print()

    #Gets all the data requested
    paragraphs = scrape(url, keywords, "p")

    #Displays Paragraphs
    print()
    print("------------------------------------------------")
    print("         | Paragraphs with Keywords |")
    print()
    for paragraph in paragraphs:
        print(paragraph)
        print()
    print("------------------------------------------------")
    print()

    #Gives option to download data
    while True:
        usrInput = input("Do you want to download this data as a txt file?: ")
        clear_last_line()
        if usrInput.upper() == "yes".upper():
            name = input("Enter a file name: ")
            clear_last_line()
            download(name, paragraphs)
            print("            | Download Succesful |")
            break
        elif usrInput.upper() == "no".upper():
            break
    
    print()
    print("               | Program Ended |")
    print()
            
main()

