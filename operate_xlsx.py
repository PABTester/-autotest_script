#!/usr/bin/env python
# coding: utf-8

import xlrd,inspect,xlutils.copy,openpyxl

from common.get_log import get_log

class Read_Excel():

    def __init__(self,path,log_style='console'):

        self.path = path

        self.log_style = log_style

    def read_excel_dict(self, sheet):

        """

        根据sheet_name读取除第一行外所有行，并以字典返回

        {'mcht_name': ['营业名称1234567890', '营业名称1234567891', '营业名称1234567892']}

        :param sheet:

        :return:

        """

        with xlrd.open_workbook(self.path, 'rb') as book:

            table = book.sheet_by_name(sheet)  # 找到sheet页

            # 获取总行数总列数

            row_num = table.nrows

            key = table.row_values(0)  # 这是第一行数据,返回一个列表，作为字典的key值

            if row_num <= 1:

                print('excel为空')

            else:

                result = {}

                xlsx_list = []

                for i in range(row_num):  # 有多少行，读多少次

                    values = table.row_values(i) # 获取第i行的值,首行是0

                    if i == 0:

                        key = values[0]

                        continue

                    xlsx_list.extend(values)

                result[key] = xlsx_list

                return result

    def read_excel_row(self, sheet, row):

        """

        根据sheetName读取指定行，并以字典返回

        {'mchtName': '目标商户名称', 'licenseNo': '41315204MHB1W68B5P', 'businessScope': '经营范围'}

        :param sheet:

        :param row:

        :return:

        """

        with xlrd.open_workbook(self.path, 'rb') as book:

            table = book.sheet_by_name(sheet)  # 找到sheet页

            # 获取总行数总列数

            row_num = table.nrows

            col_num = table.ncols

            key = table.row_values(0)  # 这是第一行数据,返回一个列表，作为字典的key值

            if row_num <= 1:

                print('excel为空')

            else:

                xlsx_dict = {}

                values = table.row_values(row)

                for x in range(col_num):  # 有多少列，赋值多少次

                    # 把key值对应的value赋值给key，每行循环一次

                    xlsx_dict[key[x]] = values[x]

                # 把字典添加到列表中

                # xlsx_list.append(xlsx_dict)

                return xlsx_dict

    def read_excel_rows(self, row):

        """

        根据指定行，读取所有sheet并以嵌套字典返回

        {'config': {'env': 'uat', 'log_style': 'console'},

        'first_page': {'mchtType': '1', 'businessType': '0100', 'tradeType': '1010'},

        """

        logger = get_log(inspect.stack()[0][3],style=self.log_style)

        with xlrd.open_workbook(self.path, 'rb') as book:

            sheets = book.sheet_names()

            data_dict = {}

            for sheet in sheets:

                table = book.sheet_by_name(sheet)  # 找到sheet页

                # 获取总行数总列数

                row_num = table.nrows

                col_num = table.ncols

                key = table.row_values(0)  # 这是第一行数据,返回一个列表，作为字典的key值

                xlsx_dict = {}

                if row_num <= 1:

                    logger.info('excel为空')

                else:

                    try:

                        values = table.row_values(row)

                        for x in range(col_num):  # 有多少列，赋值多少次

                            # 把key值对应的value赋值给key，每行循环一次

                            xlsx_dict[key[x]] = values[x]

                    # 把字典添加到列表中

                    except Exception as msg:

                        logger.info(msg)

                        logger.info('excel中每个sheet行数不一致')

                data_dict[sheet]=xlsx_dict

            return data_dict

    def read_max_row(self):

        logger = get_log(inspect.stack()[0][3],style=self.log_style)

        with xlrd.open_workbook(self.path, 'rb') as book:

            sheets = book.sheet_names()

            row_num0 = book.sheet_by_name('eighth_page').nrows

            for sheet in sheets:

                table = book.sheet_by_name(sheet)

                row_num = table.nrows

                if row_num0 != row_num:

                    content = sheet + "只有%s"%(row_num) + "行,eighth_page有%s" %(row_num0) + "行，请重新设置"

                    logger.info(content)

                    break

                else:

                    return int(row_num)

    def read_excel_dicts(self):

        # book = xlrd.open_workbook(path)  # 打开excel表

        with xlrd.open_workbook(self.path, 'rb') as book:

            sheets = book.sheet_names()

            excel_list = []

            for sheet in sheets:

                table = book.sheet_by_name(sheet)

                # 获取总行数总列数

                row_num = table.nrows

                col_num = table.ncols

                excel_dict = {}

                xlsx_list = []

                if row_num <= 1:

                    print('excel为空')

                else:

                    key = table.row_values(0)  # 这是第一行数据,返回一个列表，作为字典的key值

                    j = 1  # 从第二行开始获取值

                    for i in range(row_num-1):  # 有多少行，读多少次

                        xlsx_dict = {}

                        values = table.row_values(j)

                        for x in range(col_num):  # 有多少列，赋值多少次

                            # 把key值对应的value赋值给key，每行循环一次

                            xlsx_dict[key[x]] = values[x]

                        j = j + 1

                        # 把字典添加到列表中

                        xlsx_list.append(xlsx_dict)

                excel_dict[sheet] = xlsx_list

                excel_list.append(excel_dict)

            return excel_list

class Write_Excel():

    def __init__(self,path,log_style):

        self.path = path

        self.log_style = log_style

    def write_excel(self,sheet_name,content):

        # 列数从1开始，行数从1开始，首行首列都是1

        logger = get_log(inspect.stack()[0][3],style=self.log_style)

        wb = openpyxl.load_workbook(self.path)

        ws = wb.get_sheet_by_name(sheet_name)

        row_num = ws.max_row

        print(row_num)

        try:

            ws.cell(row=row_num+1,column=1).value=content

        except Exception as msg:

            logger.info(msg)

        finally:

            wb.save(self.path)

    def delete_excel(self,sheet_name,row=2):

        """

        删除指定sheet的指定行,默认删除第二行，有多少行，删除多少次

        :return:

        """

        wb =  .load_workbook(self.path)

        ws = wb.get_sheet_by_name(sheet_name)

        row_num = ws.max_row

        for i in range(row_num):

            ws.delete_rows(row) # 删除第row行数据

        wb.save(self.path)

if __name__ == '__main__':

    # path = 'D:\XXXX\config\\rabp_new_mcht.xlsx'

    path = r'D:\XXXX\config\rabp_capital.xlsx'

    log_style = 'console'

    EX = Read_Excel(path,log_style)

    # excel_data = EX.read_excel_rows(row=1)

    # print(excel_data)

    # row_max = EX.read_max_row()

    content = '营业名称1234567891'

    WT = Write_Excel(path,log_style)

    # WT.write_excel('mcht_name',content)

    result = EX.read_excel_dict('mcht_name')

    print(result)

    # result = EX.read_excel_row('capital',row=1)

    # WT.delete_excel('mcht_name')
