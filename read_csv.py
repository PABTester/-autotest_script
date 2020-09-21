#!/usr/bin/env python
# coding=utf-8

import codecs

import csv

from common.file_transcode import FileTransCode

def read_csv(path):

    path = FileTransCode(path, 'UTF-8').convert()

    try:

        with codecs.open(path, 'r', encoding='utf-8') as fp:

            fp_key = csv.reader(fp)  # 一行一行读取，返回一个迭代对象

            for csv_key in fp_key:

                # print('字典的key值：%s' % csv_key)

                csv_reader = csv.DictReader(fp, fieldnames=csv_key)

                print('DictReader()方法返回值：%s' % csv_reader)

                for row in csv_reader:

                    # print('-----读取每一行-----')

                    csv_dict = dict(row)

                    # print(csv_dict)

    except UnicodeDecodeError:

        with codecs.open(path, 'r', encoding='gb2312') as fp:

            fp_key = csv.reader(fp)  # 一行一行读取，返回一个迭代对象

            for csv_key in fp_key:

                # print('字典的key值：%s' % csv_key)

                csv_reader = csv.DictReader(fp, fieldnames=csv_key)

                print('DictReader()方法返回值：%s' % csv_reader)

                for row in csv_reader:

                    # print('-----读取每一行-----')

                    csv_dict = dict(row)

                    # print(csv_dict)

            return csv_dict
