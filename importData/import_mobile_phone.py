#! /usr/bin/env python
# coding:utf8

#INSERT INTO onethink323.wx_phone_range (province, city, phones, status) VALUES ('浙江', '嘉兴', '1896636', 0)

target_city = ['淮安', '漳州', '衡阳', '宜昌', '潍坊', '淄博', '济宁', '南阳', '许昌']
template = "INSERT INTO onethink323.wx_phone_range (province, city, phones, status) VALUES ('%s', '%s', '%s', 0)"
#1388920,移动号段,沈阳,辽宁

with open('data.txt') as data_file:

    out_data = open('result.txt', 'w')
    for mobile_range in data_file.readlines():
        fields_arr = mobile_range.split(',')
        province = fields_arr[3].strip()
        city = fields_arr[2]
        phone = fields_arr[0]

        if city in target_city:
            sql_statement = template % (province, city, phone)
            out_data.write(sql_statement + ';\n')

    out_data.close()
    pass

