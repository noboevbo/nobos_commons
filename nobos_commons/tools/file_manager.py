import os
import shutil
from distutils.dir_util import copy_tree
from typing import Dict

from nobos_commons.tools.log_handler import logger
from nobos_commons.utils.file_helper import is_filename_matching_regex, get_extension


def extract_files(source_dir: str, target_dir: str, regex: str = None):
    files = os.listdir(source_dir)
    for filename in files:
        if not is_filename_matching_regex(filename, regex):
            continue
        full_file_name = os.path.join(source_dir, filename)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, target_dir)


def transfer_files(src: str, dst: str, move_src_data: bool = False):
    """
    Copies or moves files recursively from one directory to another.
    :param src: source directory
    :param dst: target directory
    :param move_src_data: True if src should be moved, False if it should be copied
    """
    if move_src_data:
        logger.info('Move {0} to {1}'.format(src, dst))
        shutil.move(src, dst)
    else:
        logger.info('Copy {0} to {1}'.format(src, dst))
        copy_tree(src, dst)


def copy_folder_to_folder_indexed(source_dir: str, target_dir: str) -> Dict[str, str]:
    """
    Copies files from the source directory to target directory and names them after <index>.extension
    :param source_dir: source directory
    :param target_dir: target directory
    :return: Dictionary[OldFileName, NewFileName]
    """
    index_file_name_dic = dict()
    count = len([name for name in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, name))])

    files = os.listdir(source_dir)
    for file in files:
        source_path = os.path.join(source_dir, file)
        if os.path.isfile(source_path):
            target_path = os.path.join(target_dir, file)
            shutil.copy2(source_path, target_dir)
            indexed_file_name = str(count) + get_extension(file)
            os.rename(target_path, os.path.join(target_dir, indexed_file_name))
            count += 1
            index_file_name_dic[file] = indexed_file_name

    return index_file_name_dic


def copy_rename_file(source_file_path: str, target_dir: str, new_name: str) -> str:
    """
    Copys a given file to a given target directory and renames it.
    :param source_file_path: Path to the source file
    :param target_dir: Path to the target directory
    :param new_name: The new name of the file (without extension)
    :return: The full path to the new file
    """
    shutil.copy2(source_file_path, target_dir)
    target_path = os.path.join(target_dir, os.path.basename(source_file_path))
    new_file_name = new_name + get_extension(source_file_path)
    new_file_path = os.path.join(target_dir, new_file_name)
    os.rename(target_path, new_file_path)
    return new_file_path