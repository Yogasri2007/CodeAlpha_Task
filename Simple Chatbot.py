import time
from datetime import datetime

def student_chatbot():
    print("\n📚 Welcome to StudyBuddy ChatBot! 📚")
    print("How can I help you today?\n")
    
    # Main categories
    categories = {
        1: "Study Help",
        2: "Campus Life",
        3: "Time Management",
        4: "General Chat",
        5: "Exit"
    }
    
    # Responses for each category
    responses = {
        # Study Help
        1: {
            1: ("Math help", "Remember PEMDAS for order of operations: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction"),
            2: ("Writing tips", "Start with an outline! Introduction, 3 main points, conclusion."),
            3: ("Science concepts", "The scientific method: Question, Research, Hypothesis, Experiment, Analyze, Conclusion"),
            4: ("Back to main menu", "")
        },
        
        # Campus Life
        2: {
            1: ("Clubs", "Check the student center bulletin board for club listings!"),
            2: ("Food options", "The cafeteria has daily specials, and there are 3 food trucks near the library."),
            3: ("Dorm life", "Bring shower shoes, an extra-long twin sheet set, and a good lamp!"),
            4: ("Back to main menu", "")
        },
        
        # Time Management
        3: {
            1: ("Study schedule", "Try the Pomodoro technique: 25 mins study, 5 mins break, repeat!"),
            2: ("Prioritization", "Use the Eisenhower Box: Urgent/Important matrix for tasks."),
            3: ("Avoid procrastination", "Break big tasks into smaller steps and reward yourself after each one."),
            4: ("Back to main menu", "")
        },
        
        # General Chat
        4: {
            1: ("Joke", "Why did the student eat his homework? Because the teacher said it was a piece of cake!"),
            2: ("Motivation", "You got this! Every expert was once a beginner."),
            3: ("Current time", f"The current time is {datetime.now().strftime('%H:%M')}"),
            4: ("Back to main menu", "")
        }
    }
    
    while True:
        # Show main menu
        print("\nMAIN MENU:")
        for num, category in categories.items():
            print(f"{num}. {category}")
        
        try:
            main_choice = int(input("\nChoose a category (1-5): "))
            
            if main_choice == 5:
                print("\n👋 Goodbye! Good luck with your studies!")
                break
            elif 1 <= main_choice <= 4:
                # Show submenu
                while True:
                    print(f"\n{categories[main_choice].upper()} OPTIONS:")
                    for num, (option, _) in responses[main_choice].items():
                        print(f"{num}. {option}")
                    
                    sub_choice = int(input("\nChoose an option (1-4): "))
                    
                    if sub_choice == 4:  # Back to main menu
                        break
                    elif 1 <= sub_choice <= 3:
                        print(f"\n🤖 {responses[main_choice][sub_choice][1]}\n")
                        input("Press Enter to continue...")
                    else:
                        print("Please enter a number between 1-4")
            else:
                print("Please enter a number between 1-5")
                
        except ValueError:
            print("Please enter a valid number!")

# Run the chatbot
student_chatbot()
