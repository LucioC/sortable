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
key_list = sorted(key_list,key=lambda s: s.lower())
for key in key_list:
  f.write(json.dumps({ "product_name" : key, "listings" : result[key] }))
  f.write('\n')
  
f.close()

print("non matches: " + str(len(search.non_matches)))

f = open('output_non_matches.txt', 'w')

for non_match in search.non_matches:
  f.write(json.dumps(non_match.dict_without_tags()))
  f.write('\n')
  
f.close()

#verify solution
to_verify_list = reader.read_json_list('correct_partial_solution.txt')

not_on_list = []
for correct in to_verify_list:
  if correct['product_name'] not in key_list:
    not_on_list.append(correct['product_name'])
    
for error in not_on_list:
  print(error)





