import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from utils import text_node_to_html_node, split_nodes_delimiter

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

    def test_split_node_single(self):
        text = TextNode("this is some text", TextType.TEXT)

        result = split_nodes_delimiter([text], "*", TextType.ITALIC)

        self.assertEqual([text], result)
    
    def test_split_node_italic(self):
        text = TextNode("this is *some* text", TextType.TEXT)

        result = split_nodes_delimiter([text], "*", TextType.ITALIC)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                          TextNode("some", TextType.ITALIC),
                          TextNode(" text", TextType.TEXT)],
                          result)
    
    def test_split_node_bold(self):
        text = TextNode("this is **some** text", TextType.TEXT)

        result = split_nodes_delimiter([text], "**", TextType.BOLD)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                          TextNode("some", TextType.BOLD),
                          TextNode(" text", TextType.TEXT)],
                          result)
    
    def test_split_node_bold(self):
        text = TextNode("this is `some` text", TextType.TEXT)

        result = split_nodes_delimiter([text], "`", TextType.CODE)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                          TextNode("some", TextType.CODE),
                          TextNode(" text", TextType.TEXT)],
                          result)
    
    def test_split_multi_nodes(self):
        text1 = TextNode("this is *some* *text*", TextType.TEXT)
        text2 = TextNode("this is *more*", TextType.TEXT)

        result = split_nodes_delimiter([text1, text2], "*", TextType.ITALIC)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                    TextNode("some", TextType.ITALIC),
                    TextNode(" ", TextType.TEXT),
                    TextNode("text", TextType.ITALIC),
                    TextNode("this is ", TextType.TEXT),
                    TextNode("more", TextType.ITALIC),
                    ],
                    result)
        
    def test_split_no_nodes(self):
        self.assertEqual(split_nodes_delimiter([], "*", TextType.ITALIC), [])
    
    def test_split_raise_if_wrong_delimiter(self):
        self.assertRaises(Exception, lambda _: split_nodes_delimiter([], "=", TextType.CODE))

    def test_split_multi_apply(self):
        text1 = TextNode("this is *some* **text**", TextType.TEXT)

        new_nodes = split_nodes_delimiter([text1], "**", TextType.BOLD)
        new_nodes_2 = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)

        self.assertEqual([
            TextNode("this is ", TextType.TEXT),
            TextNode("some", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("text", TextType.BOLD)],
            new_nodes_2
            )
