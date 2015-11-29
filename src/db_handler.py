import sqlite3
import datetime
import re


def create_master_database():
	conn = sqlite3.connect('db/database.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE sources
             (date text, source text unique, name unique)''')
	conn.commit()
	conn.close()		

def get_rss_sources():
	print "db Getting sources"
	conn = sqlite3.connect('db/database.db')
	c = conn.cursor()
	c.execute('SELECT * FROM sources')
	sources = c.fetchall()
	conn.close()
	return sources

def delete_rss_source(rss):
	conn = sqlite3.connect('db/database.db')
	c = conn.cursor()
	c.execute("""DELETE FROM sources WHERE source = ?""", rss)
	conn.commit()
	c.close()


def insert_rss_source(rss, name):
	conn = sqlite3.connect('db/database.db')
	c = conn.cursor()
	c.execute("""INSERT OR IGNORE INTO sources VALUES (?, ?, ?)""", (datetime.datetime.now().date(), rss, name ))
	#sql = """CREATE TABLE {} (date text, link text unique);""".format(name)
	#c.execute(sql)
	conn.commit()
	conn.close()
	return "added a source to the database"

#create_master_database()
insert_rss_source('http://feeds.reuters.com/reuters/oddlyEnoughNews', 'News 8')
#delete_rss_source('http://www.reddit.com/r/python/.rss')
#print get_rss_sources()