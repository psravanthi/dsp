#PLACE YOUR CODE HERE
import pandas    
  
degree = {}
title = {}
email = []
domain = {}
faculty_df = pandas.read_csv('/Users/Manoj/Documents/metis/prework/faculty.csv',sep='\s*,\s*',engine='python')

faculty_df['degree'] = faculty_df['degree'].str.replace('.','').str.strip().str.upper()
faculty_df['title'] = faculty_df['title'].str.upper().str.replace("\sIS\s"," OF ")
for row in faculty_df.itertuples():
    
    for d in row.degree.split(' '):
        if d == '0':
            continue
       
        if d not in degree:
            degree[d] = 1
        else:
            degree[d] = degree[d] + 1
    if row.title not in title:
        title[row.title] = 1
    else:
        title[row.title] += 1
    if row.email not in email:
        email.append(row.email)
    if row.email.split('@')[1] not in domain:
        domain[row.email.split('@')[1]] = 1
    else:
        domain[row.email.split('@')[1]] += 1
print("Degrees :",degree,"\n","Title: ",title,"\n","Email list: ",email,"\n","Domain Names: ",domain)

    
