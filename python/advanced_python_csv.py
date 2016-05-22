PLACE YOUR CODE HERE
import pandas

faculty_df = pandas.read_csv('/Users/Manoj/Documents/metis/pre-work/faculty.csv',sep='\s*,\s*',engine='python')
fout = open('/Users/Manoj/Documents/metis/pre-work/email_list.csv','w')
for row in faculty_df.itertuples():
    fout.write(row.email+'\n')
fout.close()