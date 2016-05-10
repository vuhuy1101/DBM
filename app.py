#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify, get_template_attribute, json

# import mysql.connector
# from mysql.connector import Error

import MySQLdb
from types import *

app = Flask(__name__)
__timeDimensionHierarchy = ''
__productDimensionHierarchy = ''
__storeDimensionHierarchy = ''

@app.route('/')
def hello():
	return render_template('index.html')


# @app.rout('/test', methods = ['GET']
# def test():
	
@app.route('/loadOperations')
def loadOps():
	return render_template('operations.html')

@app.route('/getResults')
def getResults():
	
	db =  MySQLdb.connect("127.0.0.1","root","","GroceryDB")
	cur = db.cursor()

	#if isinstance(request.form['conceptTime'], basestring):
	#	__timeDimensionHierarchy = request.form['conceptTime']
	#if isinstance(request.form['conceptProduct'], basestring):
	#	__productDimensionHierarchy = request.form['conceptProduct']
	#if isinstance(request.form['conceptStore'], basestring):
	#	__storeDimensionHierarchy = request.form['conceptStore']
	if request.args.get('action') == "addDim":
		time = request.args.get('conceptTime')
		product = request.args.get('conceptProduct')
		store = request.args.get('conceptStore')
		action = request.args.get('action')
	else:
		global __timeDimensionHierarchy 
		global __productDimensionHierarchy
		global __storeDimensionHierarchy
		__timeDimensionHierarchy = request.args.get('conceptTime')
		__productDimensionHierarchy = request.args.get('conceptProduct')
		__storeDimensionHierarchy = request.args.get('conceptStore')

	print("results = " + __timeDimensionHierarchy)
	
	#if time dimension not selected
	# if not __timeDimensionHierarchy:
	# 	cur.execute("select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", sum(f.dollar_sales) "+
	# 		"AS total_sales from Product p, Store s,`sales_fact` f "+
	# 		"where p.product_key = f.product_key "+
	# 		"AND s.store_key = f.store_key "+
	# 		"group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+
	# 		" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy)
	
	if not __timeDimensionHierarchy and not __productDimensionHierarchy and not __storeDimensionHierarchy:
		# blank false statement
		cur.execute("select 'Please select a concept hierarchy'")

	elif not __productDimensionHierarchy and not __storeDimensionHierarchy: 
		select_stmt = "select t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Time t, `sales_fact` f "
		where_stmt = "where t.time_key = f.time_key "
		groupby_stmt = "group by t."+__timeDimensionHierarchy+" order by t."+__timeDimensionHierarchy
		
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
		#		"AS total_sales from Time t, `sales_fact` f "+
		#		"where t.time_key = f.time_key "+
		#		"group by t."+__timeDimensionHierarchy+
		#		" order by t."+__timeDimensionHierarchy)

	elif not __timeDimensionHierarchy and not __storeDimensionHierarchy:
		select_stmt = "select p."+__productDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Product p, `sales_fact` f "
		where_stmt = "where p.product_key = f.product_key "
		groupby_stmt = "group by p."+__productDimensionHierarchy+" order by p."+__productDimensionHierarchy
		
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select s."+__storeDimensionHierarchy+", sum(f.dollar_sales) "+
		#	"AS total_sales from Store s,`sales_fact` f "+
		#	"where s.store_key = f.store_key "+
		#	"group by s."+__storeDimensionHierarchy+
		#	" order by s."+__storeDimensionHierarchy)
	elif not __timeDimensionHierarchy:
		select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", sum(f.dollar_sales) AS total_sales"
		from_stmt = "from Product p, Store s,`sales_fact` f "
		where_stmt = "where p.product_key = f.product_key AND s.store_key = f.store_key "
		groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy
		
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", sum(f.dollar_sales) "+
		#	"AS total_sales from Product p, Store s,`sales_fact` f "+
		#	"where p.product_key = f.product_key "+
		#	"AND s.store_key = f.store_key "+
		#	"group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+
		#	" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy)
	elif not __storeDimensionHierarchy:
		select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Product p, Time t,`sales_fact` f "
		where_stmt = "where p.product_key = f.product_key AND t.time_key = f.time_key "
		groupby_stmt = "group by p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy
		
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
		#		"AS total_sales from Product p, Time t,`sales_fact` f "+
		#		"where p.product_key = f.product_key "+
		#		"AND t.time_key = f.time_key "+
		#		"group by p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+
		#		" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy)
	elif not __productDimensionHierarchy:
		select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Time t, Store s,`sales_fact` f "
		where_stmt = "where s.store_key = f.store_key AND t.time_key = f.time_key "
		groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy
		
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
		#		"AS total_sales from Time t, Store s,`sales_fact` f "+
		#		"where s.store_key = f.store_key "+
		#		"AND t.time_key = f.time_key "+
		#		"group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+
		#		" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy)

	

	else:
		select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
		where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
		groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy
		
			
			
			#cur.execute("select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
			#	"AS total_sales from Product p, Time t, Store s,`sales_fact` f "+
			#	"where p.product_key = f.product_key "+
			#	"AND s.store_key = f.store_key "+
			#	"AND t.time_key = f.time_key "+
			#	"group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+
			#	" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy)
	
	cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
	results = cur.fetchall()
	field_names = [str(i[0]) for i in cur.description]
	print(field_names)

	r = [dict((cur.description[i][0], value) 	
               for i, value in enumerate(row)) for row in results]
	jsonDUMPfromMysql = json.dumps(r)
	return jsonDUMPfromMysql
	

	# a="<table border='1'>" + "<tr>"
	# for column_heading in field_names:
	# 	a += "<th>"+ column_heading +"</th>"
	# a+= "</tr>"


	# for row in results:
	# 	i=0
	# 	a+="<tr>"
	# 	for column_heading in field_names:
	# 		insert_element = row[i]
	# 		a+="<td>"+str(insert_element)+"</td>"
	# 		i+=1
	# 	a+="</tr>"
	# return render_template('index.html',variable=a)




	# return (__timeDimensionHierarchy +" - "+ __productDimensionHierarchy +" -"+ __storeDimensionHierarchy)

