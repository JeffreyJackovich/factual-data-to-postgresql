import psycopg2


def connect_to_postgres(hostname, db, name, pw):
    print("\nConnecting to postgres at: "+str(hostname)+" - "+str(db)+" - "+str(name))
    conn = None
    try:
        # Try to connect to the database, store connection object in 'conn'
        conn = psycopg2.connect(host=hostname, database=db, user=name, password=pw)
        # Get the cursor object from connection, used to traverse records
        cursor = conn.cursor()
        print("Hot damn, Successfully connected to database!\n")
        create_raw_export_table(conn,cursor) 
        return conn,cursor
    except psycopg2.DatabaseError, e:
        # If database error, rollback any changes
        if conn:
            conn.rollback()
            conn.close()
        print 'Error %s' % e
        sys.exit(1)


def create_raw_export_table(conn, cursor):
    try:
        print "Creating table that do not exist."
        cursor.execute("CREATE TABLE IF NOT EXISTS factual_test (name VARCHAR(1000), address TEXT,          \
            address_extended TEXT, po_box TEXT, locality TEXT, region TEXT, postcode TEXT, website TEXT,    \
            latitude TEXT, longitude TEXT, country TEXT, factual_id TEXT PRIMARY KEY, tel TEXT, fax TEXT,   \
            email TEXT, category_ids TEXT, category_labels TEXT, chain_id TEXT, chain_name TEXT,            \
            neighborhood TEXT, admin_region TEXT, hours TEXT, hours_display TEXT);")
        conn.commit()
        print "Table created."
    except psycopg2.DatabaseError, e:
        #If database error, let's rollback any changes.
        if con:
            con.rollback()
            con.close()
        print 'Error %s' % e
        sys.exit(1)


# Database variables
hostname = "<insert hostname>"
db = "<insert database name>"
name = "<insert name>"
pw = "<insert password>"

# Cursor connection method call
conn,cursor = connect_to_postgres(hostname, db, name, pw)

