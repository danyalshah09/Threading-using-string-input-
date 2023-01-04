import threading
def main():
    string = ""  # Declare the global variable
    def input_thread():
        global string  # Access the global variable
        while True:
            try:
                # Take input from user
                string = input("Enter an input string: ")
                if not string.isalpha():
                    raise ValueError("Exception Found!Input Alphabetical characters only")
            except ValueError as e:
                # Handle invalid input
                print(e)
            else:
                break
        # Notify other threads to start their work
        reverse_thread.start()
        capital_thread.start()
        shift_thread.start()

    def reverse_thread():
        global string  # Access the global variable
        try:
            # Reverse the string
            reversed_string = string[::-1]
            print("---------------------------------")

            print("Reversed string:", reversed_string)
            print("---------------------------------")
        except Exception as e:
            # Handle exceptions
            print("Exception occurred in reverse thread:", e)

    def capital_thread():
        global string  # Access the global variable
        try:
            # Capitalize the string
            capitalized_string = string.upper()
            print("Capitalized string:", capitalized_string)
            print("---------------------------------")

        except Exception as e:
            # Handle exceptions
            print("Exception occurred in capital thread:", e)

    def shift_thread():
        global string  # Access the global variable
        try:
            # Shift each character of the string by two
            shifted_string = ""
            for char in string:
                if not char.isalpha():
                    raise ValueError("Input must be a string containing only alphabetical characters")
                shifted_string += chr(ord(char) + 2)
            print("Shifted string:", shifted_string)
            print("---------------------------------")

        except ValueError as e:
            # Handle exceptions
            print("Exception occurred in shift thread:", e)


    # Create the threads
    input_thread = threading.Thread(target=input_thread)
    reverse_thread = threading.Thread(target=reverse_thread)
    capital_thread = threading.Thread(target=capital_thread)
    shift_thread = threading.Thread(target=shift_thread)

    # Start the input thread
    input_thread.start()

    # Wait for all threads to complete
    input_thread.join()
    reverse_thread.join()
    capital_thread.join()
    shift_thread.join()

if __name__ == "__main__":
    main()