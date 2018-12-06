import glob
import ntpath
import os
import re
import shutil
from typing import List, Dict


def is_filename_matching_regex(filename: str, regex: str) -> bool:
    if regex is None:
        return True
    pattern = re.compile(regex)
    return pattern.match(filename) is not None

def get_img_paths_from_folder(img_dir: str) -> List[str]:
    file_types = ['.png', '.jpg', '.PNG', '.JPG', '.JPEG']
    img_paths = []
    for file_type in file_types:
        img_search_string = os.path.join(img_dir, "*" + file_type)
        img_paths.extend(glob.glob(img_search_string))
    return img_paths


def get_img_paths_from_folder_recursive(img_dir: str) -> List[str]:
    img_paths = get_img_paths_from_folder(img_dir)
    for sub_dir in get_immediate_subdirectories(img_dir):
        print("Handle {}".format(sub_dir))
        img_paths += (get_img_paths_from_folder_recursive(sub_dir))
    return img_paths


def get_immediate_subdirectories(directory: str) -> List[str]:
    return [os.path.join(directory, name) for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]


def get_filenames_without_extension(file_dir: str) -> List[str]:
    filenames = []
    files = os.listdir(file_dir)
    for filename in files:
        filenames.append(get_filename_without_extension(filename))
    return filenames


def get_filename_from_path(file_path: str) -> str:
    return ntpath.basename(file_path)


def get_filename_without_extension(filename: str) -> str:
    return os.path.splitext(filename)[0]


def get_extension(filename: str) -> str:
    """
    Returns the extension from a filename / path
    :param filename: filename or file path to the file which extension is required
    :return: The files extension (with .)
    """
    return os.path.splitext(filename)[1]


def get_create_path(path: str) -> str:
    """
    Returns the given path, if it doesn't exist it creates it on file system
    :param path: The requested path
    :return: The requested path (which was created on file system if it doesn't exists)
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_pickle_filename_from_file_path(file_path: str) -> str:
    """
    Removes the extension of the given file path and replaces it with .pkl
    :param file_path: The path to the original file
    :return: The path to the pickle file which has the same name, but a .pkl extension
    """
    return os.path.join(os.path.abspath(file_path), get_filename_without_extension(file_path) + ".pkl")


def get_autoincremented_filepath(file_path: str) -> str:
    file_path = os.path.expanduser(file_path)

    if not os.path.exists(file_path):
        return file_path

    root, ext = os.path.splitext(os.path.expanduser(file_path))
    file_dir_path = os.path.dirname(root)
    filename = os.path.basename(root)
    candidate = filename + ext
    index = 0
    ls = set(os.listdir(file_dir_path))
    while candidate in ls:
        candidate = "{}_{}{}".format(filename, index, ext)
        index += 1
    return os.path.join(file_dir_path, candidate)
