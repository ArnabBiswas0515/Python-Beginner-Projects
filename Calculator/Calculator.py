HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r')
    lines = file.readlines()
    if len(lines) == 0:
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w')
    file.close()
    print("History Cleared")

def save_history(equation, result):
    file = open(HISTORY_FILE, 'a')
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input")
        return
    num1, num2 = float(parts[0]), float(parts[2])
    operator = parts[1]

    if operator in ['+','-','*','/']:
        match operator:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 == 0:
                    print("Cannot divide by zero.")
                    return
                result = num1 / num2
            case _:
                print("There was an Error")
                return
            
    if int(result) == result:
        result = int(result)
    print(f"Result: {result}")
    save_history(user_input, result)

def main():
    print("--- A Simple Calculator ---")
    print("Operation: (History, Clear, Exit or Operation)")

    while True:
        user_input = input("Enter Calculation or Command: ")
        
        if user_input in ["History", "history"]:
            show_history()
        elif user_input in ["Clear", "clear"]:
            clear_history()
        elif user_input in ["Exit", "exit"]:
            print("Thank You for using the Calculator")
            break
        else:
            calculate(user_input)

if __name__ == "__main__":
    main()