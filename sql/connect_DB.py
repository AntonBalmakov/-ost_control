import psycopg2
conn = psycopg2.connect(dbname='test_db', user='anton',
                        password='admin', host='localhost')
cursor = conn.cursor()
cursor.execute("""SELECT brnd.title,
                    COUNT(brnd.id)
                    FROM notebooks_notebook AS ntbk
                    JOIN notebooks_brand AS brnd
                    ON ntbk.brand_id = brnd.id
                    GROUP BY brnd.title ORDER BY count DESC """)

cursor.execute("""select x.width, x.depth, x.height, count(*) cnt
                from notebooks_notebook n
                inner join notebooks_brand as b on n.brand_id = b.id
                cross join lateral (values (width::int / 5 * 5, depth / 5 * 5, height / 5 * 5)) x(width, depth, height)
                group by x.width, x.depth, x.height """)

for row in cursor:
    print(row)
cursor.close()
conn.close()
