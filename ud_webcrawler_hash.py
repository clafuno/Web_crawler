# Udacity course - INTRO TO COMPUTER SCIENCE
# Web crawler II
# Substitute the linear index by a hash table

# Function hash_string takes as inputs a keyword and a number of buckets,
# and returns a number representing the bucket for that keyword (index)
def hash_string(keyword,nbuckets):
    length = len(keyword)
    result = 0
    i = 0
    while i < length:
        result = result + ord(keyword[i])
        i = i + 1
    return result % nbuckets

# Different way of defining hash_string function:
# def hash_string(keyword,buckets):
#     h = 0
#     for c in keyword:
#         h = (h + ord(c))%buckets
#     return h

# Creating an empty hash table (empty set of buckets)
def make_hashtable(nbuckets):
    hash_table = []
    i = 0
    while i < nbuckets:
        hash_table.append([])
        i = i + 1
    return hash_table

# Different way of defining make_hashtable function
# def make_hashtable(nbuckets):
#     hash_table = []
#     for unused in range (0,nbuckets):
#         hash_table.append([])
#     return hash_table

# Function to obtain the bucket corresponding to a certain keyword.
# It uses the function hash_string to determine the index where that
# keyword is located and returns the whole bucket.
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

# Prodecure hastable_add adds a new keyword to the corresponding bucket.
def hashtable_add(htable,key,value):
    index = hash_string(key, len(htable))
    htable[index].append([key,value])
    return htable #optional

# Different way of defining hashtable_add:
# def hashtable_add(htable,key,value):
#     bucket = hashtable_get_bucket(htable,key)
#     bucket.append([key,value])
#     return htable

# Procedure hastable_lookup returns the value (URLs) associated with
# the provided keyword.
# It finds the bucket where the keyword is stored and then checks the first
# element (e[0]) of each sub-list within the bucket. When it finds it, returns
# the second element of the sub-list (URLs associated with the keyword).

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable,key)
    for e in bucket:
        if e[0] == key:
            return e[1]
    return None #Case when the word is NOT in the bucket

# Procedure hastable_update changes the value of the value assignated to a key.
def hastable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key)
    for e in bucket:
        if e[0] == key:
            e[1] = value
            return htable
    hashtable_add(htable,key,value) #Adds the keyword if it's not in the table
    return htable


# TEST of HASH FUNCTION
# Distributes a set of given keywords in buckets
def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        hv = func(w,size)
        results[hv] += 1
        keys_used.append(w)
    return results

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

words = get_page('http://www.gutenberg.org/files/1661/1661-h/1661-h.htm')
counts = test_hash_function(hash_string,words,12)
print counts
