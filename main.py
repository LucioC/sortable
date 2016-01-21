import os
import json
from challenge import FileReader, Product, Listing, MatchSearch
import challenge

reader = FileReader()
search = MatchSearch()
products = reader.read_products('products.txt');
listings = reader.read_listings('listings.txt');
listings = listings[0:1000]

result = search.match_listings(listings, products, debug = lambda c: print(c))

f = open('output.txt', 'w')

key_list = list(result.keys())
for key in key_list:
  f.write(json.dumps({ "product_name" : key, "listings" : result[key] }))
  f.write('\n')
  
f.close()

print(len(search.non_matches))
#for non_match in search.non_matches[0:100]:
#  print(non_match.dict_without_tags())





