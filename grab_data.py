#!/usr/bin/python

import os
from os import listdir
from cd import cd

ck_path = os.getcwd() + '/images/CK+/cohn-kanade-plus-images/'
with cd(ck_path):
    all_dir = os.listdir('.')
    for directory in all_dir: #S-level
        if directory[0] == '.':
            continue
        else:
            subdir_path = ck_path + directory + '/'
            with cd(subdir_path):
                all_subdirs = os.listdir('.') #0-level
                for subdir in all_subdirs:
                    if subdir[0] == '.':
                        continue
                    else:
                        img_level_path = subdir_path + subdir + '/'
                        with cd(img_level_path):
                            all_imgs = os.listdir('.')
                            last_img_path = img_level_path + all_imgs[-1]
                            print last_img_path
