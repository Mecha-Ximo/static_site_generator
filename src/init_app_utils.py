import os
import shutil

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