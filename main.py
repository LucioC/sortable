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
products_expected = []
for item in to_verify_list:
  products_expected.append(item['product_name'])

expected_missing = []
for correct in products_expected:
  if correct not in key_list:
    expected_missing.append(correct)
    
print("expected to be on output:")
for error in expected_missing:
  print(error)

non_expected_list = [] 
for o in key_list:
  if o not in products_expected:
    non_expected_list.append(o)

print("Non expected to be on output:")
for error in non_expected_list:
  print(error)





