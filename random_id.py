#!/usr/bin/env/python
# coding = utf-8

import random,time

class IdNumber(str):

    def __init__(self, id_number):

        super(IdNumber, self).__init__()

        self.id = id_number

    def get_check_digit(self):

        """通过身份证号获取校验码"""

        check_sum = 0

        for i in range(0, 17):

            check_sum += ((1 << (17 - i)) % 11) * int(self.id[i])

        check_digit = (12 - (check_sum % 11)) % 11

        return check_digit if check_digit < 10 else "X"

    @classmethod

    def generate_myid(cls):

        generate_ids = []

        # 随机生成一个区域码(6位数)

        area_code = "412826"

        # 限定出生日期范围(8位数)

        birth_day = str(int(time.strftime('%Y%m%d',time.localtime()))-20000)

        # 顺序码(2位数)

        for i in range(100):

            sort_no = f"{i:02d}"

            for j in [x for x in range(10) if x % 2 != 0]:

                sex = j

                prefix = f"{area_code}{birth_day}{sort_no}{sex}"

                valid_bit = str(cls(prefix).get_check_digit())

                generate_ids.append(f"{prefix}{valid_bit}")

        return random.choice(generate_ids)

if __name__ == "__main__":

    randomID = IdNumber.generate_myid()

    print(randomID)
