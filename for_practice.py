from flask import Flask, request, render_template, jsonify, json
import MySQLdb
from types import *





def test():
        db =  MySQLdb.connect("127.0.0.1","root","","GroceryDB")
        cur = db.cursor()
        cur.execute("select s.city, p.category, t.year, sum(f.dollar_sales)"+
                                                        " AS total_sales from Product p, Time t, Store s,`sales_fact` f"+
                                                        " where p.product_key = f.product_key"+
                                                        " AND s.store_key = f.store_key"+
                                                        " AND t.time_key = f.time_key"+
                                                        " group by s.city, p.category, t.year order by t.year, s.city, p.category")
        

        r = [dict((cur.description[i][0], value) 
               for i, value in enumerate(row)) for row in cur.fetchall()]

        #results = cur.fetchall()
        field_names = [str(i[0]) for i in cur.description]
        print(field_names)
        jsonDUMPfromMysql = json.dumps(r)
        print (jsonDUMPfromMysql)
        list = [{'param': 'foo', 'val': 2},{'param': 'bar', 'val': 10}]
        print (list)

def main():
        test()
        





if  __name__ =='__main__':main()
