import os
            
def renamer(dir_path):
    '''
    Renames jpeg files by replacing the spaces in the file names with underscores.
    dir_path (string): The path of the directory containing the jpeg files.
    '''
    try:
        file_names = os.listdir(dir_path)
        jpeg_files = [file for file in file_names if file[-5:] == ".jpeg"]
        
        for file_name in jpeg_files:
            src_name = os.path.join(dir_path, file_name) # Use join method to join two paths
            dest_name = os.path.join(dir_path, '_'.join(file_name.split())) # Splits on whitespace
            os.rename(src_name, dest_name)
            
        print("Done renaming {} jpeg files!".format(len(jpeg_files)))
        
    except FileNotFoundError:
        print('No such directory as {}!!!'.format(dir_path))


if __name__ == '__main__':
    # To get the path correctly, try placing the renamer.py file in the same
    # directory as the jpeg files and do:
    ### -> file_dir = os.getcwd() 
    # to get the current directory.
    file_dir = "/home/polo/Pictures/Delvis Photos/whiskey/m--->>"
    renamer(file_dir)