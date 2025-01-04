import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_error_if_no_value(self):
        leaf = LeafNode(None, None)

        self.assertRaises(Exception, leaf.to_html)
    
    def test_to_html_raw_text_if_no_tag(self):
        leaf = LeafNode(None, "text")

        self.assertEqual(leaf.to_html(), "text")

    def test_to_html_tag_and_attr(self):
        leaf = LeafNode("a", "link", {"href": "blog.dev"})
        expected = '<a href="blog.dev">link</a>'

        self.assertEqual(leaf.to_html(), expected)