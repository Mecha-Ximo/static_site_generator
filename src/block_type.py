from enum import Enum

class Block(Enum):
    P = "paragraph"
    H = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"