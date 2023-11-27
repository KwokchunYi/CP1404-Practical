"""
1. Write code that asks the user for their name, then opens a file called "nome. txt" and writes that name to
Remember to close yur file.
"""
FILENAME = "name. txt"
name = input("Enter name: ")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file. close()


""" 
2.(In the same file, but as if it were a separate program) Write code that opens
"name.txt" and reads the name (as above) then prints,"Your name is Bob" (or whatever the name is in the fill
"""
FILENAME = "name.txt"
in_file = open(FILENAME)
text = in_file.read()
print("Your name is " + "" + text)
in_file.close()

"""
3.Write code that opens "Numbers.txt",reads only the first two numbers and adds them together then print
result, which should be... 59.
"""
total = 0
FILENAME = "number.txt"
in_file = open(FILENAME)
for i in  range(0,2):
    number = in_file.readline()
    total = total + int(number)
print(total)
in_file.close()

"""
4.Now write a fourth block of code that prints the total for all lines in numbers.txt
or a file with any number of numbers."""
total = 0
FILLNAME = "numbers.txt"
in_file = open(FILENAME)
numbers = in_file.readline()
for number in numbers:
    total += int(number)
print(total)
in_file.close()
