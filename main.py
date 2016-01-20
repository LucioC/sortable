import os
import json
from challenge import FileReader, Product, Listing
import challenge

reader = FileReader()
products = reader.read_products('products.txt');
listings = reader.read_listings('listings.txt');
listings = listings[0:1000]

result = challenge.match_listings(listings, products)

f = open('output.txt', 'w')

key_list = list(result.keys())
for key in key_list:
  f.write(json.dumps({ "product_name" : key, "listings" : result[key] }))
  f.write('\n')
  
f.close()





