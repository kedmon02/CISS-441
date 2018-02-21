import sqlite3

dbfile = 'payroll_dc_small.db' # database file
conn = sqlite3.connect(dbfile) # connect to db

# give me a new line
print("")


def main():
	# this is my header row
	print ("{0:<25} {1:<15} {2:<10} {3:<10}".format(
		"Education level", "Type", "salmax", "salmin"))
		
	cursor = conn.execute("""
			select edlvl.edlvltypt, edlvl.edlvlt, max(f.salary) salmax, min(f.salary) salmin
			from factdata_mar2016 f, edlvl
			where f.edlvl=edlvl.edlvl
			group by edlvl.edlvltypt, edlvl.edlvlt
			order by salmax desc
			limit 20;
		""")
		
	for row in cursor:
		Education_level, type, salmax, salmin = row
		print("{0:<25} {1:<15} {2:<10} {3:<10}".format(
				Education_level,
				type[0:14],
				salmax,
				salmin
				))
				
				
	print("/nThis is my report of min and max salaries by location.")
	conn.close()
		
		
		
if __name__== "__main__":
	main()