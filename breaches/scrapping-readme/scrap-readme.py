from bs4 import BeautifulSoup
import threading
import requests
import time

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
    URL_BASE = "http://10.13.248.133/.hidden/"
    # start = time.time()
    req = requests.get('http://10.13.248.133/.hidden/')

    page = BeautifulSoup(req.content, features="html.parser")

    listOfLink = page.find_all('a')

    taille = len(listOfLink)
    taille_partie = taille // 4

    listes_divisees = []

    for i in range(4):
        debut = i * taille_partie
        fin = (i + 1) * taille_partie if i < 3 else taille
        listes_divisees.append(listOfLink[debut:fin])

    threads = []
    for i in range(4):
        t = threading.Thread(target=deepInFile, args=(listes_divisees[i], URL_BASE))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    # end = time.time()
    # print(f'Time = {end - start}')

if __name__ =="__main__":
    main()