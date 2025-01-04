import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_if_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_if_prop(self):
        node = HTMLNode(props={"target": "_blank"})

        result = node.props_to_html()

        self.assertEqual(result, ' target="_blank"')

    def test_props_to_html_if_props(self):
        node = HTMLNode(props={
            "target": "_blank",
            "checked": ""
            })

        result = node.props_to_html()

        self.assertEqual(result, ' target="_blank" checked=""')
    
    def test_repr_no_args(self):
        node = HTMLNode()

        self.assertEqual(str(node), "HTMLNode -> TAG=None VALUE=None CHILDREN=None PROPS=None")

    def test_repr_with_args(self):
        node = HTMLNode("p", "text", [HTMLNode()], {"checked": ""})

        self.assertEqual(str(node), "HTMLNode -> TAG=p VALUE=text CHILDREN=[HTMLNode -> TAG=None VALUE=None CHILDREN=None PROPS=None] PROPS={'checked': ''}")

if __name__ == "__main__":
    unittest.main()