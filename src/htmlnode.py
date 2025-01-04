from functools import reduce

class HTMLNode:
    def __init__(self, 
                 tag=None, 
                 value=None, 
                 children=None, 
                 props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Implemented by children")

    def props_to_html(self):
        if not self.props:
            return ""
        
        def stringify_prop(acc, prop):
            return f"{acc} {prop[0]}=\"{prop[1]}\""
        
        return reduce(stringify_prop, self.props.items(), "")
    
    def __repr__(self):
        return f"HTMLNode -> TAG={self.tag} VALUE={self.value} CHILDREN={self.children} PROPS={self.props}"