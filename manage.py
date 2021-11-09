from app import create_app
from flask_script import Manager, Server
from flask import render_template
from app.requests import get_sources

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@app.route('/')
def index():
    business_source = get_sources()
    
    # print(business_source)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',business_sources = business_source)

@app.route('/articles/<int:article_id>')
def articles(article_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('articles.html',id = article_id)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000', debug=True)