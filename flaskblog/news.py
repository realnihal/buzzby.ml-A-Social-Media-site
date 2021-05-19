import urllib.request as urllib
import json



def create_news():
    url="http://newsapi.org/v2/top-headlines?country=in&apiKey={YOUR API KEY}"

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
    url="http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={YOUR API KEY}"

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
    url="http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey={YOUR API KEY}"

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
    url="http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={YOUR API KEY}"

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
    url="http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey={YOUR API KEY}"

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


def create_news_science():
    url="http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey={YOUR API KEY}"

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


def create_news_technology():
    url="http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey={YOUR API KEY}"

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
