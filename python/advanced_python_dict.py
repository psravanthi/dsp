PLACE YOUR CODE HERE
import pandas
from collections import defaultdict
fac_lastname = defaultdict(list)
fac_fullname = {}
faculty_df = pandas.read_csv('/Users/Manoj/Documents/metis/prework/faculty.csv',sep='\s*,\s*',engine='python')

for row in faculty_df.itertuples():
    fac_lastname[row.name.split()[-1]].append([row.degree,row.title,row.email])
    fac_fullname[(row.name.split()[0],row.name.split()[-1])] = [row.degree,row.title,row.email]

facl=sorted(fac_lastname.items())
facn=sorted(fac_fullname.items())
print (facl[:3],"\n")
print (facn[:3],"\n")
facn_r=sorted(fac_fullname.items(), key = lambda x: x[0][1])
print (facn_r[:3])




