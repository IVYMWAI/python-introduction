print("Hello World")
print("Hello World")
x ="IVY"
print("IVY")
y = "she is a pretty girl"
print("IVY" and "she is a pretty girl")
print("     /")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print("My name is Ivy")
print("I am 21 years old")
print("I am also an undergraduate student")
print("I am 5.1 feet tall with a nice well shaped butt")
print("I am passionate about business,investment")
print("and everything to do with money")
print("yi","er","san")
print("si","wu","liu")
print("qi","ba"and "jiu")
print(1,2,3,4,5)
print(6,7,8,9,10)
print(11,12,13,14,15)
Character_name ="john"
character_age ="23"
is_male = True
print("there was once a man named" + Character_name +",")
print("he was very handsome")
print(Character_name + "was very hardworking ")
print("he was " + character_age)
Character_name ="Gibson"
print("i dont know why"  + Character_name +  "makes this so hard")
print(Character_name  +  "kinda amazing")
print("i love going out")
print("and having fun")
print("do you know Chinese")
print("have you ever been to China")
Character_name ="China"
print("today was my first day in " + Character_name+ ",")
print("I would love to visit " + Character_name +",")
Character_name = "day"
print("we can call it a " + Character_name +", ")
print("what "+ Character_name + "is it")
print("Good morning")

print("Giraffe Academy")
print("Giraffe\nAcademy")
print("ivy waithira")
print("ivy\nwaithira")
print("ivy waithira")
print("ivy\nwaithira")
print("Giraffe\nAcademy")
phrase= "Giraffe Academy"
print(phrase)
#concatenation ,that is appending a string onto another
phrase ="Giraffe Academy"
print(phrase + "is elite")
#functions..small lines of code which perform specific operations in Python
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase[5])
print(phrase[9])
print(phrase.index("G"))
print(phrase.index("A"))
print(phrase.index("c"))
print(phrase.replace("Giraffe","Lion"))
print(phrase.replace("Academy","Highschool"))
#working with numbers
print(2)
print(3.142)
print(3*2)
print(4+11.90)
my_number =7
print(my_number)
print(str(my_number))
print(str(my_number)+ (" is my favorite number"))
print(pow(3,3))
print(max(5,10))
print(max(2,4))
from math import*
print(sqrt(81))
#getting input from users to make your program more interactive
name =input("Enter your name: ")
age = input("Enter your age")
school= input("Enter your school")
print("Hello" + name + " You are " +age +"and in the great" + school +"!")
num1 =input("Enter a number: ")
num2 = input("Enter another number: ")
result =int(num1)+ int(num2)
print(result)
num3 = input("Enter a number: ")
num4 =input("Enter another number: ")
result =float(num3) +float(num4)
print(result)
#Madlib games
print("Roses are red")
print("Violets are blue")
print("It is a cruel world")
color =input("Enter a color: ")
plural_noun =input("Enter a plural_noun: ")
celebrity= input("Enter a celebrity: ")

#print("Roses are " + color)
#print(plural_noun + "are blue")
#print("I love " + celebrity)

#color =input("Enter a color: ")
#plural_noun=input("Enter a plural_noun: ")
#celebrity=input("Enter a celebrity: ")

#print("Roses are " + color )
#print(plural_noun + "are yellow")
#print("I love " + celebrity)

#day =input("Enter a day: ")
#weather =input("Enter weather")
#plural_noun =input("Enter a plural_noun")
#print("Today is " + day)
#print("It might be " + weather)
#print("I carried an  " + plural_noun)

#name= input("Enter a name: ")
#city =input("Enter a city: ")
#complexion =input("Enter complexion")
#print("There was once a man called " + name)
#print("He lived in " + city)
#print("He was very " + complexion)
#List  and list functions
friends =["Jane","Amber","Ivy","Peter","Ivy","Amber","James","Ivy","Amber","Ivy"]
#print(friends)
#print(friends[2])
#print(friends[3])
#print(friends[0])
#print(friends[1])
#print(friends[1:3])
#EXTEND,APPEND ,INSERT,REMOVE,POP,INDEX,COUNT,SORT,REVERSE,COPY,LIST FUNCTION
#lucky_numbers =[1,2,3,4,5,6]
#friends.extend(lucky_numbers)
#print(friends)
#friends.append("Creed")
#print(friends)
#friends.insert(1,"Kelly")
#print(friends)
#friends.remove("James")
#print(friends)
#print(friends.index("Ivy"))
#print(friends.index("Peter"))
#print(friends.index("Amber"))
#print(friends.count("Amber"))
#print(friends.count("Ivy"))
#friends.sort()
#print(friends)
#lucky_numbers=[1,88,34,42,59,6,78,]
#lucky_numbers.sort()
#print(lucky_numbers)
#numbers=[10,33,2,17,96,106,280,1000]
#numbers.sort()
#print(numbers)
#friends2 = friends.copy()
#print(friends2)
#tuples used to store ata that cannot be mutated
#coordinates =(4 ,5), (1 ,3), (4,8), (9,5)
#print(coordinates[2])
#Functions;collection of code which performs a specifc task
#Def(calling the function)
#    print("Hello User")
#print("Top")
#say_hi()
#print("Bottom")
#def sayhi(name,age):
#    print("Hello " + name + "You are  "+ age)
#sayhi("Mike" ,"35")
#sayhi("Steve","41")
#Return Staement,allows Python to return information from a function
#def cube(num):
 #   return num*num*num
