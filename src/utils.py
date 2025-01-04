from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(value="", tag = "img", props={
                "alt":text_node.text,
                "src":text_node.url
            })

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    delimiters = ["*", "**", "`"]
    if not delimiter in delimiters:
        raise Exception("Unsupported delimiter")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        for i in range(0, len(parts)):
            if parts[i] == "":
                continue
            
            if i % 2 == 0:
                new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(parts[i], text_type))
    
    return new_nodes