@app.route("/test")
def test():
	db = MySQLdb.connect(host='127.0.0.1', user='root',
	 passwd='', db='GroceryDB')
	cur = db.cursor()
	
	output = request.args.get('q')
	print(output)
	
	cur.execute("select s.city, p.category, t.year, sum(f.dollar_sales)"+
		" AS total_sales from Product p, Time t, Store s,`sales_fact` f"+
		" where p.product_key = f.product_key"+
		" AND s.store_key = f.store_key"+
		" AND t.time_key = f.time_key"+
		" group by s.city, p.category, t.year order by t.year, s.city, p.category")
	
	results = cur.fetchall()
	field_names = [str(i[0]) for i in cur.description]
	print(field_names)
	

	a="<table border='1'>" + "<tr>"
	for column_heading in field_names:
		a += "<th>"+ column_heading +"</th>"
	a+= "</tr>"


	for row in results:
		i=0
		a+="<tr>"
		for column_heading in field_names:
			insert_element = row[i]
			a+="<td>"+str(insert_element)+"</td>"
			i+=1
		a+="</tr>"


	r = [dict((cur.description[i][0], value) 
               for i, value in enumerate(row)) for row in results]
	jsonDUMPfromMysql = json.dumps(r)
	return jsonDUMPfromMysql

	# tags = "<p>some text here</p>"
	# return render_template ('index.html',tags=tags)
	# return(a)
	return (a)

def connect():
	try:
		conn = MySQLdb.connect(host='localhost', user='root',
		 passwd='157b', db='grocerydb')
		if conn.is_connected():
			print 'Connected to MySQL database'
	except getopt.GetoptError, e:
		print e
	finally:
		conn.close()

if __name__ == '__main__':
	app.run(debug=True)
	connect()


