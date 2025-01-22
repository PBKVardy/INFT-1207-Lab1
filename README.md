# INFT-1207 Lab 1

#### Group Names: Rehan Zaffar, Kyle Vardy

#### Description:
> The password generator lab from INFT-1207.This program generates random passwords for the user taking user input for how many
special characters, letters, and numbers the user wants in the password.

#### Date: 
> January 22nd, 2025

# Execution
run the program by typing `python3 src/password_generator.py` in the terminal

# Explanation
There are 6 functions in the program:

1. gen_random_num: This function is used to generate random numbers and puts it in a string array.
2. gen_random_letter: This function is used to generate random letters and puts it into a string array.
3. gen_random_special: This function is used to generate random special characters and puts it into a string array.
4. collect_int: This function collects and integer and if it isn't an integer it continues to ask the user until there is a valid int
5. randomize_password_order: Takes a string and turns it into a list, then shuffles this list and turns it into a string
6. menu: This is where all the main process happen. 
