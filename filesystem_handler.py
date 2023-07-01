import os
import getpass
from pathlib import Path


class FilesystemHandler:
    """Utility class for handling filesystem object operations."""

    def __init__(self):
        self.script_dir = self.get_script_dir()
        self.home_dir = self.get_home_dir()

    def get_script_dir(self) -> str:
        """returns current script file path."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        print(f"script_dir: {script_dir}")
        return script_dir

    def get_home_dir(self) -> str or None:
        """returns os agnostic home dir."""
        whoami = getpass.getuser()
        home_dir = os.path.expanduser("~" + whoami)
        return home_dir

    def mkdir(self, dir_path: list):
        """
        Creates directory at defined path, if doesn't exist.

        Args:
            dir_path: a list of each folder name in directory path.
        """
        if not Path(*dir_path).exists():

            # * unpacking operator (splat) unpacks list elements, then passes them as separate args to os.path.join().
            # this allows os.path.join() to handle linux and windows paths!
            full_dir_path = os.path.join(*dir_path)

            print(f"mkdir: {full_dir_path}")
            os.makedirs(full_dir_path)
        else:
            full_dir_path = os.path.join(*dir_path)
            print(f"full_dir_path already exists: {full_dir_path}")

    def touch(self, dir_path: list, filename: str):
        """
        creates new file at given path, if doesn't exist.

        Args:
            dir_path: a list of each folder name in directory path.
            filename: filename you want.
        """
        
        # concat list to existing list prior to splat operation
        file_path = dir_path + [filename]
        full_file_path = Path(*file_path)

        if not full_file_path.exists():
            full_file_path.touch()
            print(f"touch: {full_file_path}")
        else:
            print(f"full_file_path already exists: {full_file_path}")

    def copy_from_source_txt_into_destination_file(
        self, source_filename: str, destination_dir: list, destination_filename: str
    ):
        """
        Reads content of the source file. And then reads content of destination file.
        
        If source is not found in destination, it adds it in. It's like the IN operator.

        Args:
            source_filename: source filename.
            destination_dir: a list of each folder name in destination directory path.
            destination_filename: destination filename.
        """
        
        # read content from source file
        source_path = os.path.join(self.script_dir, "source", source_filename)
        with open(source_path, 'r') as source_f:
            source_content = source_f.read()

        # read content from destination file
        destination_path = os.path.join(*destination_dir, destination_filename)
        with open(destination_path, 'r') as dest_f:
            destination_content = dest_f.read()
        
        # check if source content already in destination file
        if source_content not in destination_content:
            # if not, append it in
            with open(destination_path, 'a') as destination:
                destination.write(source_content)
            print(f"contents copied\n\tfrom '{source_path}'\n\tto   '{destination_path}'.")
        else:
            print("source content already exists in the destination file.")
            
 

fs_handler = FilesystemHandler()
home_dir = fs_handler.home_dir

# handle cats/example.txt
new_dir = [home_dir, "cats"]
fs_handler.mkdir(new_dir)
filename = "example.txt"
fs_handler.touch(new_dir, filename)
fs_handler.copy_from_source_txt_into_destination_file(
    "cat_names.txt", new_dir, filename
)

# handle dogs/example.txt
new_dir = [home_dir, "dogs", "and", "more"]
fs_handler.mkdir(new_dir)
filename = "example.txt"
fs_handler.touch(new_dir, filename)
fs_handler.copy_from_source_txt_into_destination_file(
    "dog_names.txt", new_dir, filename
)
