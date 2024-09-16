stack = []

while True:
    choice = input("Enter 'push' to add an element, 'pop' to remove the top element, 'delete' to remove a specific element, or 'quit' to exit: ")

    if choice.lower() == 'push':
        element = input("Enter the element to push: ")
        stack.append(element)
        print("Element pushed successfully.")
        print("current stack:",stack)

    elif choice.lower() == 'pop':
        if stack:
            popped_element = stack.pop()
            print("Popped element:", popped_element)
            print("current stack:",stack)
        else:
            print("Stack is empty.")

    elif choice.lower() == 'delete':
        delete_element = input("Enter the element to delete: ")
        if delete_element in stack:
            stack.remove(delete_element)
            print("Element deleted successfully.")
            print("current stack:",stack)
        else:
            print("Element not found in the stack.")

    elif choice.lower() == 'quit':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")