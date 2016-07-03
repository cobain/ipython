#-*- coding:utf-8 -*-
from xml.etree import ElementTree
def print_node(node):
    '''��ӡ��������Ϣ'''
    print "=============================================="
    print "node.attrib:%s" % node.attrib
    if node.attrib.has_key("age") > 0 :
        print "node.attrib['age']:%s" % node.attrib['age']
    print "node.tag:%s" % node.tag
    print "node.text:%s" % node.text
def read_xml(text):
    '''��xml�ļ�'''
    # ����XML�ļ���2�ַ���,һ�Ǽ���ָ���ַ��������Ǽ���ָ���ļ���    
    # root = ElementTree.parse(r"D:/test.xml")
    root = ElementTree.fromstring(text)
    
    # ��ȡelement�ķ���
    # 1 ͨ��getiterator 
    lst_node = root.getiterator("person")
    for node in lst_node:
        print_node(node)
        
    # 2ͨ�� getchildren
    lst_node_child = lst_node[0].getchildren()[0]
    print_node(lst_node_child)
        
    # 3 .find����
    node_find = root.find('person')
    print_node(node_find)
    
    #4. findall����
    node_findall = root.findall("person/name")[1]
    print_node(node_findall)
    
if __name__ == '__main__':
     read_xml(open("test.xml").read())