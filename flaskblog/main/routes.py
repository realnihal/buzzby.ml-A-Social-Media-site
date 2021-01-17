from flask import render_template, request, Blueprint
from flaskblog.models import Post, User
from flask_login import current_user
from flaskblog.news import create_news, create_news_business, create_news_entertainment, create_news_sports, create_news_health, create_news_science, create_news_technology
from flaskblog.weather import weather_data
from flaskblog.main.forms import WeatherForm

main = Blueprint('main', __name__)


@main.route("/")
def start():
    return render_template('main.html')

@main.route("/home")
def home():
    if not current_user.is_authenticated:
        return start()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    user = User.query.filter_by(email='puramnihal@gmail.com').first()
    return render_template('about.html', title='About', user=user)


@main.route("/news")
def news():
    article = create_news()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='Top Headlines', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/business")
def news_business():
    article = create_news_business()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='Business Headlines', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)

@main.route("/news/entertainment")
def news_entertainment():
    article = create_news_entertainment()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='Entertainment Headlines', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/sports")
def news_sports():
    article = create_news_sports()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='Sports Headlines', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/health")
def news_health():
    article = create_news_health()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='Health Headlines', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/science")
def news_science():
    article = create_news_science()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='Science Headlines', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)



@main.route("/news/technology")
def news_technology():
    article = create_news_technology()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='Technology Headlines', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)



@main.route("/weather",methods=['GET', 'POST'])
def weather():
    form = WeatherForm()
    if form.validate_on_submit():
        city_name = form.city.data
        weather_list = weather_data(city_name)
        temperature =  weather_list[1]
        humidity =  weather_list[2]
        pressure =  weather_list[3]
        report =  weather_list[4]
        return render_template('weather.html',title= 'weather',form=form, city_name=city_name,temperature=temperature,humidity=humidity,pressure=pressure,report=report)
    
    weather_list = weather_data()
    city_name =  weather_list[0]
    temperature =  weather_list[1]
    humidity =  weather_list[2]
    pressure =  weather_list[3]
    report =  weather_list[4]
    return render_template('weather.html',title= 'weather',form=form, city_name=city_name,temperature=temperature,humidity=humidity,pressure=pressure,report=report)
