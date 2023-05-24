from flask import Blueprint, render_template
# Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later
bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('homepage.html')

@bp.route('/login')
def login():
    return render_template('login.html')
# This route uses a parameter. In the URL, <id> represents the parameter. 
# To capture the value, we include it as a function parameter—specifically, single(id)
@bp.route('/post/<id>')
def single(id):
  return render_template('single-post.html')