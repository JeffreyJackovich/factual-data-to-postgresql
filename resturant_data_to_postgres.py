import json
from factual import Factual
from itertools import islice
from factual.utils import circle
import time
import psycopg2
import sys

# http://developer.factual.com/working-with-categories/

class FactualAPI:

	def __init__(self, OAUTH_KEY, OAUTH_SECRET, factual):
		self.OAUTH_KEY = OAUTH_KEY  
		self.OAUTH_SECRET = OAUTH_SECRET
		self.factual = Factual(OAUTH_KEY, OAUTH_SECRET)


	def start_request_rate_ctrl(self):
	    global request_ctrl_time
	    global request_ctrl_count
	    self.request_ctrl_time = time.time()
	    self.request_ctrl_count = 0


	def wait_before_request(self):
	    global request_ctrl_time
	    global request_ctrl_count
	    request_ctrl_count += 1
	    if request_ctrl_count == MAX_REQUESTS_MINUTE:
	        # Wait for the rest of the minute and some seconds more
	        dif_time = time.time() - request_ctrl_time
	        if dif_time < 60:
	            time.sleep(dif_time + 10)
	            request_ctrl_time = time.time()
	            self.request_ctrl_count = 0


	def get_schema_field_names(self, factual, table_id):
		print("Getting schema field names\n")
		self.schema = factual.table(table_id).schema()
		self.field_names = [field['name'] for field in self.schema['fields']]
		return self.field_names


	def query_restaurants_by_proximity(self, factual, category_ids, lat, long, radius_meters):
		print("Querying restaurants for: lat, long, radius: %f, %f, %f" % (lat, long, radius_meters))
		return self.factual.table(TABLE_ID).filters({'$and': [{'$or': [{'website': {'$blank': False}}, {'email': {'$blank': False}}]},
													{'category_ids': {'$includes_any':category_ids}}]}).geo(circle(lat, long, radius_meters)).include_count(True)


	def get_restaurants_by_proximity(self, factual, schema_field_names):
		print("Getting restaurants by proximity!\n")
		self.start_request_rate_ctrl()
		restaurants = self.query_restaurants_by_proximity(factual, CATEGORY_IDS, 37.332915, -121.888558, 1000) 
		self.process_query_results(conn, cursor, schema_field_names, restaurants)


	def connect_to_postgres(self, hostname, db, name, pw):
		print("\nConnecting to postgres at: "+str(hostname)+" - "+str(db)+" - "+str(name))
		self.conn = None
		try:
			# Try to connect to the database, store connection object in 'conn'
			self.conn = psycopg2.connect(host=hostname, database=db, user=name, password=pw)
			# Get the cursor object from connection, used to traverse records
			self.cursor = self.conn.cursor()
			print("Hot damn, Successfully connected to database!\n")
			return self.conn,self.cursor 
		except psycopg2.DatabaseError, e:
			# If database error, rollback any changes
			if conn:
				conn.rollback()
				conn.close()
			print 'Error %s' % e
			sys.exit(1)


	def process_query_results(self, conn, cursor, schema_field_names, restaurants):
		print("Processing query results!\n")
		total_row_count = restaurants.total_row_count()
		print("\tTotal row count: %d" % total_row_count)
		current_row_offset = 0
		while current_row_offset < total_row_count:
			try:
				data = restaurants.offset(current_row_offset).limit(50).data()
			except Exception, e:
				e_obj = json.loads(e.message['response'])
				print "%s: %s" % ("Read request", e_obj['message'])
				exit(-1)
			current_row_offset += len(data)
			self.write_table_rows(conn, cursor, schema_field_names, data)
			print("\t Congrats. Wrote (%d/%d) restaurants rows..." % (current_row_offset, total_row_count))


	def write_table_rows(self, conn, cursor, schema_field_names, data):
		print("Writing table rows!\n")
		keys = schema_field_names
		for item in data:
			try:
				factual_restaurants_list = [json.dumps(item[key]) if item.get(key) else 'n/a' for key in keys]
				unique_name = factual_restaurants_list[0]
				unique_address = factual_restaurants_list[1]
				unique_address_extended = factual_restaurants_list[2]
				unique_po_box = factual_restaurants_list[3]
				unique_locality = factual_restaurants_list[4]
				unique_region = factual_restaurants_list[5]
				unique_postcode = factual_restaurants_list[6]
				unique_website = factual_restaurants_list[7]
				unique_latitude = factual_restaurants_list[8] 
				unique_longitude = factual_restaurants_list[9]
				unique_country = factual_restaurants_list[10]
				unique_factual_id = factual_restaurants_list[11]
				unique_tel = factual_restaurants_list[12]
				unique_fax = factual_restaurants_list[13]
				unique_email = factual_restaurants_list[14]
				unique_category_ids = factual_restaurants_list[15]
				unique_category_labels = factual_restaurants_list[16]
				unique_chain_id = factual_restaurants_list[17]
				unique_chain_name = factual_restaurants_list[18]
				unique_neighborhood = factual_restaurants_list[19]
				unique_admin_region = factual_restaurants_list[20]
				unique_hours = factual_restaurants_list[21]
				unique_hours_display = factual_restaurants_list[22]
				cursor.execute("INSERT INTO factual_resturant_data (name, address, address_extended, po_box, locality, region, 		\
					postcode, website, latitude, longitude, country, factual_id, tel, fax, email, category_ids, category_labels,	\
					chain_id, chain_name, neighborhood, admin_region, hours, hours_display)  										\
				VALUES                         																						\
					(%s, %s, %s, %s,         											 											\
					%s, %s, %s, %s, %s, %s, %s, %s,  																				\
					%s, %s, %s, %s, %s, %s, %s,       																				\
					%s, %s, %s, %s)                                      															\
				ON  																												\
				CONFLICT (factual_id)                        																		\
				DO UPDATE SET  																										\
				name = EXCLUDED.name;",																								\
					(unique_name, unique_address, unique_address_extended, unique_po_box, unique_locality, unique_region, 
					unique_postcode, unique_website, unique_latitude, unique_longitude, unique_country, unique_factual_id, 
					unique_tel, unique_fax, unique_email, unique_category_ids, unique_category_labels, unique_chain_id, 
					unique_chain_name, unique_neighborhood, unique_admin_region, unique_hours, unique_hours_display))                                                                                
				self.conn.commit()
			except psycopg2.IntegrityError, e:
				print 'Error %s' % e
				sys.exit(1)


# Oauthkey and secret key
OAUTH_KEY = '<insert oauth_key>'
OAUTH_SECRET = '<insert oauth_secret>'

# Required factual api call 
factual = Factual(OAUTH_KEY, OAUTH_SECRET)

# Creates instance of the "FactualAPI" class
factual_api_class_object = FactualAPI(OAUTH_KEY, OAUTH_SECRET, factual)


TABLE_ID = 'places-us'
# "347" is category: Social > Food and Dining > Restaurants 
CATEGORY_IDS = [347]

# Request Limit values
MAX_REQUESTS_MINUTE = 500
request_ctrl_time = 0
request_ctrl_count = 0

# Database variables
hostname = "<insert hostname>"
db = "<insert database name>"
name = "<insert name>"
pw = "<insert password>"

# Method Calls
conn,cursor = factual_api_class_object.connect_to_postgres(hostname,db,name,pw)
schema_field_names = factual_api_class_object.get_schema_field_names(factual, TABLE_ID)
factual_api_class_object.get_restaurants_by_proximity(factual,schema_field_names)



