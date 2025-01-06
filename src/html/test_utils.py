import unittest
from html.utils import extract_title

class TestHTMLUtils(unittest.TestCase):
    def test_extract_title_error(self):
        self.assertRaises(Exception,  lambda: extract_title("some text"))

    def test_extract_title_success(self):
        self.assertEqual(extract_title("# My title"), "My title")