# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
1. man : Reads the manual page
2. chmod : 'Change mode'. Changes the access permissions to files and directories
3. find :
4. grep :
5. pushd :
6. popd :
7. chdown:
8. less:
9. cat :
10. head: 
---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >
* ls : list files in this directory
* ls -a : lists all files including the hidden files
* ls -l : shows file or directory, size, modified date and time, file or folder name and owner of file and it’s permission
* ls -lh :same as above but shows size in 'human readable' 
* ls -lah : same as lh but lists the hidden files too
* ls -t : Displays newest file first based on timestamp
* ls -Glp : Displays the files in long format but prevents owner info from being shown. Also, directories are shown as /


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
ls -ltr : shows latest modification file or directory
ls -R : Recursively lists sub directories
ls -S : Shows file size in order. Largest being the 
ls -d : Displays only directories
ls -f : interprets name argument as directory and so can be used to search through directories

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs executes some command from standard input. This can be done on a list of files or directories.
Ex: 
find . -name "*.txt" | xargs grep "unix" 
The above command finds all the .txt files in the current or below directories  and then searches for the word 'unix' in each .txt file



 

