from init_app_utils import init_public, generate_page

def main():
    init_public()
    generate_page("content/index.md", "template.html", "public/index.html")




main()