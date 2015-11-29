# importing flask
from flask import Flask
from flask import request
from flask import render_template

#importing rss handler
import rss_handler as rh

#importing database handler
import db_handler as dh
app = Flask(__name__)


# setting un content for root page
@app.route('/')
def hello_world():
	sources = dh.get_rss_sources()
	feed = rh.get_rss_feed(sources)
	#template = render_template('index.html', Sources=sources)
	return render_template('index.html', Feed=feed)

# RSS sources manage site
@app.route('/manage', methods=['GET', 'POST'])
def display_config():
	print "Managing"
	rss_sources = dh.get_rss_sources()
	rss_sources = enumerate(rss_sources)
	return render_template('manage.html', Rss_sources=rss_sources)

# setting route to import rss to the database
@app.route('/import_rss', methods=['POST'])
def addRss():
	return rh.parse_rss(request.form['rss_source'], request.form['rss_name'])


if __name__ == '__main__':
    app.run(debug=True)