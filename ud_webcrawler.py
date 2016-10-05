# Udacity course - INTRO TO COMPUTER SCIENCE
# Web crawler I
# First approach, simple linear index for URLs

def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
		return ""

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None,0
	start_quote = page.find('"',start_link)
	end_quote = page.find('"',start_quote)
	url = page[start_quote+1:end_quote]
	return url,end_quote

def get_all_links(page):
	links = [] #Initialize list of links
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

# Initial version of crawl_web procedure
# def crawl_web(seed):
# 	tocrawl = [seed]
# 	crawled = []
#
# 	while tocrawl:
# 		page = tocrawl.pop()
# 		if page not in crawled:
# 			web = get_page(page)
# 			union(tocrawl,get_all_links(web))
# 			crawled.append(page)
# 	return crawled

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

index = []
def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index,url,content):
    web = content.split()
    for word in web:
        add_to_index(index,word,url)

# Second version of crawl_web procedure including the index list
def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index,page,content)
			union(tocrawl,get_all_links(web))
			crawled.append(page)
	return crawled
