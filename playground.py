import sqlite3

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
    	conn = sqlite3.connect(db_file)
    	c = conn.cursor()
    	c.execute("CREATE TABLE IF NOT EXISTS stocks (firstname text, lastname text, salary int, bonus int)")
    	return conn
    except:
    	raise

def close_connection(conn):
    conn.close()


def insert_row(conn):
	c = conn.cursor
	c.execute('''INSERT INTO stocks VALUES ('John', 'Doe', 1000, 15)''')

def experiment(conn):
	pass

if __name__ == '__main__':
	conn = create_connection('example.db')
	experiment(conn)
	close_connection(conn)
