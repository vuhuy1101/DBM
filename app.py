#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, jsonify, get_template_attribute, json
import string

# import mysql.connector
# from mysql.connector import Error

import MySQLdb
from types import *

app = Flask(__name__)
__timeDimensionHierarchy = ""
__productDimensionHierarchy = ""
__storeDimensionHierarchy = ""
action = ""
query_adder = ""


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
	db =  MySQLdb.connect("127.0.0.1","root","157b","GroceryDB")
	#db =  MySQLdb.connect("127.0.0.1","root","0309","GroceryDB")
	cur = db.cursor()

	#if isinstance(request.form['conceptTime'], basestring):
	#	__timeDimensionHierarchy = request.form['conceptTime']
	#if isinstance(request.form['conceptProduct'], basestring):
	#	__productDimensionHierarchy = request.form['conceptProduct']
	#if isinstance(request.form['conceptStore'], basestring):
	#	__storeDimensionHierarchy = request.form['conceptStore']
	if request.args.get('action') == "addDim" or request.args.get('action') == "removeDim" or request.args.get('action') == "rollup" or request.args.get('action') == "drilldown" or request.args.get('action') == "slice" or request.args.get('action') == "dice":
		time = request.args.get('conceptTime')
		product = request.args.get('conceptProduct')
		store = request.args.get('conceptStore')
		havingby = request.args.get('val0')
		timehavingby1 = request.args.get('val1')
		timehavingby2 = request.args.get('val2')
		producthavingby1 = request.args.get('val3')
		producthavingby2 = request.args.get('val4')
		storehavingby1 = request.args.get('val5')
		storehavingby2 = request.args.get('val6')
		global action
		action = request.args.get('action')
	#elif request.args.get('action') is not None:
	else:
		global __timeDimensionHierarchy 
		global __productDimensionHierarchy
		global __storeDimensionHierarchy
		global action
		global query_adder
		query_adder = ""
		__timeDimensionHierarchy = request.args.get('conceptTime')
		__productDimensionHierarchy = request.args.get('conceptProduct')
		__storeDimensionHierarchy = request.args.get('conceptStore')
		action = ""
		havingby_stmt = ""
	
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
		if action == "rollup":
			if time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
		elif action == "drilldown":
			if time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
		select_stmt = "select t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Time t, `sales_fact` f "
		where_stmt = "where t.time_key = f.time_key "
		groupby_stmt = "group by t."+__timeDimensionHierarchy
		havingby_stmt = ""
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
		#		"AS total_sales from Time t, `sales_fact` f "+
		#		"where t.time_key = f.time_key "+
		#		"group by t."+__timeDimensionHierarchy+
		#		" order by t."+__timeDimensionHierarchy)
		if action == "slice":
			if time:
				havingby_stmt = (" Having t."+time+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
		elif action == "dice":
			havingby_stmt = " Having ( t."+time+ " = "+ timehavingby1 + " or t."+time+"=" + timehavingby2 + ")" 
		elif action == "addDim":
			if time: 
				query_adder += (", t."+time)
				select_stmt = "select t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+ query_adder + " order by t."+__timeDimensionHierarchy+query_adder
			elif product: 
				query_adder += (", p."+product)
				# select_stmt = "select p."+product+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
				# from_stmt = "from Time t, Product p, `sales_fact` f "
				# where_stmt = " where t.time_key = f.time_key AND p.product_key = f.product_key "
				# groupby_stmt = "group by t."+__timeDimensionHierarchy+", p."+product+" order by t."+__timeDimensionHierarchy+", p."+product
				select_stmt = "select t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+ __timeDimensionHierarchy + query_adder + " order by t."+__timeDimensionHierarchy + query_adder

			elif store: 
				query_adder += (", s."+store)
				select_stmt = "select t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+ __timeDimensionHierarchy + query_adder + " order by t."+__timeDimensionHierarchy + query_adder
		elif action == "removeDim":
			if time: 
				#remove t.time from query_adder
				query_deleter = string.replace(query_adder,', t.'+time, '')
				query_adder = query_deleter
				select_stmt = "select t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+ query_adder + " order by t."+__timeDimensionHierarchy+query_adder
			elif product: 
				query_deleter = string.replace(query_adder,', p.'+product, '')
				query_adder = query_deleter
				select_stmt = "select t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+ query_adder + " order by t."+__timeDimensionHierarchy+query_adder
			elif store: 
				query_deleter = string.replace(query_adder,', s.'+store, '')
				query_adder = query_deleter
				select_stmt = "select t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+ query_adder + " order by t."+__timeDimensionHierarchy+query_adder


			
			
	elif not __timeDimensionHierarchy and not __storeDimensionHierarchy:
		if action == "rollup":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
		elif action == "drilldown":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
		select_stmt = "select p."+__productDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Product p, `sales_fact` f "
		where_stmt = "where p.product_key = f.product_key "
		groupby_stmt = "group by p."+__productDimensionHierarchy
		havingby_stmt = ""
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select s."+__storeDimensionHierarchy+", sum(f.dollar_sales) "+
		#	"AS total_sales from Store s,`sales_fact` f "+
		#	"where s.store_key = f.store_key "+
		#	"group by s."+__storeDimensionHierarchy+
		#	" order by s."+__storeDimensionHierarchy)
		if action == "slice":
			if product:
				havingby_stmt = (" Having p."+product+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
		elif action == "dice":
			havingby_stmt = "Having \( p."+product+ "="+ producthavingby1 + "or" + producthavingby2 + "\)" 
		elif action == "addDim":
			if time: 
				query_adder += (", t."+time)
				select_stmt = "select p."+__productDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by p."+__productDimensionHierarchy+ query_adder +" order by p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_adder += (", p."+product)
				select_stmt = "select p."+__productDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by p."+__productDimensionHierarchy+ query_adder +" order by p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_adder += (", s."+store)
				select_stmt = "select p."+__productDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by p."+__productDimensionHierarchy+ query_adder +" order by p."+__productDimensionHierarchy + query_adder
		elif action == "removeDim":
			if time: 
				#remove t.time from query_adder
				query_deleter = string.replace(query_adder,', t.'+time, '')
				query_adder = query_deleter
				select_stmt = "select p."+__productDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by p."+__productDimensionHierarchy+ query_adder +" order by p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_deleter = string.replace(query_adder,', p.'+product, '')
				query_adder = query_deleter
				select_stmt = "select p."+__productDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by p."+__productDimensionHierarchy+ query_adder +" order by p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_deleter = string.replace(query_adder,', s.'+store, '')
				query_adder = query_deleter
				select_stmt = "select p."+__productDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by p."+__productDimensionHierarchy+ query_adder +" order by p."+__productDimensionHierarchy + query_adder
	elif not __timeDimensionHierarchy and not __productDimensionHierarchy:
		if action == "rollup":
			if store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
		elif action == "drilldown":
			if store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
		select_stmt = "select s."+__storeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Store s, `sales_fact` f "
		where_stmt = "where s.store_key = f.store_key "
		groupby_stmt = "group by s."+__storeDimensionHierarchy
		havingby_stmt = ""
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select s."+__storeDimensionHierarchy+", sum(f.dollar_sales) "+
		#	"AS total_sales from Store s,`sales_fact` f "+
		#	"where s.store_key = f.store_key "+
		#	"group by s."+__storeDimensionHierarchy+
		#	" order by s."+__storeDimensionHierarchy)
		if action == "slice":
			if store:
				havingby_stmt = (" Having s."+store+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
		elif action == "dice":
			havingby_stmt = "Having \( s."+store+ "="+ storehavingby1 + "or" + storehavingby2 + "\)" 
		elif action == "addDim":
			if time: 
				query_adder += (", t."+time)
				select_stmt = "select s."+__storeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+ query_adder+" order by s."+__storeDimensionHierarchy + query_adder
			elif product: 
				query_adder += (", p."+product)
				select_stmt = "select s."+__storeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+ query_adder+" order by s."+__storeDimensionHierarchy + query_adder
			elif store:
			 	query_adder += (", s."+store)
				select_stmt = "select s."+__storeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+ query_adder+" order by s."+__storeDimensionHierarchy + query_adder
		elif action == "removeDim":
			if time: 
				#remove t.time from query_adder
				query_deleter = string.replace(query_adder,', t.'+time, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+ query_adder+" order by s."+__storeDimensionHierarchy + query_adder
			elif product: 
				query_deleter = string.replace(query_adder,', p.'+product, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+ query_adder+" order by s."+__storeDimensionHierarchy + query_adder
			elif store: 
				query_deleter = string.replace(query_adder,', s.'+store, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+ query_adder+" order by s."+__storeDimensionHierarchy + query_adder
			
				
	elif not __timeDimensionHierarchy:
		
		if action == "rollup":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
			elif store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
		elif action == "drilldown":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
			elif store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
		
		select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Product p, Store s,`sales_fact` f "
		where_stmt = "where p.product_key = f.product_key AND s.store_key = f.store_key "
		groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy
		havingby_stmt = ""
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", sum(f.dollar_sales) "+
		#	"AS total_sales from Product p, Store s,`sales_fact` f "+
		#	"where p.product_key = f.product_key "+
		#	"AND s.store_key = f.store_key "+
		#	"group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+
		#	" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy)
		if action == "slice":
			if product:
				havingby_stmt = (" Having p."+product+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
			elif store:
				havingby_stmt = (" Having s."+store+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
		elif action == "dice":
			havingby_stmt = "Having \( p."+product+ "="+ producthavingby1 + "or" + producthavingby2 + "\)"+" AND Having \( s."+store+ "="+ storehavingby1 + "or" + storehavingby2 + "\)"
		elif action == "addDim":
			if time: 
				query_adder += (", t."+time)
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder + ", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_adder += (", p."+product)
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder + ", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_adder += (", s."+store)
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder + ", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
		elif action == "removeDim":
			if time: 
				#remove t.time from query_adder
				query_deleter = string.replace(query_adder,', t.'+time, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder + ", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_deleter = string.replace(query_adder,', p.'+product, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder + ", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_deleter = string.replace(query_adder,', s.'+store, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder + ", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
	
	elif not __storeDimensionHierarchy:
		if action == "rollup":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
			elif time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
		if action == "drilldown":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
			elif time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
		select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Product p, Time t,`sales_fact` f "
		where_stmt = "where p.product_key = f.product_key AND t.time_key = f.time_key "
		groupby_stmt = "group by p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy
		havingby_stmt = ""
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
		#		"AS total_sales from Product p, Time t,`sales_fact` f "+
		#		"where p.product_key = f.product_key "+
		#		"AND t.time_key = f.time_key "+
		#		"group by p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+
		#		" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy)
		if action == "slice":
			if product:
				havingby_stmt = (" Having p."+product+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
			elif time:
				havingby_stmt = (" Having t."+time+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
		elif action == "dice":
			havingby_stmt = "Having \( p."+product+ "="+ producthavingby1 + " or " + producthavingby2 + "\)"+" AND Having \( t."+time+ "="+ timehavingby1 + " or " + timehavingby2 + "\)"
		elif action == "addDim":
			if time: 
				query_adder += (", t."+time)
				select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_adder += (", p."+product)
				select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_adder += (", s."+store)
				select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
		elif action == "removeDim":
			if time: 
				#remove t.time from query_adder
				query_deleter = string.replace(query_adder,', t.'+time, '')
				query_adder = query_deleter
				select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_deleter = string.replace(query_adder,', p.'+product, '')
				query_adder = query_deleter
				select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_deleter = string.replace(query_adder,', s.'+store, '')
				query_adder = query_deleter
				select_stmt = "select p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
	
	elif not __productDimensionHierarchy:
		if action == "rollup":
			if time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
			elif store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
		if action == "drilldown":
			if time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
			elif store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
		select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Time t, Store s,`sales_fact` f "
		where_stmt = "where s.store_key = f.store_key AND t.time_key = f.time_key "
		groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy
		havingby_stmt = ""
		#cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt)
		#cur.execute("select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
		#		"AS total_sales from Time t, Store s,`sales_fact` f "+
		#		"where s.store_key = f.store_key "+
		#		"AND t.time_key = f.time_key "+
		#		"group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+
		#		" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy)
		if action == "slice":
			if time:
				havingby_stmt = (" Having t."+time+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
			elif store:
				havingby_stmt = (" Having s."+store+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
		elif action == "dice":
			havingby_stmt = " Having \( t."+time+ "="+ timehavingby1 + " or " + timehavingby2 + "\) AND Having \( s."+store+ "='"+ storehavingby1 + "' or '" + storehavingby2 + "'\)"
		elif action == "addDim":
			if time: 
				query_adder += (", t."+time)
				select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy + query_adder
			elif product: 
				query_adder += (", p."+product)
				select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy + query_adder
			elif store: 
				query_adder += (", s."+store)
				select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy + query_adder
		elif action == "removeDim":
			if time: 
				#remove t.time from query_adder
				query_deleter = string.replace(query_adder,', t.'+time, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy + query_adder
			elif product: 
				query_deleter = string.replace(query_adder,', p.'+product, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy + query_adder
			elif store: 
				query_deleter = string.replace(query_adder,', s.'+store, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Time t, Product p, Store s, `sales_fact` f "
				where_stmt = " where t.time_key = f.time_key AND s.store_key = f.store_key AND p.product_key = f.product_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy + query_adder
	
	else:
		if action == "rollup":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
			elif store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
			elif time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
		if action == "drilldown":
			if product:
				global __productDimensionHierarchy
				__productDimensionHierarchy = product
			elif store:
				global __storeDimensionHierarchy
				__storeDimensionHierarchy = store
			elif time:
				global __timeDimensionHierarchy
				__timeDimensionHierarchy = time
		select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) AS total_sales "
		from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
		where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
		groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy
		havingby_stmt = ""
			
			
			#cur.execute("select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+", sum(f.dollar_sales) "+
			#	"AS total_sales from Product p, Time t, Store s,`sales_fact` f "+
			#	"where p.product_key = f.product_key "+
			#	"AND s.store_key = f.store_key "+
			#	"AND t.time_key = f.time_key "+
			#	"group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+
			#	" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy)
		if action == "slice":
			if product:
				havingby_stmt = (" Having p."+product+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
			elif store:
				havingby_stmt = (" Having s."+store+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
			elif time:
				havingby_stmt = (" Having t."+time+ "= '"+ havingby + "' ")
				groupby_stmt += havingby_stmt
		if action == "dice":
			havingby_stmt = "Having \( t."+time+ "="+ timehavingby1 + " or " + timehavingby2 + "\)"+" AND Having \( s."+store+ "="+ storehavingby1 + " or " + storehavingby2 + "\)"+" AND Having \( p."+product+ "="+ producthavingby1 + " or " + producthavingby2 + "\)"
		elif action == "addDim":
			if time: 
				query_adder += (", t."+time)
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
				where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_adder += (", p."+product)
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
				where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_adder += (", s."+store)
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
				where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
		elif action == "removeDim":
			if time: 
				#remove t.time from query_adder
				query_deleter = string.replace(query_adder,', t.'+time, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
				where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif product: 
				query_deleter = string.replace(query_adder,', p.'+product, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
				where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			elif store: 
				query_deleter = string.replace(query_adder,', s.'+store, '')
				query_adder = query_deleter
				select_stmt = "select s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +", sum(f.dollar_sales) AS total_sales "
				from_stmt = "from Product p, Time t, Store s,`sales_fact` f "
				where_stmt = "where p.product_key = f.product_key "+"AND s.store_key = f.store_key "+"AND t.time_key = f.time_key "
				groupby_stmt = "group by s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy+", t."+__timeDimensionHierarchy+ query_adder +" order by t."+__timeDimensionHierarchy+", s."+__storeDimensionHierarchy+", p."+__productDimensionHierarchy + query_adder
			
	print('test')
	print(select_stmt + from_stmt + where_stmt + groupby_stmt + havingby_stmt)
	cur.execute(select_stmt + from_stmt + where_stmt + groupby_stmt + havingby_stmt)
	results = cur.fetchall()
	field_names = [str(i[0]) for i in cur.description]
	print(field_names)

	r = [dict((cur.description[i][0], value) 	
               for i, value in enumerate(row)) for row in results]
	jsonDUMPfromMysql = json.dumps(r)
	return jsonDUMPfromMysql
	

def connect():
	try:
		conn = MySQLdb.connect(host='localhost', user='root',
		 passwd='', db='grocerydb')
		if conn.is_connected():
			print 'Connected to MySQL database'
	except getopt.GetoptError, e:
		print e
	finally:
		conn.close()

if __name__ == '__main__':
	app.run(debug=True)
	connect()


