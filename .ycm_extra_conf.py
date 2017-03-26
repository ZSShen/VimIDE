import os
import os.path
import sys
import json
import ycm_core


YCM_PROJECT_FILENAME = 'ycm_project.json'

YCM_PROJECT_FILES = []
YCM_PROJECT_FLAGS = []


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

SYSTEM_NAME = os.uname()[0]

if SYSTEM_NAME == 'Darwin':
    SYSTEM_SPECIFIED_FLAGS = [
        '-I/usr/local/opt/openssl/include',
        '-I/usr/local/opt/qt5/include',
        '-I/usr/local/opt/icu4c/include',
        '-isystem', '/usr/local/Frameworks/Python.framework/Versions/3.6/Headers',
    ]
elif SYSTEM_NAME == 'Linux':
    SYSTEM_SPECIFIED_FLAGS = [
        '-I/usr/include/c++/5',
    ]
else:
    SYSTEM_SPECIFIED_FLAGS = []

BASE_FLAGS.extend(SYSTEM_SPECIFIED_FLAGS)


SOURCE_EXTENSIONS = [
    '.cpp',
    '.cxx',
    '.cc',
    '.c',
    '.m',
    '.mm'
]


HEADER_EXTENSIONS = [
    '.h',
    '.hxx',
    '.hpp',
    '.hh'
]


HEADER_PATHS = [
    'include',
    'inc',
    'headers'
]


def is_header_file(filename):
    extension = os.path.splitext(filename)[1]
    return extension in HEADER_EXTENSIONS


def is_header_path(path):
    name = os.path.basename(path)
    return name.lower() in HEADER_PATHS


def find_nearest_file(path, target):
    candidate = os.path.join(path, target)
    if(os.path.isfile(candidate)):
        return os.path.abspath(candidate)
    else:
        parent = os.path.dirname(os.path.abspath(path))
        if(parent == path):
            raise RuntimeError("Could not find " + target)
        return find_nearest_file(parent, target)


def process_ycm_project_include_flags(root, flags, traverse):
    if traverse is False:
        flag = '-I' + root
        if flag not in flags:
            flags.append(flag)

        return

    for dirroot, dirnames, filenames in os.walk(root):
        flag = '-I' + dirroot
        if flag in flags:
            continue

        if is_header_path(dirroot):
            flags.append(flag)
            continue

        for f in filenames:
            if is_header_file(f):
                temp = [flag]
                traverse_dir = dirroot

                while traverse_dir != root:
                    traverse_dir = os.path.dirname(traverse_dir)
                    flag = '-I' + traverse_dir
                    if is_header_path(traverse_dir):
                        temp = [] if flag in flags else [flag]
                        break
                    if flag in flags:
                        break
                    temp.append(flag)

                flags.extend(temp)
                break


def flags_for_ycm_project(root):
    global YCM_PROJECT_FILES
    global YCM_PROJECT_FLAGS

    try:
        ycm_project_file = find_nearest_file(root, YCM_PROJECT_FILENAME)

        if ycm_project_file in YCM_PROJECT_FILES:
            return YCM_PROJECT_FLAGS

        YCM_PROJECT_FILES.append(ycm_project_file)

        ycm_project_root = os.path.dirname(ycm_project_file)
        candidate_roots = []

        with open(ycm_project_file) as f:
            try:
                ycm_project_data = json.loads(f.read())
                include_field = ycm_project_data['include']
                if type(include_field) is list:
                    candidate_roots = include_field
                elif type(include_field) is str:
                    candidate_roots = [include_field]
                elif sys.version_info.major == 2:
                    if type(include_field) is unicode:
                        candidate_roots = [include_field]
            except:
                pass

        if not candidate_roots:
            candidate_roots = [ycm_project_root]

        for candidate_root in candidate_roots:
            traverse = True
            real_root = ''
            try:
                if type(candidate_root) is str:
                    real_root = candidate_root
                elif type(candidate_root) is dict:
                    real_root = candidate_root['path']
                    if 'deep' in candidate_root:
                        traverse = candidate_root['deep']
                elif sys.version_info.major == 2:
                    if type(candidate_root) is unicode:
                        real_root = candidate_root
                else:
                    continue

                if not os.path.isabs(real_root):
                    real_root = os.path.join(ycm_project_root, real_root)
            except:
                continue

            process_ycm_project_include_flags(real_root,
                                              YCM_PROJECT_FLAGS,
                                              traverse)

        return YCM_PROJECT_FLAGS
    except:
        return []


