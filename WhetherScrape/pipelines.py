# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
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
        
        self.con = pymysql.connect(
                     user=u,
                     passwd=p,
                     host=h,
                     db=d,
                     use_unicode=True,
                     charset="utf8")
        self.cur = self.con.cursor()
        
        self.insert_sql = "INSERT INTO yohoutbl2 values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
        
        n = item['wheather']
        whether_list1 = n[0:24]
        whether_list2 = n[24:48]
        whether_list3 = n[48:72]
        print(whether_list1)
        
        n = item['prob_precip']
        prob_precip_list1 = n[0:24]
        prob_precip_list2 = n[24:48]
        prob_precip_list3 = n[48:72]
        print(prob_precip_list1)
        
        n = item['precipitation']
        precipitation_list1 = n[0:24]
        precipitation_list2 = n[24:48]
        precipitation_list3 = n[48:72]
        print(precipitation_list1)
        
        n = item['wind_blow']
        wind_blow_list1 = n[0:24]
        n = item['wind_blow2']
        wind_blow_list2 = n[0:24]
        wind_blow_list3 = n[24:48]
        print(wind_blow_list1)
        
        n = item['wind_speed']
        wind_speed_list1 = n[0:24]
        wind_speed_list2 = n[24:48]
        wind_speed_list3 = n[48:72]
        print(wind_speed_list1)
        
        # today
        # select
        self.insertdb(ymd1, kion_list1, hum_list1, whether_list1, prob_precip_list1, precipitation_list1, wind_blow_list1, wind_speed_list1)
        
        # tommorow
        self.insertdb(ymd2, kion_list2, hum_list2, whether_list2, prob_precip_list2, precipitation_list2, wind_blow_list2, wind_speed_list2)
        
        # day after tommorow
        self.insertdb(ymd3, kion_list3, hum_list3, whether_list3, prob_precip_list3, precipitation_list3, wind_blow_list3, wind_speed_list3)
        
        self.con.commit();
        self.cur.close
        self.con.close
        
        return item
        
    def insertdb(self, ymd, kion, hum, whether, prob_prec, precip, wind_blow, wind_speed ):
        # delete
        self.cur.execute(self.delete_sql, (ymd,))
        
        for i in range(0,24):
            #insert
            tpl = (ymd, i+1, kion[i], hum[i], whether[i], prob_prec[i], precip[i], wind_blow[i], wind_speed[i])
            self.cur.execute(self.insert_sql, tpl)








