import psycopg2
conn = psycopg2.connect(dbname='test_db', user='anton',
                        password='admin', host='localhost')
cursor = conn.cursor()
# cursor.execute("""SELECT brnd.title,
#                     COUNT(brnd.id)
#                     FROM notebooks_notebook AS ntbk
#                     JOIN notebooks_brand AS brnd
#                     ON ntbk.brand_id = brnd.id
#                     GROUP BY brnd.title ORDER BY count DESC """)

cursor.execute("""SELECT brnd.title,
                    COUNT(brnd.id)
                    FROM notebooks_notebook AS ntbk
                    JOIN notebooks_brand AS brnd
                    ON ntbk.brand_id = brnd.id
                    GROUP BY brnd.title """)

for row in cursor:
    print(row)
cursor.close()
conn.close()