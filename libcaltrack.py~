import os
import sys
import psycopg2

item = input("Item:")
conn = psycopg2.connect("dbname=caltrack user=andrea")
cur = conn.cursor()
query = "SELECT cal \
FROM test \
INNER JOIN nuttest \
on (nutnum = nut_key) \
WHERE code='{}'".format(item)
cur.execute(query)
results = cur.fetchone()[0]


cur.close()
conn.close()
print("calories:", results)
