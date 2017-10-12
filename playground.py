import sqlite3
import os

SQDB_TMP = '/tmp/example.db'


def insert_row(conn):
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

def update_pay_of_one_person(conn):
	c = conn.cursor()
	# check that the primary key is present first
	entry_in_db = c.execute('''
		SELECT count(*) 
		FROM employees 
		WHERE firstname = 'John' AND lastname = 'Doe'
	''')
	result = c.fetchall()
	if result[0][0] == 1:
		c.execute('''
			UPDATE employees
			SET salary = 120, bonus = 20
			WHERE firstname = 'John' AND lastname = 'Doe'
		''')
		conn.commit()
	print_db(conn)

def format_tuples(n):
	s = '('
	for _ in range(n-1): 
		s += '?, '
	s += '?)'
	return s

def update_pay_of_list_of_people(conn):
	c = conn.cursor()
	update_list_all = [
		('John', 'Doe', 120, 20),
		('Alice', 'Anderson', 95, 20),
		('Bob', 'Brown', 85, 30)
	]
	update_names_tuple = map(lambda row: row[0], update_list_all)

	if len(update_names_tuple) > 0:
		validate_names_query = '''
			SELECT firstname 
			FROM employees
			WHERE firstname IN '''
		validate_names_query += format_tuples(len(update_names_tuple))
		c.execute(validate_names_query, update_names_tuple)
		result = c.fetchall()
		validated_names_tuple = tuple(map(lambda entry: entry[0], result))
		
		# actual update
		# update_query = "REPLACE INTO employees (firstname, salary, bonus) VALUES ('John', 120, 20)"
		update_query = '''
			INSERT INTO employees (firstname, lastname, salary, bonus)
			VALUES 
				('John', 'Doe', 120, 20),
				('Alice', 'Anderson', 95, 20)
		'''
		c.execute(update_query)
		print_db(conn)

def experiment(conn):
	insert_row(conn)
	# update_pay_of_one_person(conn)
	update_pay_of_list_of_people(conn)


if __name__ == '__main__':
	try:
		conn = sqlite3.connect(SQDB_TMP)
		c = conn.cursor()
		c.execute('''
    		CREATE TABLE IF NOT EXISTS employees 
    		(
    			firstname text PRIMARY KEY ON CONFLICT REPLACE,
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
