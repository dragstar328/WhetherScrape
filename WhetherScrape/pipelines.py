# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import json

class WhetherscrapePipeline(object):

    def __init__(self):
        f = open("db_setting.json")
        j = json.load(f)
        f.close
        
        u = j['user']
        p = j['passwd']
        h = j['host']
        d = j['db']
        
        self.con = MySQLdb.connect(
                     user=u,
                     passwd=p,
                     host=h,
                     db=d)
        self.cur = self.con.cursor()
        
        self.insert_sql = "INSERT INTO yohoutbl2 values(%s, %s, %s, %s)"
        self.delete_sql = "DELETE from yohoutbl2 WHERE key_hiduke = %s"

    def process_item(self, item, spider):
        print("*********** from pipeline ***********")
        n = item['body'][0]
        y = n[3:7]
        m = n[8:10]
        d = n[11:13]
        ymd1 = y + m + d
        
        print(y + m + d)
        
        n = item['body'][1]
        y = n[3:7]
        m = n[8:10]
        d = n[11:13]
        ymd2 = y + m + d
        
        print(y + m + d)
        
        n = item['body2'][0]
        y = n[4:8]
        m = n[9:11]
        d = n[12:14]
        ymd3 = y + m + d
        
        print(y + m + d)
        
        n = item['kion']
        kion_list1 = n[0:24]
        kion_list2 = n[24:48]
        kion_list3 = n[48:72]
        
        print(kion_list1)
        
        n = item['shitsudo']
        hum_list1 = n[0:24]
        print(hum_list1)
        
        n = item['shitsudo2']
        hum_list2 = n[0:24]
        hum_list3 = n[24:48]
        print(hum_list3)
        
        
        # today
        # select
        self.insertdb(ymd1, kion_list1, hum_list1)
        
        # tommorow
        self.insertdb(ymd2, kion_list2, hum_list2)
        
        # day after tommorow
        self.insertdb(ymd3, kion_list3, hum_list3)
        
        self.con.commit();
        self.cur.close
        self.con.close
        
        return item
        
    def insertdb(self, ymd, kion, hum):
        # delete
        self.cur.execute(self.delete_sql, (ymd,))
        
        for i in range(0,24):
            #insert
            tpl = (ymd, i+1, kion[i], hum[i])
            self.cur.execute(self.insert_sql, tpl)








