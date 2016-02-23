import sys
import os
from os import walk

digit_padding = 7
file_base = 'time_lapse_'
current_file = 1

if len(sys.argv) < 2:
    print 'Must supply file path as argument'
else:
    folder_path = str(sys.argv[1])
    f = []
    for (dirpath, dirnames, filenames) in walk(folder_path):
        for file in filenames:
            new_file_name = file_base + str(current_file).zfill(digit_padding) + '.' + file.split('.')[1]
            os.rename(folder_path + '/' + file, folder_path + '/' + new_file_name)
            current_file += 1
