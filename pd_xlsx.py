#!/usr/bin/env/python
# coding = utf-8

import pandas as pd

from pandas import read_excel

def pand_read_excel(path,sheet_name):

    excel = pd.read_excel(io=path,sheet_name=sheet_name)

    keys = list(excel.keys())

    print(keys)

if __name__ == '__main__':

    pand_read_excel(path='D:\XXXX\config\\rabp_new_mcht.xlsx',sheet_name='first_page')
