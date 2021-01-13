import urllib.request as urllib
import json



def create_news():
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey=7b57dbfa104847e6b72e2a4b28e51401"

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    articles=data["articles"]
    titles=[]
    urlsOfNews=[]
    author =  []
    descriptions=[]
    for i in articles:
        author.append(i['author'])
        titles.append(i["title"])
        urlsOfNews.append(i["url"])
        descriptions.append(i["description"])
    return [author, titles, urlsOfNews, descriptions]




def create_news_business():
    url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=7b57dbfa104847e6b72e2a4b28e51401"

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    articles=data["articles"]
    titles=[]
    urlsOfNews=[]
    author =  []
    descriptions=[]
    for i in articles:
        author.append(i['author'])
        titles.append(i["title"])
        urlsOfNews.append(i["url"])
        descriptions.append(i["description"])
    return [author, titles, urlsOfNews, descriptions]


    
def create_news_entertainment():
    url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=7b57dbfa104847e6b72e2a4b28e51401"

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    articles=data["articles"]
    titles=[]
    urlsOfNews=[]
    author =  []
    descriptions=[]
    for i in articles:
        author.append(i['author'])
        titles.append(i["title"])
        urlsOfNews.append(i["url"])
        descriptions.append(i["description"])
    return [author, titles, urlsOfNews, descriptions]



def create_news_sports():
    url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=7b57dbfa104847e6b72e2a4b28e51401"

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    articles=data["articles"]
    titles=[]
    urlsOfNews=[]
    author =  []
    descriptions=[]
    for i in articles:
        author.append(i['author'])
        titles.append(i["title"])
        urlsOfNews.append(i["url"])
        descriptions.append(i["description"])
    return [author, titles, urlsOfNews, descriptions]


def create_news_health():
    url="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=7b57dbfa104847e6b72e2a4b28e51401"

    response = urllib.urlopen(url)
    data = json.loads(response.read())

    articles=data["articles"]
    titles=[]
    urlsOfNews=[]
    author =  []
    descriptions=[]
    for i in articles:
        author.append(i['author'])
        titles.append(i["title"])
        urlsOfNews.append(i["url"])
        descriptions.append(i["description"])
    return [author, titles, urlsOfNews, descriptions]