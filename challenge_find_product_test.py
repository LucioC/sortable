import unittest
from challenge import FileReader, Listing, Product
import challenge
import json

class TestChallengeFindProductByListing(unittest.TestCase):

  def test_find_canonSX130IS(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"199.96"})
    expected_product = json.loads('{"product_name":"Canon_PowerShot_SX130_IS","manufacturer":"Canon","model":"SX130 IS","family":"PowerShot","announced-date":"2010-08-18T20:00:00.000-04:00"}')
    expected_product = Product.create(expected_product)
    product = challenge.find_product(listing, products)    
    self.assertEqual(expected_product, product, json.dumps(product.__dict__))

  def test_dont_find_MacroRingLight(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"LED Flash Macro Ring Light (48 X LED) with 6 Adapter Rings for For Canon/Sony/Nikon/Sigma Lenses","manufacturer":"Neewer Electronics Accessories","currency":"CAD","price":"35.99"})
    product = challenge.find_product(listing, products)
    self.assertEqual(None, product, product)

  def test_find_2ndcanonSX130IS(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Canon PowerShot SX130IS 12.1 MP Digital Camera with 12x Wide Angle Optical Image Stabilized Zoom with 3.0-Inch LCD","manufacturer":"Canon Canada","currency":"CAD","price":"209.00"})
    expected_product = json.loads('{"product_name":"Canon_PowerShot_SX130_IS","manufacturer":"Canon","model":"SX130 IS","family":"PowerShot","announced-date":"2010-08-18T20:00:00.000-04:00"}')
    expected_product = Product.create(expected_product)
    product = challenge.find_product(listing, products)    
    self.assertEqual(expected_product, product)

  def test_find_PowerShotD10(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Canon PowerShot D10 12.1 MP Waterproof Digital Camera with 3x Optical Image Stabilized Zoom and 2.5-inch LCD (Blue/Silver)","manufacturer":"Canon Canada","currency":"CAD","price":"306.24"})
    expected_product = json.loads('{"product_name":"Canon_PowerShot_D10","manufacturer":"Canon","model":"D10","family":"PowerShot","announced-date":"2009-02-17T19:00:00.000-05:00"}')
    expected_product = Product.create(expected_product)
    product = challenge.find_product(listing, products)    
    self.assertEqual(expected_product, product)

  def test_dont_find_i9000GalaxySBattery(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Genuine Samsung EB575152VU i9000 GalaxyS Battery","manufacturer":"Samsung","currency":"CAD","price":"13.99"})
    product = challenge.find_product(listing, products)    
    self.assertEqual(None, product)
  
  def test_find_PowerShotA1200(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Canon PowerShot A1200 (Black)","manufacturer":"Canon Canada","currency":"CAD","price":"129.99"})
    expected_product = json.loads('{"product_name":"Canon-A1200","manufacturer":"Canon","model":"A1200","family":"PowerShot","announced-date":"2011-01-04T19:00:00.000-05:00"}')
    expected_product = Product.create(expected_product)
    product = challenge.find_product(listing, products)    
    self.assertEqual(expected_product, product)

  def test_find_PowerShotA495(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Canon PowerShot A495 10.1 MP Digital Camera with 3.3x Optical Zoom and 2.5-Inch LCD (Blue)","manufacturer":"Canon Canada","currency":"CAD","price":"88.00"})
    expected_product = json.loads('{"product_name":"Canon_PowerShot_A495","manufacturer":"Canon","model":"A495","family":"PowerShot","announced-date":"2010-01-04T19:00:00.000-05:00"}')
    expected_product = Product.create(expected_product)
    product = challenge.find_product(listing, products)    
    self.assertEqual(expected_product, product)

  def test_find_KodakZ981(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Kodak EasyShare Z981 14MP Digital Camera with Schneider-Kreuznach Variogon 26x Wide Angle Optical Image Stabilized Zoom Lens and 3.0 Inch LCD","manufacturer":"Kodak","currency":"CAD","price":"299.00"})
    expected_product = json.loads('{"product_name":"Kodak_EasyShare_Z981","manufacturer":"Kodak","model":"Z981","family":"EasyShare","announced-date":"2010-01-04T19:00:00.000-05:00"}')
    expected_product = Product.create(expected_product)
    product = challenge.find_product(listing, products)    
    self.assertEqual(expected_product, product)

  def test_dont_find_NikonENEL9aBattery(self):
    reader = FileReader()
    products = reader.read_products('products.txt')
    listing = Listing.create({"title":"Nikon EN-EL9a 1080mAh Ultra High Capacity Li-ion Battery Pack for Nikon D40, D40x, D60, D3000, & D5000 Digital SLR Cameras","manufacturer":"Nikon","currency":"CAD","price":"29.75"})
    product = challenge.find_product(listing, products)    
    self.assertEqual(None, product)
    
  def test_dont_find_LeicaDigiluxZoom_WhenListingIsPanasonic(self):
    reader = FileReader()
    products = [Product.create({"product_name":"Leica_Digilux_Zoom","manufacturer":"Leica","model":"Zoom","family":"Digilux","announced-date":"2000-02-03T19:00:00.000-05:00"})]
    listing = Listing.create({"currency": "CAD", "price": "489.95", "title": "Panasonic Lumix ZS10 Red 16x Zoom Taxes Included", "manufacturer": "Panasonic"})
    product = challenge.find_product(listing, products)    
    self.assertEqual(None, product)
    
  def test_should_not_find_canonPowerShotG1_WhenListingIsCanonNB7LBattery(self):    
    reader = FileReader()
    products = [Product.create({"product_name":"Canon_PowerShot_G1","manufacturer":"Canon","model":"G1","family":"PowerShot","announced-date":"2000-09-17T20:00:00.000-04:00"})]
    listing = Listing.create({
                "currency": "CAD",
                "title": "Canon NB-7L Lithium-Ion Battery for G10, G11, G12 Cameras",
                "manufacturer": "Canon",
                "price": "44.99"
            })
    product = challenge.find_product(listing, products)    
    self.assertEqual(None, product)    
  
  def test_should_not_find_nikonCoolpix100_WhenListingIsNikonENEL51100maH(self):
    reader = FileReader()
    products = [Product.create({"product_name":"Nikon_Coolpix_100","manufacturer":"Nikon","model":"100","family":"Coolpix","announced-date":"1997-01-19T19:00:00.000-05:00"})]
    listing = Listing.create({
                "currency": "CAD",
                "title": "Nikon EN-EL5 1100mAh Ultra High Capacity Li-ion Battery Pack for Nikon P100, P90, P80, P6000",
                "manufacturer": "Nikon",
                "price": "19.99"
            })
    product = challenge.find_product(listing, products)    
    self.assertEqual(None, product)
  
  def test_should_find_SonyW310_WhenListingIsSonyW310S(self):
    reader = FileReader()
    products = [Product.create({"product_name":"Sony_Cyber-shot_DSC-W310","manufacturer":"Sony","model":"DSC-W310","family":"Cyber-shot","announced-date":"2010-01-06T19:00:00.000-05:00"})]
    listing = Listing.create({
              "title":"Sony DSC-W310S Digitalkamera (12 Megapixel, 28mm Weitwinkelobjektiv mit 4fach optischem Zoom, 6,9 cm (2,7 Zoll) LC-Display) silber",
              "manufacturer":"Sony",
              "currency":"EUR",
              "price":"65.99"
              })
    product = challenge.find_product(listing, products)    
    self.assertEqual(products[0], product)
    
  
  def test_should_not_find_OlympusC2100UZ_WhenListingIsOlympusUZSeries(self):
    reader = FileReader()
    products = [Product.create({"product_name":"Olympus_C-2100_UZ","manufacturer":"Olympus","model":"C-2100 UZ","announced-date":"2000-06-14T20:00:00.000-04:00"})]
    listing = Listing.create({
                "currency": "CAD",
                "manufacturer": "Olympus",
                "title": "Olympus UZ Series 14 MP 30 X",
                "price": "257.87"
              })
    product = challenge.find_product(listing, products)    
    self.assertEqual(None, product)
    
  def test_should_not_find_OlympusC2100UZ_WhenListingIsOlympusUZSeries(self):
    reader = FileReader()
    products = [Product.create({"product_name":"Olympus-TG310","manufacturer":"Olympus","model":"TG310","announced-date":"2011-02-15T19:00:00.000-05:00"})]
    listing = Listing.create({
                "manufacturer": "Olympus Canada", 
                "title": "Olympus TG-310 14 MP Digital Camera with 3.6x Optical Zoom, Waterproof, Shockproof, Freezer Proof (Red)", 
                "price": "199.99", 
                "currency": "CAD"
              })
              
    product = challenge.find_product(listing, products)    
    self.assertEqual(products[0], product)
    
if __name__ == '__main__':
    unittest.main()
