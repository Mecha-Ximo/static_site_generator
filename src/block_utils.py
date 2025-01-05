def markdown_to_blocks(markdown: str):
    raw_blocks = markdown.split("\n\n")
    trimmed_blocks = list(map(lambda x: x.strip(), raw_blocks))
    filtered_blocks = list(filter(lambda x: x != "", trimmed_blocks))

    return filtered_blocks