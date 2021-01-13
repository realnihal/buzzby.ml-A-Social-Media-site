import urllib.request as urllib
import json



def create_news(source):

    if source == 'plain':
        url="http://newsapi.org/v2/top-headlines?country=in&sports&apiKey=7b57dbfa104847e6b72e2a4b28e51401"
    elif source == 'sports':
        url="http://newsapi.org/v2/top-headlines?country=in&sports&apiKey=7b57dbfa104847e6b72e2a4b28e51401"
    elif source == 'business':
        url="http://newsapi.org/v2/top-headlines?country=in&business&apiKey=7b57dbfa104847e6b72e2a4b28e51401"
    elif source == 'entertainment':
        url="http://newsapi.org/v2/top-headlines?country=in&entertainment&apiKey=7b57dbfa104847e6b72e2a4b28e51401"
    elif source == 'health':
        url="http://newsapi.org/v2/top-headlines?country=in&health&apiKey=7b57dbfa104847e6b72e2a4b28e51401"
    elif source == 'science':
        url="http://newsapi.org/v2/top-headlines?country=in&science&apiKey=7b57dbfa104847e6b72e2a4b28e51401"
    elif source == 'technology':
        url="http://newsapi.org/v2/top-headlines?country=in&technology&apiKey=7b57dbfa104847e6b72e2a4b28e51401"
    else:
        url="http://newsapi.org/v2/top-headlines?country=in&sports&apiKey=7b57dbfa104847e6b72e2a4b28e51401"

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
    