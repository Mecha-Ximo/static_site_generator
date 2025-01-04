import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("a", TextType.BOLD)
        node2 = TextNode("a", TextType.BOLD)

        self.assertEqual(node1, node2)
    
    def test_eq_with_url(self):
        node1 = TextNode("a", TextType.BOLD, "http")
        node2 = TextNode("a", TextType.BOLD, "http")

        self.assertEqual(node1, node2)
    
    def test_not_eq_type(self):
        node1 = TextNode("a", TextType.CODE, "http")
        node2 = TextNode("a", TextType.BOLD, "http")

        self.assertNotEqual(node1, node2)

    def test_not_eq_url(self):
        node1 = TextNode("a", TextType.BOLD)
        node2 = TextNode("a", TextType.BOLD, "http:")

        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()