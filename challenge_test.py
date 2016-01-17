import unittest
import challenge
import json

class TestChallenge(unittest.TestCase):

  def test_find_canonSX130IS(self):
    products = challenge.read_products()
    listings = challenge.read_listings()    
    expected_product = json.loads('{"product_name":"Canon_PowerShot_SX130_IS","manufacturer":"Canon","model":"SX130 IS","family":"PowerShot","announced-date":"2010-08-18T20:00:00.000-04:00"}')
    product = challenge.find_product(listings[1], products)    
    self.assertEqual(expected_product, product)

  def test_dont_find_MacroRingLight(self):
    products = challenge.read_products()
    listings = challenge.read_listings()
    product = challenge.find_product(listings[0], products)
    self.assertEqual(None, product, product)

  def test_find_2ndcanonSX130IS(self):
    products = challenge.read_products()
    listings = challenge.read_listings()    
    expected_product = json.loads('{"product_name":"Canon_PowerShot_SX130_IS","manufacturer":"Canon","model":"SX130 IS","family":"PowerShot","announced-date":"2010-08-18T20:00:00.000-04:00"}')
    product = challenge.find_product(listings[2], products)    
    self.assertEqual(expected_product, product)

  def test_find_PowerShotD10(self):
    products = challenge.read_products()
    listings = challenge.read_listings()    
    expected_product = json.loads('{"product_name":"Canon_PowerShot_D10","manufacturer":"Canon","model":"D10","family":"PowerShot","announced-date":"2009-02-17T19:00:00.000-05:00"}')
    product = challenge.find_product(listings[3], products)    
    self.assertEqual(expected_product, product)

  def test_dont_find_i9000GalaxySBattery(self):
    products = challenge.read_products()
    listings = challenge.read_listings()
    product = challenge.find_product(listings[5], products)    
    self.assertEqual(None, product)
  
  def test_find_PowerShotA1200(self):
    products = challenge.read_products()
    listings = challenge.read_listings()    
    expected_product = json.loads('{"product_name":"Canon-A1200","manufacturer":"Canon","model":"A1200","family":"PowerShot","announced-date":"2011-01-04T19:00:00.000-05:00"}')
    product = challenge.find_product(listings[6], products)    
    self.assertEqual(expected_product, product)

  def test_find_PowerShotA495(self):
    products = challenge.read_products()
    listings = challenge.read_listings()    
    expected_product = json.loads('{"product_name":"Canon_PowerShot_A495","manufacturer":"Canon","model":"A495","family":"PowerShot","announced-date":"2010-01-04T19:00:00.000-05:00"}')
    product = challenge.find_product(listings[7], products)    
    self.assertEqual(expected_product, product)

  def test_find_KodakZ971(self):
    products = challenge.read_products()
    listings = challenge.read_listings()    
    expected_product = json.loads('{"product_name":"Kodak_EasyShare_Z981","manufacturer":"Kodak","model":"Z981","family":"EasyShare","announced-date":"2010-01-04T19:00:00.000-05:00"}')
    product = challenge.find_product(listings[12], products)    
    self.assertEqual(expected_product, product)

  def test_dont_find_NikonENEL9aBattery(self):
    products = challenge.read_products()
    listings = challenge.read_listings()    
    product = challenge.find_product(listings[14], products)    
    self.assertEqual(None, product)

if __name__ == '__main__':
    unittest.main()
