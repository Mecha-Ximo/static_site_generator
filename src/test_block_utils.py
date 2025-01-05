import unittest

from block_utils import markdown_to_blocks, block_to_block_type

class TestBlockUtils(unittest.TestCase):
    def test_markdown_to_blocks_empty_markdown(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_markdown_to_block_paragraphs(self):
        text = "# header\n\nsome text\n\n- list1\n- list2\n"

        self.assertEqual(markdown_to_blocks(text), ["# header", "some text", "- list1\n- list2"])
    
    def test_block_to_block_type_base(self):
        self.assertEqual(block_to_block_type("some text"), "paragraph")

    def test_block_to_block_type_headings(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "heading")

        for _ in range(0, 5):
            block = "#" + block
            self.assertEqual(block_to_block_type(block), "heading")
        
        block = "#" + block
        self.assertNotEqual(block_to_block_type(block), "heading")
    
    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("``` a ```"), "code")
    
    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> quote\n> quote"), "quote")

    def test_block_to_block_type_wrong_quote(self):
        self.assertNotEqual(block_to_block_type("> quote\n* quote"), "quote")

    def test_block_to_block_type_ul(self):
        self.assertEqual(block_to_block_type("* quote\n* quote"), "unordered_list")
        self.assertEqual(block_to_block_type("- quote\n- quote"), "unordered_list")
    
    def test_block_to_block_type_ul_wrong(self):
        self.assertNotEqual(block_to_block_type("* quote\n- quote"), "unordered_list")
        self.assertNotEqual(block_to_block_type("- quote\n* quote"), "unordered_list")

    def test_block_to_block_type_ol(self):
        self.assertEqual(block_to_block_type("1. quote\n2. quote"), "ordered_list")
    
    def test_block_to_block_type_wrong_ol(self):
        self.assertNotEqual(block_to_block_type("2. quote\n"), "ordered_list")
        self.assertNotEqual(block_to_block_type("1.quote\n3. quote\n2. quote\n"), "ordered_list")