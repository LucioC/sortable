import os
import json

class MatchSearch:  
  def __init__(self):
    self.result = {}
    self.non_matches = []
  
  def match_listings(self, listings, products, debug=None):
    self.result = {}
    self.non_matches = []
    count = 0
    for listing in listings:
      product = find_product(listing, products)
      count += 1
      if debug is not None:
        debug(count)
      
      if product is not None:
        name = product.name
        if name in self.result:
          self.result[name].append(listing.dict_without_tags())
        else:
          self.result[name] = []
          self.result[name].append(listing.dict_without_tags()) 
      else:
        self.non_matches.append(listing)
    return self.result    

def find_product(listing, products):

  listing_tags = listing.extract_tags()

  product_ratings = {}
  for product in products:
    product_ratings[product.name] = {'product':product, 'rating':0}

  for tag in listing_tags:
    product_matches = find_word_match_in_products(tag, products)
    for product_match in product_matches:
      product_rating = product_ratings[product_match.name]
      product_ratings[product_match.name] = {'product':product_rating['product'], 'rating':product_rating['rating'] + 1}

  pairs = return_dict_pairs_sorted_descending(product_ratings)
  
  if(pairs[0][1] > 0):
    return filter_by_model(pairs, listing_tags)  
  else:
    return None

def filter_by_model(pairs, listing_tags):
  potential_choices = list(filter(lambda x: x[1]!= 0, pairs))
    
  for potential_choice in potential_choices: 
    #if has rating greater than 1 and model is present
    if potential_choice[1] > 1 and verify_model(potential_choice, listing_tags):
      return potential_choice[0]
  return None

def verify_model(potential_product, listing_tags):
  model = prepare_string(potential_product[0].model)
  
  split = model.split()
  if len(split) == 1:
    for tag in listing_tags:
      if tag.startswith(model):
        return True
  else:
    join_model = ''.join(model.split())
    for tag in listing_tags:
      if tag.startswith(join_model):
        return True
    
    listing_sentence = ' '.join(listing_tags)
    if model in listing_sentence:
      return True
      
  return False

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
    product_tags = product.extract_tags()
    if listing_tag in product_tags:
      matches.append(product)
  return matches
  
ignored = 'dmc'
def prepare_string(s):
  s = s.translate(s.maketrans("", "", ",.-!")).lower()
  s = s.replace(ignored, '')
  return s
  
class Listing:
  def __init__(self, title, manufacturer, currency, price):
    self.title = title
    self.manufacturer = manufacturer
    self.currency = currency
    self.price = price
    self.tags = []
  
  def dict_without_tags(self):  
    d = dict(self.__dict__)
    if 'tags' in d:
      del d['tags'] 
    return d
    
  def __eq__(self, other):
    return (isinstance(other, self.__class__)
      and self.dict_without_tags() == other.dict_without_tags())
    
  def extract_tags(self):
    if not self.tags:
      self.tags = self.extract_listing_tags()    
    return self.tags
    
  def extract_listing_tags(self):
    title = prepare_string(self.title)
    manufacturer = prepare_string(self.manufacturer)
    tags = []
    tags.extend(title.split()[0:5])
    tags.extend(manufacturer.split())
    return tags  
    
  @staticmethod
  def create(json_object):
    return Listing(json_object['title'],json_object['manufacturer'],json_object['currency'], json_object['price'])
  
class Product:
  def __init__(self, name, manufacturer, model, family, announced_date):
    self.name = name
    self.manufacturer = manufacturer
    self.model = model
    self.family = family
    self.announced_date = announced_date
    self.tags = []
      
  def dict_without_tags(self):  
    d = dict(self.__dict__)
    if 'tags' in d:
      del d['tags'] 
    return d
    
  def __repr__(self):
    return json.dumps(self.dict_without_tags())
    
  def __eq__(self, other):
    return (isinstance(other, self.__class__)
      and self.dict_without_tags() == other.dict_without_tags())
    
  def extract_tags(self):
    if not self.tags:
      self.tags = self.extract_product_tags()    
    return self.tags
    
  def extract_product_tags(self):
    product_tags = []
    manufacturer = prepare_string(self.manufacturer)
    family = prepare_string(self.family)
    model = prepare_string(self.model)
    product_tags.extend(manufacturer.split())
    model_tags = model.split()
    model_tags.append(''.join(model_tags))
    product_tags.extend(model_tags)
    product_tags.extend(family.split())
    return product_tags
      
  @staticmethod
  def create(json_object):
    return Product(json_object['product_name'], json_object['manufacturer'], json_object['model'], json_object['family'] if 'family' in json_object else '', json_object['announced-date'])

class FileReader:
  
  def read_listings(self, filename):
    listings_json = self.read_json_list(filename)
    listings = []
    for listing_json in listings_json:
      listings.append(Listing.create(listing_json))
      
    return listings
  
  def read_products(self, filename):
    products_json = self.read_json_list(filename)
    products = []
    for product_json in products_json:
      products.append(Product.create(product_json))
      
    return products
  
  def read_json_list(self,filename):
    script_dir = os.path.dirname(__file__)
    file_path = filename
    file_path = os.path.join(script_dir, file_path)

    items_file = open(file_path, 'r')

    items = []
    for line in items_file:
      item = json.loads(line)    
      items.append(item)

    items_file.close();
    return items

