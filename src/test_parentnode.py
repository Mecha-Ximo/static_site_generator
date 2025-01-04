import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_raise_exception_if_no_tag(self):
        parent = ParentNode(None, None)

        self.assertRaises(ValueError, parent.to_html)

    def test_to_html_raise_exception_if_no_children(self):
        parent = ParentNode("div", None)
        self.assertRaises(ValueError, parent.to_html)

    def test_to_html_empty_children(self):
        parent = ParentNode("div", [])
        
        self.assertEqual(
            parent.to_html(),
            "<div></div>"
        )

    def test_to_html_deep_1(self):
        leaf = LeafNode('p', "some text", {"width":"100%"})
        parent1 = ParentNode('section', [leaf], {"width": "100%"})

        self.assertEqual(
            parent1.to_html(), 
            '<section width="100%"><p width="100%">some text</p></section>'
            )

    def test_to_html_deep_2(self):
        leaf = LeafNode('p', "some text", {"width":"100%"})
        parent1 = ParentNode('section', [leaf], {"width": "100%"})
        parent2 = ParentNode('div', [parent1, leaf], {"width": "97%"})

        self.assertEqual(
            parent2.to_html(),
            '<div width="97%"><section width="100%"><p width="100%">some text</p></section><p width="100%">some text</p></div>'
        )