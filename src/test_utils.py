import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from utils import text_node_to_html_node

class TestUtils(unittest.TestCase):
    def test_text_to_html_TEXT(self):
        text = TextNode("text", TextType.TEXT)
        expected = "text"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected)

    def test_text_to_html_BOLD(self):
        text = TextNode("text", TextType.BOLD)
        expected = "<b>text</b>"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected)   

    def test_text_to_html_ITALIC(self):
        text = TextNode("text", TextType.ITALIC)
        expected = "<i>text</i>"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 
    
    def test_text_to_html_CODE(self):
        text = TextNode("text", TextType.CODE)
        expected = "<code>text</code>"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 

    def test_text_to_html_LINK(self):
        text = TextNode("text", TextType.LINK, "google.com")
        expected = '<a href="google.com">text</a>'

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 

    def test_text_to_html_IMAGE(self):
        text = TextNode("text", TextType.IMAGE, "cat.png")
        expected = '<img alt="text" src="cat.png"></img>'

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 
