from flask import render_template, request, Blueprint
from flaskblog.models import Post, User
from flask_login import current_user

main = Blueprint('main', __name__)


@main.route("/home")
def start():
    return render_template('main.html')

@main.route("/")
def home():
    if not current_user.is_authenticated:
        flash('You must be logged in', 'warning')
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
    return render_template('news.html', title='News')