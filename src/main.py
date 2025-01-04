from textnode import TextNode, TextType

def main():
    node1 = TextNode("Hello", TextType.BOLD, "https://some_url")
    print(node1)

main()