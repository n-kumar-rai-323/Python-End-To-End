# 1. write a python program to display a user entered name followed by good afternoon using input () function
str = input("Enter your text ")
print(f"Good Afternoon {str}")


# 2. write a program to fill in a letter templae given below with name and date.
letter = """ 
Dear  name you are selected ! date
"""
newLetter = letter.replace("name", "Nishan Kumar Rai").replace("date", "2024/05/10")
print(newLetter)



# 3. write a program to detect double space in a string?
thar = "Sharmila  Rai"
newSpace =thar.find("  ")
print(newSpace)


# 4. replace the double space form problem 3 with single spaces. 
thir2 = "Nishan  Rai"
repToDobTosing= thir2.replace("  ", " ")
print(repToDobTosing)



# 5. write a program to format the following letter using escape sequence characters.
letter_two = "\"Dear Nishan, this python course is nice. Thank you ! \""
print(letter_two)