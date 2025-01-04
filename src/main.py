from textnode import TextNode, TextType
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    node1 = TextNode("Hello", TextType.BOLD, "https://some_url")
    leaf = LeafNode('p', "some text", {"width":"100%"})
    parent1 = ParentNode('section', [leaf], {"width": "100%"})
    parent2 = ParentNode('div', [parent1, leaf], {"width": "97%"})
    print(parent2.to_html())

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    )

    print(node.to_html())

main()