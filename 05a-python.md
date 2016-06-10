# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> 
Lists and tuples are similar in sense that they have a set order and can be accessed using an index. Tuples are immutable whereas list values can be changed. Usually tuples are treated as one coherent unit. Lists can be a sequence of different items. Lists cannot be used as dictionary keys as keys should be immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>
Both lists and sets are a collection of data. While lists have a set order, Sets are a collection of unordered items. Sets do not allow duplicate elements whereas duplicates are allowed in lists.
Lists are faster when it comes to iterating over elements but when it comes to determining the presence of element, sets are significantly faster. Sets use hash function to store elements and hence it takes O(1) to find an elements. Lists take O(n), in worst case.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>
Small anonymous functions can be created with the lambda keyword. The function is created on runtime and not compiled.
Ex:
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted(pairs, key = lambda x : x[1])
Sorts based on the 2nd element 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.
>>
Comprehensions are constructs that allow sequences to be built from other sequences. 
>>
Ex:  1) squares = [x**2 for x in range(10)]
>> 
     'map' equivalent : squares = map(lambda x: x**2, range(10))
>>    
2) special_squares = [x for x in squares if x > 5 and x < 50]
>>     
'filter' equivalent : special_squares = filter(lambda x: x > 5 and x < 50, squares)
>>
Apart from being more readable, List comprehensions are also efficient in most cases (When lambda is used). However, map and filter are more efficient when the function is predefined.
>>
Set Comprehension :
a = {x for x in 'abracadabra' if x not in 'abc'}
Dictionary Comprehension:
list = {(1,abc),(2,hjg)}
output = { key:value for item in list}

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.  

from datetime import datetime
def datediff(start,stop,format):
 d1 = datetime.strptime(start, format)
 d2 = datetime.strptime(stop, format)
 return (abs((d1-d2).days)) 
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
datediff('01-02-2013','07-28-2015',"%m-%d-%Y")

937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
 datediff('12312013','05282015',"%m%d%Y")
 
513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
datediff('15-Jan-1994','14-Jul-2015',"%d-%b-%Y")

7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





