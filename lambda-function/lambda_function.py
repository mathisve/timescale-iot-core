import psycopg2

conn_str = "postgres://tsdbadmin:password@service.project.tsdb.cloud.timescale.com:35961/tsdb?sslmode=require"
conn = psycopg2.connect(conn_str)
cursor = conn.cursor()

def handler(event, context):
	print(event)

	try:
		cursor.execute("INSERT INTO sensor (time, value) VALUES (NOW(), %s);", [event["value"]])
		conn.commit()
	except (Exception, psycopg2.Error) as error:
		print(error)
		
	return 