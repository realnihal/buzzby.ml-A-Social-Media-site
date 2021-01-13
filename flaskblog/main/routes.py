from flask import render_template, request, Blueprint
from flaskblog.models import Post, User
from flask_login import current_user
from flaskblog.news import create_news, create_news_business, create_news_entertainment, create_news_sports, create_news_health, create_news_science, create_news_technology


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
    if not current_user.is_authenticated:
    return start()
    article = create_news()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='News', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/business")
def news_business():
    if not current_user.is_authenticated:
    return start()
    article = create_news_business()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='News', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)

@main.route("/news/entertainment")
def news_entertainment():
    if not current_user.is_authenticated:
    return start()
    article = create_news_entertainment()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='News', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/sports")
def news_sports():
    if not current_user.is_authenticated:
    return start()
    article = create_news_sports()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='News', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/health")
def news_health():
    if not current_user.is_authenticated:
    return start()
    article = create_news_health()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='News', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)


@main.route("/news/science")
def news_science():
    if not current_user.is_authenticated:
    return start()
    article = create_news_science()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='News', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)



@main.route("/news/technology")
def news_technology():
    if not current_user.is_authenticated:
    return start()
    article = create_news_technology()
    author = article[0]
    titles = article[1]
    urlsOfNews = article[2]
    descriptions = article[3]
    num = len(titles)
    return render_template('news.html', title='News', author=author,titles=titles,urls=urlsOfNews,descriptions=descriptions,length=num)