from textnode import TextNode, TextType
from leafnode.leafnode import LeafNode

def main():
    node1 = TextNode("Hello", TextType.BOLD, "https://some_url")
    leaf = LeafNode('p', "some text", {"width":"100%"})
    print(leaf.to_html())

main()