import os


class FileHandler:
    def __init__(self, dir_path, file_name, new_text_file):
        self.dir_path = dir_path
        self.file_name = file_name
        self.file_path = os.path.join(self.dir_path, self.file_name)
        self.new_text_file = new_text_file
 
    def mkdir(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
    
    def create_file(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                pass
    
    def append_text_from_file(self):
        with open(self.new_text_file, "r") as new_text_file:
            new_text = new_text_file.read().strip()
        
        with open(self.file_path, "a+") as file:
            file.seek(0)
            content = file.read()
            if new_text and new_text not in content:
                file.write(f"{new_text}\n")

    def append_text_as_arg(self, new_text):
        with open(self.file_path, "a+") as file:
            file.seek(0)
            content = file.read()
            if new_text not in content:
                file.write(f"{new_text}\n")

    def copy_file(self, source_file_path, dest_file_path):
        if not os.path.exists(dest_file_path):
            os.path.copy2(source_file_path, dest_file_path)

    def check_directory_permissions(self):
        if not os.path.exists(self.dir_path):
            print(f"dir does not exist: {self.dir_path}")
            return

        permission_read = os.access(self.dir_path, os.R_OK)
        permission_write = os.access(self.dir_path, os.W_OK)
        permission_execute = os.access(self.dir_path, os.X_OK)

        # fancy f-strings
        print(f"Permissions for: {self.dir_path}")
        print(f"Read: {'Yes' if permission_read else 'No'}")
        print(f"Write: {'Yes' if permission_write else 'No'}")
        print(f"Execute: {'Yes' if permission_execute else 'No'}")


# TODO: how to best structure code? staticmethods?
file_handler = FileHandler("my_dir", "my_file.txt", "new_text_file.txt")
file_handler.mkdir()
file_handler.create_file()
file_handler.append_text_from_file()
file_handler.append_text_as_arg()
file_handler.check_directory_permissions()
file_handler.copy_file()

# define_root_dir("/animals")
# check_directory_permissions("/animals/")
# mkdir("/mammals/cats/")
# create_file("/mammals/cats/names.txt")
# append_text_from_file("/mammals/source_cat_names.txt", "/cats/names.txt")
# mkdir("/mammals/dogs/")
# create_file("/mammals/dogs/names.txt")
# append_text_as_arg("dogs are great right?", "/mammals/dogs/names.txt")
# copy_file(source_file_path/parrots.txt, dest_file_path/parrots.txt)
