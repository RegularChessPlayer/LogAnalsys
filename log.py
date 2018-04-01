#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# 1. What are the most popular three articles of all time?
query1 = "select title,views from article_view limit 3"

# 2. Who are the most popular article authors of all time?
query2 = """select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""

# 3. On which days did more than 1% of requests lead to errors?
query3 = "select * from error_log_view where \"Percent Error\" > 1"


def get_query1():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute(query1)
	results = c.fetchall()
	db.close()
	print ("query1")
	for result in results:
		print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' views')
	return

def get_query2():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute(query2)
	results = c.fetchall()
	db.close()
	print ("query2")
	for result in results:
		print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' views')
	return

def get_query3():
	db = psycopg2.connect(database=DBNAME)
	c = db.cursor()
	c.execute(query3)
	results = c.fetchall()
	db.close()
	print ("query3")
	for result in results:
		print ('\t' + str(result[0]) + ' ---> ' + str(result[1]) + ' %')
	return results


get_query1()
get_query2()
get_query3()



