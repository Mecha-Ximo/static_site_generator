import unittest

from block_utils import markdown_to_blocks

class TestBlockUtils(unittest.TestCase):
    def test_markdown_to_blocks_empty_markdown(self):
        self.assertEqual(markdown_to_blocks(""), [])

    def test_markdown_to_block_paragraphs(self):
        text = "# header\n\nsome text\n\n- list1\n- list2\n"

        self.assertEqual(markdown_to_blocks(text), ["# header", "some text", "- list1\n- list2"])