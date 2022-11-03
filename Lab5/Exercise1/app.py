from Exercise1 import utils

#b) Write a module named app.py.
# When this module is run, it will run in an infinite loop, waiting for inputs from the user.
# The program will convert the input to a number and process it using the function process_item implented in utils.py.
# You will have to import this function in your module. The program stops when the user enters the message "q".
while True:
    print("Enter a number:")
    given_input=input()
    if given_input!='q':
        try:
            next_prime= utils.process_item(int(given_input))
            print(f"Least prime number greater than {given_input} is {next_prime}")
        except:
            print("Input is not a number!")
    else:
        print("q given. Module will stop")
        exit()