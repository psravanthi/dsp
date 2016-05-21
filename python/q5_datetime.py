
from datetime import datetime
def datediff(start,stop,format):
 d1 = datetime.strptime(start, format)
 d2 = datetime.strptime(stop, format)
 return (abs((d1-d2).days))
 
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'  
print("Number of days between",'01-02-2013',"and",'07-28-2015',"is:", datediff('01-02-2013','07-28-2015',"%m-%d-%Y")) 

####b)  
date_start = '12312013'  
date_stop = '05282015'  
print("Number of days between",'12312013',"and",'05282015',"is:", datediff('12312013','05282015',"%m%d%Y"))

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
print("Number of days between",'15-Jan-1994',"and",'14-Jul-2015',"is:", datediff('15-Jan-1994','14-Jul-2015',"%d-%b-%Y"))