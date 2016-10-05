# Udacity course - INTRO TO COMPUTER SCIENCE
# Web crawler III
# Create the page index making use of dictionaries

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        # not found, add new keyword to index along its url
        index[keyword] = url

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        # works with "index" being either a listor a dictionary

# Initial version of crawl_web
# def crawl_web(seed):
#     tocrawl = [seed]
#     crawled = []
#     index = {} # Initializes "index" to be a dictionary
#     while tocrawl:
#         page = tocrawl.pop()
#         if page not in crawled:
#             content = get_page(page)
#             add_page_to_index(index, page, content)
#             union(tocrawl, get_all_links(content))
#             crawled.append(page)
#     return index

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

# Modified version of crawl_web where we include a graph of the 
# pages we've been through. Graph will also be a dictionary where the entries are
# url (target page): [url1, url2...] (pages that link to target)

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    graph = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links
            #build graph

            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

