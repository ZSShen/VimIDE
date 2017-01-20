import os
import ycm_core


YCM_EXTRA_CONF = ".ycm_extra_conf.py"


BASE_FLAGS = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-Wno-long-long',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-DNDEBUG',
    '-std=c++14',
    '-xc++',

    '-I/usr/lib',
    '-I/usr/include',
    '-I/usr/local/lib',
    '-I/usr/local/inlude',
]


def FindProjctRoot(curr):
    path_conf = os.path.join(curr, YCM_EXTRA_CONF)
    if os.path.isfile(path_conf):
        return curr
    if curr == os.path.join("/"):
        raise RuntimeError("Can not find the YCM configuration.")
    parent = os.path.dirname(curr)
    return FindProjctRoot(parent)


def ScanProjectFlags(curr):
    root = FindProjctRoot(curr)
    flags = []
    for dir_root, dir_names, file_names in os.walk(root):
        for dir_name in dir_names:
            dir_path = os.path.join(dir_root, dir_name)
            flags += ['-I' + dir_path]
    flags += ['-I' + root]
    return flags


def FlagsForFile(filename):
    final_flags = BASE_FLAGS

    start = os.path.dirname(os.path.abspath(filename))
    extended_flags = ScanProjectFlags(start)
    final_flags += extended_flags

    return {'flags': final_flags}
