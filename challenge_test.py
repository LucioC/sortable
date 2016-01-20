import unittest
from challenge import FileReader, Listing, Product
import challenge
import json

class TestChallengeFindProductByListing(unittest.TestCase):

  def listings(self,listings_json):
    listings = []
    for l in listings_json:
      listings.append(Listing.create(l))
      
    return listings
    
  def test_generate_output_for_2_listings_products(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listings = self.listings([{"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"199.96"}, {"title":"Canon PowerShot D10 12.1 MP Waterproof Digital Camera with 3x Optical Image Stabilized Zoom and 2.5-inch LCD (Blue/Silver)","manufacturer":"Canon Canada","currency":"CAD","price":"306.24"}])
    
    expected_output = json.loads('{"Canon_PowerShot_SX130_IS": [{"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"199.96"}] , "Canon_PowerShot_D10": [{"title":"Canon PowerShot D10 12.1 MP Waterproof Digital Camera with 3x Optical Image Stabilized Zoom and 2.5-inch LCD (Blue/Silver)","manufacturer":"Canon Canada","currency":"CAD","price":"306.24"}] }')
    result = challenge.match_listings(listings, products)   
    self.assertEqual(expected_output, result, result)

  def test_generate_output_for_3_listings_being2_for_one_product(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listings = self.listings([{"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"209.00"},{"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"199.96"}, {"title":"Canon PowerShot D10 12.1 MP Waterproof Digital Camera with 3x Optical Image Stabilized Zoom and 2.5-inch LCD (Blue/Silver)","manufacturer":"Canon Canada","currency":"CAD","price":"306.24"}])
    expected_output = json.loads('{"Canon_PowerShot_SX130_IS" :[{"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"209.00"},{"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"199.96"}],"Canon_PowerShot_D10": [{"title":"Canon PowerShot D10 12.1 MP Waterproof Digital Camera with 3x Optical Image Stabilized Zoom and 2.5-inch LCD (Blue/Silver)","manufacturer":"Canon Canada","currency":"CAD","price":"306.24"}]}')
    result = challenge.match_listings(listings, products)
    
    self.assertEqual(expected_output, result)

if __name__ == '__main__':
    unittest.main()
