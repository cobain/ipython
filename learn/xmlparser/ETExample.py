#encoding=utf-8
from xml.etree import ElementTree as ET
#Ҫ�ҳ������˵�����
per=ET.parse('test.xml')
p=per.findall('./person')
for x in p:
    print x.attrib
print
for oneper in p:  #�ҳ�person�ڵ�
    for child in oneper.getchildren(): #�ҳ�person�ڵ���ӽڵ�
        print child.tag,':',child.text

    print 'age:',oneper.get('age')
    print '############'