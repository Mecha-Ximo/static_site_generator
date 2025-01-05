import re
from block_type import Block

heading_regex = r"^#{1,6} "
code_regex = r"^`{3}.*`{3}"

def markdown_to_blocks(markdown: str):
    raw_blocks = markdown.split("\n\n")
    trimmed_blocks = list(map(lambda x: x.strip(), raw_blocks))
    filtered_blocks = list(filter(lambda x: x != "", trimmed_blocks))

    return filtered_blocks

def block_to_block_type(block: str):
    if re.match(heading_regex, block):
        return Block.H.value
    if re.match(code_regex, block):
        return Block.CODE.value
    if block.startswith("> "):
        return Block.QUOTE.value
    if check_ul_block(block):
        return Block.UL.value
    if check_ol_block(block):
        return Block.OL.value
    
    return Block.P.value

def check_ul_block(block: str):
    is_ul = re.match(r"^[*-] ", block)
    if not is_ul:
        return False
    
    lines = block.split("\n")

    if block.startswith("*"):
        for line in lines:
            if not line.startswith("* "):
                return False
        return True
    
    if block.startswith("-"):
        for line in lines:
            if not line.startswith("- "):
                return False
        return True
    
    return False

        


def check_ol_block(block: str):
    lines = block.split("\n")

    for i in range(0, len(lines)):
        if not lines[i].startswith(f"{i + 1}. "):
            return False
    return True