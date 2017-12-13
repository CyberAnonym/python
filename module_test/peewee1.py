#!/usr/bin/python
#coding:utf-8

#导入模块
import peewee

#建立连接
connect  = peewee.MySQLDatabase(
    database = 'sophiroth',
    host = 'localhost',
    user = 'alvin',
    passwd = 'alvin'
    )
#创建表
    #类名必须大写

class sophia(peewee.Model):
    name = peewee.CharField(max_length=32) #name char (32)
    age = peewee.IntegerField() #int
    birthday = peewee.DateTimeField()  #日期

    class Meta:
        database = connect
if __name__ == '__main__':
    sophia.create_table()