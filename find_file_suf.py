#!/usr/bin/env/python

# coding = utf-8\

import os

import string

from datetime import datetime

path = 'D:\\XXXX\\venv\\Report\\'

keyword = datetime.now().date().isoformat() + '_report.html'

target_file_path = ''

for file in os.listdir(path):

    print(os.path.splitext(file))

    if keyword == os.path.splitext(file)[0] + os.path.splitext(file)[1]:

        target_file_path = os.path.join(os.path.splitext(file)[0], os.path.splitext(file)[1])
