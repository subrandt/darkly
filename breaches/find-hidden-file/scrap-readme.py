from bs4 import BeautifulSoup
import requests

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
    URL_BASE = "http://10.13.248.97/.hidden/"
    req = requests.get(URL_BASE)

    page = BeautifulSoup(req.content, features="html.parser")

    listOfLink = page.find_all('a')
    deepInFile(listOfLink, URL_BASE)


if __name__ =="__main__":
    main()