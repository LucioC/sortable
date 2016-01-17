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


if __name__ == '__main__':
    unittest.main()
