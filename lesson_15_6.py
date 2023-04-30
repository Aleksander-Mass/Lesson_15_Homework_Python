# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ===   имя файла без расширения или название каталога,
# ===   расширение, если это файл,
# ===   флаг каталога,
# ===   название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.
import argparse
import os
import pathlib
from pathlib import Path
from collections import namedtuple
import logging

logging.basicConfig(filename="task_6.log", encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def get_info(directory_path: pathlib.Path):
    Object = namedtuple('Object', 'Name, Extension, IsCatalog, Parent')
    all_files = pathlib.Path(directory_path).glob('*')
    for file in all_files:
        if file.is_file():
            name = file.name.split('.')[0]
            extension = f".{file.name.split('.')[1]}" if str(file.name).count('.') == 1 else None
            catalog_flag = (os.stat(file).st_mode & 0o777)
            parent = str(file.parent).split('\\')[-1]
            to_write = Object._make([name, extension, catalog_flag, parent])
            logger.info(to_write)
        elif file.is_dir():
            name = file.name
            extension = None
            catalog_flag = (os.stat(file).st_mode & 0o777)
            parent = str(file.parent).split('\\')[-1]
            to_write = Object._make([name, extension, catalog_flag, parent])
            logger.info(to_write)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Path to directory on PC")
    parser.add_argument('--path', default=Path(os.getcwd()))
    args = parser.parse_args()
    path = args.path
    get_info(path)