#!C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe

import cgi

def sum_of_digits(number):
    digit_sum = sum(int(digit) for digit in str(number))
    return digit_sum

form = cgi.FieldStorage()
number = int(form.getvalue("number"))

print("Content-type:text/html\r\n\r\n")
print(f"<html><head><title>Sum of Digits</title></head><body>")
print(f"<h1>The sum of digits in {number} is {sum_of_digits(number)}.</h1>")
print("</body></html>")

import cgi
import cgitb
import mysql.connector
import random
cgitb.enable()

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def dice_rolling_game(dices, max_value, tries):
    random.seed()
    best_result = 0
    for _ in range(tries):
        current_result = sum(random.randint(1, max_value) for _ in range(dices))
        best_result = max(best_result, current_result)
    return best_result

def connect_to_database():
    connection = mysql.connector.connect(
        #host="localhost",
        #user="yourusername",
        #password="yourpassword",
        #database="yourdbname"
    )
    return connection

def save_user_input(user_input):
    connection = connect_to_database()
    cursor = connection.cursor()
    query = "INSERT INTO user_input (input_data) VALUES (%s)"
    cursor.execute(query, (user_input,))
    connection.commit()
    cursor.close()
    connection.close()

form = cgi.FieldStorage()

if "number" in form:
    number = int(form.getvalue("number"))
    result = sum_of_digits(number)
    save_user_input(number)
    print("Content-type:text/html\r\n\r\n")
    print(f"<h1>Sum of Digits: {result}</h1>")
elif "dices" in form and "max_value" in form and "tries" in form:
    dices = int(form.getvalue("dices"))
    max_value = int(form.getvalue("max_value"))
    tries = int(form.getvalue("tries"))
    result = dice_rolling_game(dices, max_value, tries)
    save_user_input(f"{dices}, {max_value}, {tries}")
    print("Content-type:text/html\r\n\r\n")
    print(f"<h1>Best Result: {result}</h1>")
else:
    print("Content-type:text/html\r\n\r\n")
    print("<h1>Error: Invalid input</h1>")
