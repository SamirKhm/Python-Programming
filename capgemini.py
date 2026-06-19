n=int(input("Enter the number of semesters: "))

max_marks=[]

for i in range(n):
    subjects=int(input("Enter the number of subjects in semester "+str(i+1)+": "))
    max=-1
    for j in range(subjects):
        marks=int(input("Enter the marks obtained in subject "+str(j+1)+": "))
        if marks>max:
            max=marks

        if marks<0 or marks>100:
            print("Invalid marks entered. Please enter marks between 0 and 100.")
            exit()
        
    max_marks.append(max)

for j in range(n):
    print("Maximum marks obtained in semester",j+1,":",max_marks[j])

