import os
import json

def match_listings(listings, products):
  result = {}

  for listing in listings:
    product = find_product(listing, products)
    if product is not None:
      name = product['product_name']
      if name in result:
        result[name].append(listing)
      else:
        result[name] = []
        result[name].append(listing)       
  
  return result

def find_product(listing, products):

  listing_tags = extract_listing_tags(listing)

  product_ratings = {}
  for product in products:
    product_ratings[product['product_name']] = {'product':product, 'rating':0}

  for tag in listing_tags:
    product_matches = find_word_match_in_products(tag, products)
    for product_match in product_matches:
      product_rating = product_ratings[product_match['product_name']]
      product_ratings[product_match['product_name']] = {'product':product_rating['product'], 'rating':product_rating['rating'] + 1}

  pairs = return_dict_pairs_sorted_descending(product_ratings)
  
  if(pairs[0][1] > 0):
    return filter_by_model(pairs, listing_tags)  
  else:
    return None

def filter_by_model(pairs, listing_tags):
  potential_choices = list(filter(lambda x: x[1]!= 0, pairs))
    
  for potential_choice in potential_choices: 
    if verify_model(potential_choice, listing_tags):
      return potential_choice[0]
  return None

def verify_model(potential_product, listing_tags):
  tags = []

  model_stream = ''.join(potential_product[0]['model'].split())
  listing_stream = ''.join(listing_tags[0:7])

  if model_stream in listing_stream:
    return True
  return False

def extract_listing_tags(listing):
  title = listing['title']
  manufacturer = listing['manufacturer']
  tags = []
  tags.extend(title.split())
  tags.extend(manufacturer.split())
  return tags

def extract_product_tags(product):
  product_tags = []
  if 'manufacturer' in product:
    product_tags.extend(product['manufacturer'].split())
  if 'model' in product:
    model_tags = product['model'].split()
    model_tags.append(''.join(model_tags))
    product_tags.extend(model_tags)
  if 'family' in product:
    product_tags.extend(product['family'].split())

  return product_tags

def return_dict_pairs_sorted_descending(product_ratings):
  pairs = []
  for key in product_ratings.keys():
    value = product_ratings[key]
    pairs.append((value['product'], value['rating']))
  
  pairs = sorted(pairs, key=lambda v: v[1], reverse=True)
  return pairs

def find_word_match_in_products(listing_tag, products):
  matches = []  
  for product in products:
    product_tags = extract_product_tags(product)    
    if listing_tag in product_tags:
      matches.append(product)
  return matches

def read_products():
  script_dir = os.path.dirname(__file__)
  products_path = "products.txt"
  products_path = os.path.join(script_dir, products_path)

  products_file = open(products_path, 'r')

  products = []
  for line in products_file:
    product = json.loads(line)    
    products.append(product)

  products_file.close();
  return products

def read_listings():
  script_dir = os.path.dirname(__file__)
  listings_path = "listings.txt"
  listings_path = os.path.join(script_dir, listings_path)
  listings_file = open(listings_path, 'r')

  listings = []
  for line in listings_file:
    listing = json.loads(line)    
    listings.append(listing)

  listings_file.close()
  return listings
