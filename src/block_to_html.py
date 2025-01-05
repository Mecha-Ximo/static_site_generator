from block_utils import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for md_block in markdown_blocks:
        block_type = block_to_block_type(md_block)

        if block_type == "heading":
            h_node = convert_heading_block(md_block)
            html_nodes.append(h_node)
        if block_type == "ordered_list":
            html_nodes.append(convert_list(md_block, "ol"))
        if block_type == "unordered_list":
            html_nodes.append(convert_list(md_block, "ul"))
        if block_type == "paragraph":
            html_nodes.append(HTMLNode("p", md_block))
        if block_type == "code":
            html_nodes.append(HTMLNode("code", md_block.strip("`")))
        if block_type == "quote":
            html_nodes.append(convert_quote(md_block))

    return HTMLNode("div", None, html_nodes)

def convert_heading_block(block):
    h_mapper = {
        "# ": "h1",
        "## ": "h2",
        "### ": "h3",
        "#### ": "h4",
        "##### ": "h5",
        "###### ": "h6",
    }

    for k in h_mapper:
        _, content = block.split(k)
        if block.startswith(k):
            return HTMLNode(h_mapper[k], content)
        
def convert_list(block, type):
    li_elements = []
    parts = block.split("\n")

    for part in parts:
        li_elements.append(HTMLNode("li", part[2:]))

    return HTMLNode(type, None, li_elements)

def convert_quote(block):
    content = ""
    for text in block.split("\n"):
        content += text[2:]
    
    return HTMLNode("blockquote", content)
        