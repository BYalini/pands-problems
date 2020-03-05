# count the number of e s in moby-dict.txt
file_name = './data/moby-dict.txt'

with open(file_name, 'r') as file : 
    total =0 
    for line in file: 
        total = total+ line.count('e')
    print(total)