def get_compilation_info_for_file(database, filename):
    if is_header_file(filename):
        basename = os.path.splitext(filename)[0]
        for extension in SOURCE_EXTENSIONS:
            replacement_file = basename + extension
            if os.path.exists(replacement_file):
                compilation_info = database.get_compilation_info_for_file(
                    replacement_file)
                if compilation_info.compiler_flags_:
                    return compilation_info
        return None
    return database.get_compilation_info_for_file(filename)


def find_nearest(path, target):
    candidate = os.path.join(path, target)
    if(os.path.isfile(candidate) or os.path.isdir(candidate)):
        return candidate
    else:
        parent = os.path.dirname(os.path.abspath(path))
        if(parent == path):
            raise RuntimeError("Could not find " + target)
        return find_nearest(parent, target)


def make_relative_paths_in_flags_absolute(flags, working_directory):
    if not working_directory:
        return list(flags)
    new_flags = []
    make_next_absolute = False
    path_flags = ['-isystem', '-I', '-iquote', '--sysroot=']
    for flag in flags:
        new_flag = flag

        if make_next_absolute:
            make_next_absolute = False
            if not flag.startswith('/'):
                new_flag = os.path.join(working_directory, flag)

        for path_flag in path_flags:
            if flag == path_flag:
                make_next_absolute = True
                break

            if flag.startswith(path_flag):
                path = flag[len(path_flag):]
                new_flag = path_flag + os.path.join(working_directory, path)
                break

        if new_flag:
            new_flags.append(new_flag)
    return new_flags


def flags_for_clang_complete(root):
    try:
        clang_complete_path = find_nearest(root, '.clang_complete')
        clang_complete_flags = open(
            clang_complete_path, 'r').read().splitlines()
        return clang_complete_flags
    except:
        return None


def flags_for_include(root):
    try:
        include_path = find_nearest(root, 'include')
        flags = []
        for dirroot, dirnames, filenames in os.walk(include_path):
            for dir_path in dirnames:
                real_path = os.path.join(dirroot, dir_path)
                flags = flags + ["-I" + real_path]
        flags = flags + ["-I" + include_path]
        return flags
    except:
        return None


def flags_for_compilation_database(root, filename):
    try:
        compilation_db_path = find_nearest(root, 'compile_commands.json')
        compilation_db_dir = os.path.dirname(compilation_db_path)
        compilation_db = ycm_core.CompilationDatabase(compilation_db_dir)
        if not compilation_db:
            return None
        compilation_info = get_compilation_info_for_file(compilation_db,
                                                         filename)
        if not compilation_info:
            return None
        return make_relative_paths_in_flags_absolute(
            compilation_info.compiler_flags_,
            compilation_info.compiler_working_dir_)
    except:
        return None


def FlagsForFile(filename):
    root = os.path.realpath(filename)

    compilation_db_flags = flags_for_compilation_database(root, filename)
    if not compilation_db_flags:
        compilation_db_flags = flags_for_compilation_database(os.getcwd(),
                                                              filename)

    if compilation_db_flags:
        final_flags = compilation_db_flags
    else:
        final_flags = BASE_FLAGS
        ycm_project_flags = flags_for_ycm_project(root)
        if ycm_project_flags:
            final_flags = final_flags + ycm_project_flags
        else:
            clang_flags = flags_for_clang_complete(root)
            if clang_flags:
                final_flags = final_flags + clang_flags
            include_flags = flags_for_include(root)
            if include_flags:
                final_flags = final_flags + include_flags

    return {'flags': final_flags, 'do_cache': True}
