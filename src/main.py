from init_app_utils import init_public, generate_pages_recursively

def main():
    init_public()
    generate_pages_recursively("content", "template.html", "public")




main()