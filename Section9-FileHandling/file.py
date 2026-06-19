

# f=open("Section9-FileHandling/sam.txt","rt") 
# # rt - read text
# # rb - read binary
# # wt - write text
# # wb - write binary
# # at - append text
# # ab - append binary

# content=f.read()
# print(content)
# f.close()

# # writing

# f=open("Section9-FileHandling/sam.txt","wt")

# string='''
# xyz'''

# f.write(string)
# f.close()

# # appending

# f=open("Section9-FileHandling/sam.txt","at")

# string='''
# abc''' 

# f.write(string)
# f.close()

# f=open("Section9-FileHandling/sam.txt","rt")
# content=f.read()
# print(content)
# f.close()


# with statement - it automatically closes the file after the block of code is executed

with open("Section9-FileHandling/sam.txt","rt") as f:
    content=f.read()
    print(content)
