#coding=utf8
#! /usr/bin/env python

def odd(n):
    return n % 2

def double(n):
    return n*2

li = [1, 2, 3, 5, 9, 10, 256, -3]

newList = filter(odd, li)
print newList

li = [1, 2, 3, 5, 9, 10, 256, -3]

newList = map(double, li)
print newList

g = lambda item: item * 3

print map(g, li)