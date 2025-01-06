import os
import shutil

from block_to_html import markdown_to_html_node
from html.utils import extract_title
from inline_utils import text_to_textnodes, text_node_to_html_node

def init_public():
    clean_public()
    create_public()
    copy_recursive("static", "public")

def clean_public():
    if not os.path.exists("public"):
        print("[SKIP] PUBLIC dir does not exists")
        return
    
    print("[ ] Cleaning public dir...")

    remove_recursive("public")

    print("[x] Public dir clean-up complete")

def create_public():
    if os.path.exists("public"):
        print("[SKIP] PUBLIC already exists")
    else:
        print("[ ] Creating PUBLIC...")
        os.mkdir("public")
        print("[x] PUBLIC created!")

def remove_recursive(current_path):
    for path in os.listdir(current_path):
        full_path = os.path.join(current_path, path)

        if os.path.isfile(full_path):
            print(f"- Removing FILE: {full_path}")
            os.remove(full_path)
        else:
            remove_recursive(full_path)
            print(f"- Removing DIR: {full_path}")

    os.removedirs(current_path)

def copy_recursive(src_path, dst_path):
    if not os.path.exists(src_path):
        raise Exception(f"Source path '{src_path}' does not exist")
    if not os.path.exists(dst_path):
        raise Exception(f"Destination path '{dst_path}' does not exist")

    for path in os.listdir(src_path):
        final_src_path = os.path.join(src_path, path)
        final_dst_path = os.path.join(dst_path, path)

        if os.path.isfile(final_src_path):
            shutil.copy(final_src_path, final_dst_path)
            print(f"- Copying file: {final_src_path} -> {final_dst_path}")
        else:
            os.mkdir(final_dst_path)
            print(f"- Copying dir: {final_src_path} -> {final_dst_path}")
            copy_recursive(final_src_path, final_dst_path)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, item)

        if os.path.isfile(full_path):
            print(f"-> Convert --{full_path}-- to html")
            generate_page(full_path, template_path, os.path.join(dest_dir_path, item.replace(".md", ".html")))
        else:
            os.mkdir(os.path.join(dest_dir_path, item))
            generate_pages_recursively(full_path, template_path, os.path.join(dest_dir_path, item))


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as md_f:
        md_content = md_f.read()
        node = markdown_to_html_node(md_content)
        html_content = node.to_html()

        inline_converted = ""
        inline_nodes = text_to_textnodes(html_content)

        for node in inline_nodes:
            inline_converted += text_node_to_html_node(node).to_html()

        with open(template_path) as template:
            template_content = template.read()
            with_title = template_content.replace("{{ Title }}", extract_title(md_content))
            with_content = with_title.replace("{{ Content }}", inline_converted)

            with open(dest_path, "w") as dest:
                dest.write(with_content)

    
    