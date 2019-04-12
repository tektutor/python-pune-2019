#!/usr/bin/python3
import re

s = '''
    123-456-7890
    Hello World
    123.456.7890
    (123)-(456)-(9990)
    Hello Python
    (135)(552)(4523)
    This is a test sentence
    (444).(323).(6345)
'''

mobile_format1 = "\d{3}[-|.]\d{3}[-|.]\d{4}"
mobile_format2 = "[(]\d{3}[)][-|.|][(]\d{3}[)][-|.|][(]\d{4}[)]"
mobile_format3 = "[(]\d{3}[)][(]\d{3}[)][(]\d{4}[)]"

pattern = mobile_format1 + "|" + mobile_format2 + "|" + mobile_format3

mobile_format1 = re.compile ( pattern )

match = re.findall( mobile_format1, s )
print ( match )