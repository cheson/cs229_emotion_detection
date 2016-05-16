#!/usr/bin/python

import os
from os import listdir
from cd import cd

ck_path = os.getcwd() + '/images/CK+/cohn-kanade-plus-images/'
with cd(ck_path):
    all_dir = os.listdir('.')
    for directory in all_dir:
        if directory[0] == '.':
            continue
        else:
            subdir_path = ck_path + directory + '/'
            with cd(subdir_path):
                all_images = os.listdir('.')
                img_path = subdir_path+all_images[-1]
                print img_path
