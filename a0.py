"""
Kyle Edmondson
"""


print("Starting a0 - Python: Print, List, Dictionary & Git")
lncount = 0
with open("globalterrorismdb_0617dist.csv") as f:
    for line in f:
        lncount += 1
        if lncount < 10:
            print(line[0:12])
            
            
print("done and we found this many lines:", lncount)