#print(cube(3))
#print(cube(2))
#print(cube(5))
#def cube(num):
#    return num*num*num
#result =cube(4)
#print(result)
#If statement,helps a program makes decisions(creating a boolean variable)
#if is a condition(true or false)
#Else(otherwise)
#is_male =True
#if is_male:
 #   print("You are a male")
#else:
#    print("You are not a male")

#is_male =True
#is_tall =False
#if is_male and is_tall:
#    print("You are a tall male")
#else:
#    print("You are either not male or not tall or both")
#is_male =False
#is_tall =False
#if is_male and is_tall:
#    print("You are a tall male")
#elif is_male and not(is_tall):
#    print("You are a short male")
#elif not (is_male) and not is_tall:
#    print("You are not a  male and are tall")
#else:
#    print("You are either not male or not tall or both")
#If statements and comparisons
#def max_num(num1, num2, num3):
 #   if num1>= num2 and num1 >= num3:
 #       return num1
  #  elif num2 >= num1 and num2 >=num3:
  #          return num2
  #  else:
   #         return num3

#print(max_num(300,40,5))
#Building a basic calculator
#num1 =float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter second number: "))
#if op == " + ":
#    print(num1 + num2)
#elif op == " -":
#    print(num1- num2)
#elif op ==" / ":
#    print(num1/num2)
#elif op == " * ":
#    print(num1*num2)
#else: 
#    print("Invalid Operator")

#Dictionaries
#special characters in Pyhton which allows us to store information in what is called key value pairs
#creating dictionaries in Python we use curly brackets
#"Jan" is a key,when we print out the key it goes to the dictionary and gives us the full name ofthat key
#monthconversions = {
 #   "Jan" : "January",
 #   "Feb" : "February",
  #  "Mar" : "March",
  #  "Apr" : "April",
   # "May" : "May",
   # "Jun" : "June",
   # "Jul" : "July",
   # "Aug" : "August",
   # "Sep" : "September",
   # "Oct" : "October",
   # "Nov" : "November",
   # "Dec" : "December",
#}
#print(monthconversions["Aug"])
#print(monthconversions.get("Dec"))
#print(monthconversions["Nov"])
#print(monthconversions["Feb"])

#WHILE LOOPS
#allows us to loop through a block of code multiple times
#we can create integers
#i = 1
#while i <= 10:
 #   print(i)
 #   i += 1
#print("Done with loop")

#Building a basic guessing game
#secret_word = "giraffe" 
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess != secret_word and not (out_of_guesses):
 #   if guess_count < guess_limit:
 #    guess = input("Enter guess: ")
  #   guess_count += 1
  #  else:
  #        out_of_guesses =True
#if out_of_guesses:
 #   print("Out of guesses, You lose!")
#else:
#    print("You win!")
#print("I am so proud of you Ivy ")
#print("do not give up on yourself")
#print("I will make mad bag this year")
#print("Good morning!")

#FOR LOOPS SPECIAL TYPE OF LOOP in python which alllows one to loop over a various collection of items.
#for letter in "Giraffe Academy":
#   print(letter)
#friends = ["Kelvin","Grace","Hannah","Angel"]
#for friend in friends:
 #  print(friend)
#for index in range(5):
#   if index == 0:
 #     print("first iteraion")
 #  else:
 #     print("not first iteration")
#EXPONENT FUNCTION 
#print(2**3)
#def raise_to_power(base_num,power_num):
 #  result = 1
 #  for index in range(power_num):
 #     result =result * base_num
 #  return result

#print(raise_to_power(3, 4))

#2D lists and nested loops accesing elements in a 2d list
#number_grid =[
#[1,2,3],
#[4,5,6],
#[7,8,9],
#[0]
#]
#print(number_grid[0][0]) 
#print(number_grid[2][1])
#for row in number_grid:
   #print(row)
   #for col in row:
   #   print(col)

#BUILD A TRANSLATOR
#"Giraffe language"
#"vowels -> g"
#def translate(phrase):
 #  translation = ""
  # for letter in phrase:
  #  if letter in "AEIOUaeiou":
   #   translation = translation +"g"
   #else:
   #      translation = translation + letter
   #return translation
#print(translate(input("Enter a phrase: ")))

#COMMENTS a line of code that is not going to be printed by Python,commenting out a line of code
#print("comments are fun")
#coding is fun

#TRY EXCEPT allows you to try out a piece of code
#try:
  #  number = int(input("Enter a number"))
   # print(number)
#except:
 #  print("Invalid input")
 
 #READING FILES using the python read command ie reading external files in python
 #r read,w write,a append,r+ read and write
#excel_file =open("Mwichirira.xls" ,"r")
#print(excel_file.readable())
#excel_file.close()
#WRITING AND APPENDING FILES
#employee_file = open("employee.txt" ,"a")
#employee_file.write("Tpby - human resources")
#employee_file.close()
#(when you run this code a Toby is added  in the list)
#Modules and Pip.A module is a python file that we can import into our current python file.
#most useful python modules
#python docs
#pip is used to store python modules
#import docx
#CLASSES AND OBJECTS
#they make your code more organized,eg creating another data type
#from student import student
#student1 =student("Jim", "Business", 3.1,False)
#print(student1.name)
#Building a multiple choice quiz
#OBJECT FUNCTIONS
#INHERITANCE creating a function inside a class and then inherit those attributes
#Chef is the class and inside this class we have three functions:salad,chicken and special dish
#from Chef import Chef
#myChef =Chef()
#myChef.make_chicken()
#Python interpretor
print("five hours done!")


















   
































