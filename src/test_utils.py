import unittest

from textnode import TextNode, TextType
from utils import text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes

class TestUtils(unittest.TestCase):
    def test_text_to_html_TEXT(self):
        text = TextNode("text", TextType.TEXT)
        expected = "text"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected)

    def test_text_to_html_BOLD(self):
        text = TextNode("text", TextType.BOLD)
        expected = "<b>text</b>"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected)   

    def test_text_to_html_ITALIC(self):
        text = TextNode("text", TextType.ITALIC)
        expected = "<i>text</i>"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 
    
    def test_text_to_html_CODE(self):
        text = TextNode("text", TextType.CODE)
        expected = "<code>text</code>"

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 

    def test_text_to_html_LINK(self):
        text = TextNode("text", TextType.LINK, "google.com")
        expected = '<a href="google.com">text</a>'

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 

    def test_text_to_html_IMAGE(self):
        text = TextNode("text", TextType.IMAGE, "cat.png")
        expected = '<img alt="text" src="cat.png"></img>'

        html_node = text_node_to_html_node(text)

        self.assertEqual(html_node.to_html(), expected) 

    def test_split_node_single(self):
        text = TextNode("this is some text", TextType.TEXT)

        result = split_nodes_delimiter([text], "*", TextType.ITALIC)

        self.assertEqual([text], result)
    
    def test_split_node_italic(self):
        text = TextNode("this is *some* text", TextType.TEXT)

        result = split_nodes_delimiter([text], "*", TextType.ITALIC)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                          TextNode("some", TextType.ITALIC),
                          TextNode(" text", TextType.TEXT)],
                          result)
    
    def test_split_node_bold(self):
        text = TextNode("this is **some** text", TextType.TEXT)

        result = split_nodes_delimiter([text], "**", TextType.BOLD)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                          TextNode("some", TextType.BOLD),
                          TextNode(" text", TextType.TEXT)],
                          result)
    
    def test_split_node_bold(self):
        text = TextNode("this is `some` text", TextType.TEXT)

        result = split_nodes_delimiter([text], "`", TextType.CODE)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                          TextNode("some", TextType.CODE),
                          TextNode(" text", TextType.TEXT)],
                          result)
    
    def test_split_multi_nodes(self):
        text1 = TextNode("this is *some* *text*", TextType.TEXT)
        text2 = TextNode("this is *more*", TextType.TEXT)

        result = split_nodes_delimiter([text1, text2], "*", TextType.ITALIC)

        self.assertEqual([TextNode("this is ", TextType.TEXT),
                    TextNode("some", TextType.ITALIC),
                    TextNode(" ", TextType.TEXT),
                    TextNode("text", TextType.ITALIC),
                    TextNode("this is ", TextType.TEXT),
                    TextNode("more", TextType.ITALIC),
                    ],
                    result)
        
    def test_split_no_nodes(self):
        self.assertEqual(split_nodes_delimiter([], "*", TextType.ITALIC), [])
    
    def test_split_raise_if_wrong_delimiter(self):
        self.assertRaises(Exception, lambda _: split_nodes_delimiter([], "=", TextType.CODE))

    def test_split_multi_apply(self):
        text1 = TextNode("this is *some* **text**", TextType.TEXT)

        new_nodes = split_nodes_delimiter([text1], "**", TextType.BOLD)
        new_nodes_2 = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)

        self.assertEqual([
            TextNode("this is ", TextType.TEXT),
            TextNode("some", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("text", TextType.BOLD)],
            new_nodes_2
            )

    def test_extract_img_no_matches(self):
        result = extract_markdown_images("no images")

        self.assertEqual(result, [])
    
    def test_extract_img_single_match(self):
        result = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)")

        self.assertEqual(result, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')])

    def test_extract_img_multi_match(self):
        result = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")

        self.assertEqual(result, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_extract_link_no_matches(self):
        result = extract_markdown_links("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")

        self.assertEqual(result , [])
    
    def test_extract_link_single_match(self):
        result = extract_markdown_links("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")

        self.assertEqual(result, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif')])

    def test_extract_link_multi_match(self):
        result = extract_markdown_links("This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")

        self.assertEqual(result, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])

    def test_split_nodes_image_no_image(self):
        node = TextNode("some text", TextType.TEXT)
        result = split_nodes_image([node])

        self.assertEqual(result, [node])
    
    def test_split_nodes_image_with_image(self):
        node = TextNode("some text ![my image](./image.jpg)", TextType.TEXT)
        result = split_nodes_image([node])

        self.assertEqual(result, [
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.IMAGE, "./image.jpg")
        ])
    
    def test_split_nodes_image_with_multi_image(self):
        node = TextNode("some text ![my image](./image.jpg) ![my image2](./image.jpg)", TextType.TEXT)
        result = split_nodes_image([node])

        self.assertEqual(result, [
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.IMAGE, "./image.jpg"),
            TextNode(" ", TextType.TEXT,),
            TextNode("my image2", TextType.IMAGE, "./image.jpg")
        ])

    def test_split_nodes_image_with_multi_node(self):
        node = TextNode("some text ![my image](./image.jpg) ![my image2](./image.jpg)", TextType.TEXT)
        node2 = TextNode("some text ![my image](./image.jpg) ![my image2](./image.jpg)", TextType.TEXT)
        result = split_nodes_image([node, node2])

        self.assertEqual(result, [
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.IMAGE, "./image.jpg"),
            TextNode(" ", TextType.TEXT,),
            TextNode("my image2", TextType.IMAGE, "./image.jpg"),
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.IMAGE, "./image.jpg"),
            TextNode(" ", TextType.TEXT,),
            TextNode("my image2", TextType.IMAGE, "./image.jpg")
        ])

    def test_split_nodes_link_no_link(self):
        node = TextNode("some text", TextType.TEXT)
        result = split_nodes_link([node])

        self.assertEqual(result, [node])

    def test_split_nodes_link_with_link(self):
        node = TextNode("some text [my image](./image.jpg)", TextType.TEXT)
        result = split_nodes_link([node])

        self.assertEqual(result, [
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.LINK, "./image.jpg")
        ])

    def test_split_nodes_link_with_multi_link(self):
        node = TextNode("some text [my image](./image.jpg) [my image2](./image.jpg)", TextType.TEXT)
        result = split_nodes_link([node])

        self.assertEqual(result, [
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.LINK, "./image.jpg"),
            TextNode(" ", TextType.TEXT,),
            TextNode("my image2", TextType.LINK, "./image.jpg")
        ])

    def test_split_nodes_link_with_multi_node(self):
        node = TextNode("some text [my image](./image.jpg) [my image2](./image.jpg)", TextType.TEXT)
        node2 = TextNode("some text [my image](./image.jpg) [my image2](./image.jpg)", TextType.TEXT)
        result = split_nodes_link([node, node2])

        self.assertEqual(result, [
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.LINK, "./image.jpg"),
            TextNode(" ", TextType.TEXT,),
            TextNode("my image2", TextType.LINK, "./image.jpg"),
            TextNode("some text ", TextType.TEXT),
            TextNode("my image", TextType.LINK, "./image.jpg"),
            TextNode(" ", TextType.TEXT,),
            TextNode("my image2", TextType.LINK, "./image.jpg")
        ])

    def test_text_to_text_nodes_base(self):
        text = "aa"
        result = text_to_textnodes(text)

        self.assertEqual(result, [TextNode(text, TextType.TEXT)])
    
    def test_text_to_textnode_full(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)

        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])