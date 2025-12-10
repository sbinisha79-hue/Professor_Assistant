import random

print("Welcome to professor assistant version 
professor_name = input("Please Enter Your Name: ")
print(f"Hello Professor {professor_name}, I am here to help you create exams from a question bank.")

while True:

    
    choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()

    if choice == "no":
        print(f"Thank you professor {professor_name}. Have a good day!")
        break

    elif choice == "yes":
        
        path = input("Please Enter the Path to the Question Bank: ")

        try:
            with open(path, "r", encoding="utf-8") as file:
                data = [line.strip() for line in file.readlines()]
            print("Yes, indeed the path you provided includes questions and answers.")

            # Extract question-answer pairs
            qa_pairs = [(data[i], data[i+1]) for i in range(0, len(data), 2)]

            
            num = int(input("How many question-answer pairs do you want to include in your exam? "))
            if num > len(qa_pairs):
                print("❌ Not enough questions in the question bank! Try again.")
                continue

            
            save_file = input("Where do you want to save your exam? ")

            selected = random.sample(qa_pairs, num)

            with open(save_file, "w", encoding="utf-8") as output:
                for q, a in selected:
                    output.write(q + "\n")
                    output.write(a + "\n\n")

            print(f"🎉 Congratulations Professor {professor_name}. Your exam is created and saved in {save_file}.")

        except FileNotFoundError:
            print("❌ Error: The file path is invalid. Please try again.")

    else:
        print("Invalid input, please enter Yes or No.")
