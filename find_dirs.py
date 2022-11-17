import os

def descend_dirs(master_list, directory):
    """ look in the speceified directory, and find all the directories
    underneath it, returning the structure as a dict. """
    #print(f'in {directory}')
    dirs = find_dirs(directory)
    #print(f'found {dirs}')
    paths = {}
    for this_dir in dirs:
        #print(f'preparing to descend to {this_dir}')
        paths[this_dir] = descend_dirs(master_list, this_dir)
        if not paths[this_dir]:
            final_dir = os.path.split(this_dir)[1]
            master_list[final_dir] = this_dir
    return paths


def find_dirs(directory):
    """ get all the directories in the specified directory """
    # get all the files in this directory
    my_files = os.listdir(directory)
    #print(f'found these files in {directory}: {my_files}')

    # now find all the files which are actually directories
    my_dirs = []
    for name in my_files:
        name = os.path.join(directory, name)
        if os.path.isdir(name):
            my_dirs.append(name)

    return my_dirs

def main():
    master_list = {}
    all_dirs = descend_dirs(master_list, '.')
    #print(all_dirs)
    print(master_list)

if __name__ == '__main__':
    main()
