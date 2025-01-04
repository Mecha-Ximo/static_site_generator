from functools import reduce
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required in parent node")
        if self.children == None:
            raise ValueError("Children is required in parent node")
        
        def recurse_to_html(acc: str, node: HTMLNode) -> str:
            if not node.children:
                acc += node.to_html()
                return acc
            
            return acc + f"<{node.tag}{node.props_to_html()}>{reduce(recurse_to_html, node.children, "")}</{node.tag}>"
        
        return f"<{self.tag}{self.props_to_html()}>{reduce(recurse_to_html, self.children, "")}</{self.tag}>"
        
