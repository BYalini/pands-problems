# A python script to read in a text file and outputs the number of e's it contains
# Ref : https://realpython.com/python-command-line-arguments/

# import interal python module sys to access system argument(s)
import sys 

# only runs if one additional argument is passed with script name (i.e filename to count 'e' s in)
if len(sys.argv)  == 2 :
   
    # argv[0] is the python script name, argv[1] is file name
    file_name = sys.argv[1]
    
    # define letter to count the occurrence
    letter = 'e'
    total = 0
    
    #open file with context manager 
    with open(file_name,'r') as file:
        # loop through each line in the file
        for line in file : 
            # count how manty times 'e' appear in each line
            total = total + line.count(letter)
    # context manager closes the file
        
    print(total)




