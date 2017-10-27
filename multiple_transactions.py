import sqlite3
import os

SQDB_TMP = '/tmp/example.db'


def insert_rows(conn):
	c = conn.cursor()
	c.execute('''INSERT INTO employees VALUES ('John', 'Doe', 100, 15)''')
	c.execute('''INSERT INTO employees VALUES ('Jane', 'Roe', 110, 5)''')
	c.execute('''INSERT INTO employees VALUES ('Alice', 'Anderson', 80, 20)''')
	c.execute('''INSERT INTO employees VALUES ('Bob', 'Brown', 70, 30)''')
	conn.commit()
	print_db(conn)

def print_db(conn):
	c = conn.cursor()
	db = c.execute('''SELECT * FROM employees''')
	print '\n\n************************************'
	for row in db:
		print row
	print '************************************\n\n'

def update_pay_of_list_of_people(conn):
	c = conn.cursor()
	update_query = '''
		UPDATE employees SET salary = 120, bonus = 20 WHERE firstname = 'John'; COMMIT;
		UPDATE employees SET salary = 95, bonus = 15 WHERE firstname = 'Alice'; COMMIT;
	'''
	c.execute(update_query)
	print_db(conn)

def experiment(conn):
	insert_rows(conn)
	update_pay_of_list_of_people(conn)

if __name__ == '__main__':
	try:
		conn = sqlite3.connect(SQDB_TMP)
		c = conn.cursor()
		c.execute('''
    		CREATE TABLE IF NOT EXISTS employees 
    		(
    			firstname text PRIMARY KEY,
    			lastname text,
    			salary int,
    			bonus int
    		)''')
		experiment(conn)
		conn.close()
	except:
		raise
	finally:
		if os.path.isfile(SQDB_TMP):
			os.remove(SQDB_TMP)
