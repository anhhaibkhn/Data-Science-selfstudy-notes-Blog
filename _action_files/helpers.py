import os


def getDirectoryList(path):
    """ Get all subfolders that contain jupyter notebooks """
    directoryList = []

    #return nothing if path is a file
    if os.path.isfile(path):
        return []

    #add dir to directorylist if it contains .ipynb files
    if len([f for f in os.listdir(path) if f.endswith('.ipynb')])>0:
        directoryList.append(path)

    for d in os.listdir(path):
        new_path = os.path.join(path, d)
        if os.path.isdir(new_path):
            directoryList += getDirectoryList(new_path)

    return directoryList


# if __name__=='__main__':
#     src_dir = os.getcwd() + '\_notebooks'
#     print(src_dir)
#     print(list( (f + '\\*.ipynb') for f in getDirectoryList(src_dir)))