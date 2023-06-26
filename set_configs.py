import os


class FileHandler:
    def __init__(self, dir_path, file_name, new_text_file):
        self.dir_path = dir_path
        self.file_name = file_name
        self.file_path = os.path.join(self.dir_path, self.file_name)
        self.new_text_file = new_text_file

    @staticmethod
    def get_current_dir() -> str or None:
        """
        Gets current working directory path.

        Returns:
            str or None: Current working directory path.
        """

        current_dir = os.getcwd()
        if os.path.isdir(current_dir):
            print(f"current_dir: {current_dir}")
            return current_dir
        else:
            print(f"get_current_dir() found no path.")
            return None



    @staticmethod
    def get_directory_permissions(dir_path: str) -> dict or None:
        """
        Gets directory permissions.

        Args:
            dir_path (str): path to directory.

        Returns:
            dict or None: Dictionary containing all permissions:
            {
                'Read': bool,
                'Write': bool,
                'Execute': bool,
            }
            Returns None if no such directory.
        """
        if not os.path.exists(dir_path):
            print(f"dir does not exist: {dir_path}")
            return

        permission_read = os.access(dir_path, os.R_OK)
        permission_write = os.access(dir_path, os.W_OK)
        permission_execute = os.access(dir_path, os.X_OK)

        permissions = {
            'Read': permission_read,
            'Write': permission_write,
            'Execute': permission_execute
        }

        return permissions


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



# paths can be relative based on where you execute from
current_dir = FileHandler.get_current_dir()

permissions = FileHandler.get_directory_permissions(current_dir)
if permissions:
    print(f"Permissions for: {current_dir}")
    for permission, value in permissions.items():
        print(f"{permission}: {value}")



# file_handler = FileHandler("my_dir", "my_file.txt", "new_text_file.txt")
# FileHandler.mkdir()
# file_handler.create_file()
# file_handler.append_text_from_file()
# file_handler.append_text_as_arg()
# file_handler.check_directory_permissions()
# file_handler.copy_file()

# define_root_dir("/animals")
# check_directory_permissions("/animals/")
# mkdir("/mammals/cats/")
# create_file("/mammals/cats/names.txt")
# append_text_from_file("/mammals/source_cat_names.txt", "/cats/names.txt")
# mkdir("/mammals/dogs/")
# create_file("/mammals/dogs/names.txt")
# append_text_as_arg("dogs are great right?", "/mammals/dogs/names.txt")
# copy_file(source_file_path/parrots.txt, dest_file_path/parrots.txt)
