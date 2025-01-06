from block_utils import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block.startswith("# "):
            return block[2:]
    
    raise Exception("Main header (h1 - #) is required in document")

