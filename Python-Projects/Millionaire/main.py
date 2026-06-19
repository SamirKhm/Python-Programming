questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

for q in questions:
    print(q[0])
    print(f"a.{q[1]}")
    print(f"b.{q[2]}")
    print(f"c.{q[3]}")
    print(f"d.{q[4]}")

    #Check wether the answer is correct or not
    a=input("Enter your answer(a/b/c/d): ")
    if(q[5]==1 and a=="a"):
        print("Correct answer\n")
    elif(q[5]==2 and a=="b"):
        print("Correct answer\n")
    elif(q[5]==3 and a=="c"):
        print("Correct answer\n")
    elif(q[5]==4 and a=="d"):
        print("Correct answer\n")
    else:
        print("Incorrect answer\n")