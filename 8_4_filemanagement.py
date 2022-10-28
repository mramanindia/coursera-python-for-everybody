#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in alphabetical order.

fh = open('romeo.txt')
lst = list()
for line in fh:
    word=line.rstrip()
    #for strinpping the line
    word=line.split()
    for element in word:
        # Checking the elements or character in words
        if(element not in lst):
            lst.append(element)
lst.sort()
print(lst)
    


      
   
