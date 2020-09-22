#!/usr/bin/env python
# coding: utf-8

import chardet, sys

class FileTransCode:

    def __init__(self, path, dst_code):

        """

        :param path: 文件路径

        :param dst_code: 要转换的文件目标编码

        """

        self.path = path

        self.dst_code = dst_code

    def get_encoding(self):

        # 二进制方式读取，获取字节数据，检测文件编码类型

        with open(self.path, 'rb') as fp:

            data = fp.read()

            if chardet.detect(data)['encoding'] is not None:

                return chardet.detect(data)['encoding']

            else:

                print("无法判断文件编码类型，程序执行中止")

                sys.exit()

    def convert(self):

        code = str(self.get_encoding())

        if code == self.dst_code:  # 无需转换

            pass

            print('是目标编码，无需转换：', self.dst_code)

        elif code == 'GB2312':

            print('转换为GB2312')

            with open(self.path, 'wb') as fp:

                # 获取文件内容并转码

                new_content = fp.read().decode('GB2312', 'ignore').encode(self.dst_code)

                fp.write(new_content)  # 返回的是写入的字符长度

                return self.path

        elif code == 'GBK':

            print('转换为GBK')

            with open(self.path, 'wb') as fp:

                # 获取文件内容并转码

                new_content = fp.read().decode('GBK', 'ignore').encode(self.dst_code)

                fp.write(new_content)  # 返回的是写入的字符长度

                return self.path

        elif code == 'Unicode':

            print('转换为Unicode')

            with open(self.path, 'wb') as fp:

                # 获取文件内容并转码

                new_content = fp.read().decode('Unicode', 'ignore').encode(self.dst_code)

                fp.write(new_content)  # 返回的是写入的字符长度

                return self.path

        elif code == 'Ansi':

            print('转换为Ansi')

            with open(self.path, 'wb') as fp:

                # 获取文件内容并转码

                new_content = fp.read().decode('Ansi', 'ignore').encode(self.dst_code)

                fp.write(new_content)  # 返回的是写入的字符长度

                return self.path

        elif code == 'UTF-8':

            print('转换为UTF-8')

            with open(self.path, 'wb') as fp:

                # 获取文件内容并转码

                new_content = fp.read().decode('UTF-8', 'ignore').encode(self.dst_code)

                fp.write(new_content)  # 返回的是写入的字符长度

                return self.path

        elif code is None:

            print('转换为UTF-8')

            with open(self.path, 'wb') as fp:

                # 获取文件内容并转码

                new_content = fp.read().decode('UTF-8', 'ignore').encode(self.dst_code)

                fp.write(new_content)  # 返回的是写入的字符长度

                return self.path

        """

                with codecs.open(self.path, 'rb') as fp:

            content = fp.read()

            try:

                content.decode('utf-8').encode('utf-8')

                source_encoding = 'utf-8'

                print("utf-8")

                return source_encoding

            except UnicodeDecodeError:

                try:

                    content.decode('gbk').encode('utf-8')

                    source_encoding = 'gbk'

                    return source_encoding

                except UnicodeDecodeError:

                    try:

                        content.decode('gb2312').encode('utf-8')

                        source_encoding = 'gb2312'

                        return source_encoding

                    except UnicodeDecodeError:

                        try:

                            content.decode('gb18030').encode('utf-8')

                            source_encoding = 'gb18030'

                            return source_encoding

                        except UnicodeDecodeError:

                            try:

                                content.decode('big5').encode('utf-8')

                                source_encoding = 'gb18030'

                                return source_encoding

                            except UnicodeDecodeError:

                                content.decode('cp936').encode('utf-8')

                                source_encoding = 'cp936'

                                return source_encoding

        """

if __name__ == '__main__':

    path0 = 'D:\\XXXX\\test_file\\element.csv'

    A = FileTransCode(path0, 'UTF-8')

    print(A.get_encoding())

    new_file = A.convert()

    print(new_file)
