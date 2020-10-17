#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


fname=open("mbox-short.txt") #for getting the data from file
counts=dict()
List=list()
for line in fname: #fetching the dat from file
    if line.startswith("From "):#checking the line starts with from
        
        line=line.split() #spliting the line which starts with  from
        List.append(line[1]) #now appending the email in a list
#now checking the count of words and storing in a dictionary 
for word in List:
    counts[word]=counts.get(word,0)+1
  
bigemail=None
bigno=None
for k,v in counts.items(): 
    
    if bigemail is None or v>bigno:
        bigemail=k
        bigno=v
print(bigemail,bigno)
        
        
        
       
       
        

    
           
