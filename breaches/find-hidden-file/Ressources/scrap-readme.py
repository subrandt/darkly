from bs4 import BeautifulSoup
import requests
import os

URL = os.environ.get('URL_DARKLY')

def deepInFile(listOfLink, url):
    for a in listOfLink:
        element = a.get('href')
        if element == 'README':
            req = requests.get(url + 'README')
            i = len(req.content)
            if i > 34:
                print(url)
                print(req.content)
                return(0)
        if element != '../':
            path = url + str(element) 
            req = requests.get(path)
            page = BeautifulSoup(req.content, features="html.parser")
            deepInFile(page.find_all('a'), path)


def main():
    try:
        URL_BASE = "http://" + URL + "/.hidden/"
        print(URL_BASE)
        req = requests.get(URL_BASE)

        page = BeautifulSoup(req.content, features="html.parser")

        listOfLink = page.find_all('a')
        deepInFile(listOfLink, URL_BASE)
    except Exception as e:
        print(f"Error: {e}")        


if __name__ =="__main__":
    main()