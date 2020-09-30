from bs4 import BeautifulSoup as bs
import requests

def kickass_search(query):

    results=[]

    dataDict={}

    a=[]

    base_url="https://kickass.unblockit.top/search.php?q="

    url=base_url+query+'/'

    print("Searching......")

    source=requests.get(url).text

    soup=bs(source,'lxml')

    name=soup.find_all('a', class_="cellMainLink")

    magnet=soup.find_all('a', title="Torrent magnet link")

    for m in magnet:
            a.append(m['href'])

    i=1
    for r in name:
        movie = str(i) + " " + r.text

        magnet_link=(a[i-1])

        movieData = {
            "movie":movie,
            "Magnet":magnet_link
         }

        results.append(movieData)

        i = i+1

    return(results)

