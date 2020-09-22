#!/usr/bin/env python
# coding=utf-8

import codecs

def read_txt(path):

    txt_list = []

    with codecs.open(path, 'r', 'utf-8') as config:

        for line in config.readlines():

            # 遍历文件中每一行并以“;”分隔，再做列表解析，使用for循环去掉换行符,并以列表形式返回

            result = [ele.strip() for ele in line.split(';', 1)]

            # 先使用dict()将嵌套列表'[result]'转换成字典，再使用update更新字典

            # txt_dict.update(dict([result]))

        return txt_list

def write_txt(content):

    path = 'D:\Rabp\config\mcht_name.txt'

    with codecs.open(path,'a+','utf-8') as fp:

        fp.write(content+";")

if __name__ == "__main__":

    contents = ['11','22']

    for content in contents:

        write = write_txt(content)
