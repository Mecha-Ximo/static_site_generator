from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node must have a value")

        if not self.tag:
            return self.value

        html = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        return html