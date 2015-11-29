import feedparser

'''
    keymap = {'channel': 'feed',
              'items': 'entries',
              'guid': 'id',
              'date': 'updated',
              'date_parsed': 'updated_parsed',
              'description': ['subtitle', 'summary'],
              'url': ['href'],
              'modified': 'updated',
              'modified_parsed': 'updated_parsed',
              'issued': 'published',
              'issued_parsed': 'published_parsed',
              'copyright': 'rights',
              'copyright_detail': 'rights_detail',
              'tagline': 'subtitle',
              'tagline_detail': 'subtitle_detail'}

result['feed']
result['entries']

if _XML_AVAILABLE:
    result['bozo'] = 0
        # save HTTP headers
# save HTTP headers
if hasattr(f, 'info'):
    info = f.info()
    result['etag'] = info.getheader('ETag')

result['modified']
result['href'] 
result['status']
result['debug_message']


# feed
return link['href']
return self[key]

'''
def add_new_rss():
	# add the rss to the database
	pass

def parse_rss(rss_link):
	# parse the rss and get the data from it
	d = feedparser.parse(rss_link)
	return d

def get_rss_feed(feed):
  site_news = list()
  for f in feed:
    f = parse_rss(f[1])
    site_news.append(f)
  return site_news


'''
d = feedparser.parse('http://www.reddit.com/r/python/.rss')

print d['feed']['title']
print d['feed']['link']
print d.feed.subtitle
print len(d['entries'])
print d['entries'][0]['title'] 
print d.entries[0]['link'] 
print d.entries[0]['link'] 
print d.headers

parse_rss('http://www.reddit.com/r/python/.rss')


print "done"
'''