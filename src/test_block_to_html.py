import unittest

from htmlnode import HTMLNode
from block_to_html import markdown_to_html_node

class TestBlockToHTML(unittest.TestCase):
    def test_empty_md_is_div(self):
        self.assertEqual(str(markdown_to_html_node("")), str(HTMLNode("div", None, [])))

    def test_conversion(self):
        markdown = "## h2\n\n* u1\n* u2\n\nsome text"
        result = markdown_to_html_node(markdown)

        expected = HTMLNode("div", children=[
            HTMLNode("h2", "h2"),
            HTMLNode("ul", children=[
                HTMLNode("li", "u1"),
                HTMLNode("li", "u2"),
            ]),
            HTMLNode("p", "some text")
        ])

        self.assertEqual(str(result), str(expected))