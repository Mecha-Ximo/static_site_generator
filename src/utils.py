import re
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

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"[^!]\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    return splitter(old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    return splitter(old_nodes, TextType.LINK)

def splitter(old_nodes, text_type):
    accepted_types = [TextType.LINK, TextType.IMAGE]
    if not text_type in accepted_types:
        raise ValueError("Not accepted type")
    
    type_mapper = {}
    type_mapper[TextType.LINK] = {
            "extracter": extract_markdown_links,
            "delimiter": lambda x,y: f"[{x}]({y})" 
        }
    type_mapper[TextType.IMAGE] = {
            "extracter": extract_markdown_images,
            "delimiter": lambda x,y: f"![{x}]({y})" 
        }


    old_nodes_copy = old_nodes.copy()
    new_nodes: list[TextNode] = []

    for node in old_nodes_copy:
        extractables = type_mapper[text_type]["extracter"](node.text)

        if not extractables:
            new_nodes.append(node)
            continue

        for extractable in extractables:
            parts: list[str] = node.text.split(type_mapper[text_type]["delimiter"](extractable[0], extractable[1]), 1)
            
            new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(extractable[0], text_type, extractable[1]))

            node.text = parts[1]

    new_nodes = list(filter(lambda x: x.text != "", new_nodes))
    return new_nodes