import Yachiyo_info
import os
#
\
\
\
\
\
# #str = string
# #int = number with out decimal
# #Floats = number with decimal
# #list
# #tuples = tup()
# #list = []
# #sets = set{}
# list = [1,2,3,4,]
# print(list)
# #CREATE FILE, DIR
# #os.getcwd : get file path
# #os.chdir : chose dir
# print(os.getcwd())
# os.removedirs("you're/yuri")
# os.makedirs("you're/yuri")
# os.remove("you're.")
# print(os.listdir())
# for path, dirname, filename in os.walk("/workspaces/new"):
#     print('path:',path)
#     print('dir name',dirname)
#     print('file:',filename)
#     print('------------------')
# welcome = ["Welcome to the world of programming!",
#            "Let's start coding together!",
#            "Coding is fun and rewarding!"]
# os.chdir("/workspaces/new")
# for range in welcome:
#     print(welcome.index(1, range), range)
\
\
\
\
# #FILE TXT READ
# n1 =open('exemple.txt', 'w')
# n2 =open('exemple2.txt', 'w')
# n1.close(),n2.close()
# # Encoding is the rule that converts text characters to bytes (for saving)
# #  and bytes back to text (for reading).
# #UTF-8: supports basically all languages and symbols, most recommended default.
# with open('exemple.txt', 'w+', encoding='utf-8') as nu1, open('exemple2.txt', 'w', encoding='utf-8')as nu2:
#     nu1.write('test exemple')
#     nu1.seek(0)
#     sizen2 = 1
#     whatisreading = nu1.read(sizen2)
#     while len(whatisreading)>0:
#         print(whatisreading,end='')
#         nu2.write(whatisreading)
#         whatisreading = nu1.read(sizen2)
\
#.join to join a str and a another str that repeat for each string
\
\
\

# with open('exemple1.txt', 'w+', encoding='utf-8') as my_file, open('exemple2.txt', 'w+', encoding='utf-8') as my_result:
#     #/n for next line
#     my_file.write('hello my name is\nbye\nhello again\n')
#     my_file.seek(0)

#     lf = 'hello'
#     # To unpack the line number and it text, chose the starting number that it count
#     #readlines to read all the file
#     words = my_file.readlines() #if you use readline, it will only read one line
#     #using my_file.readlines, you can search word by word
#     #if you use READLINE with out the s, it will read letter by letter
#     for i, line in enumerate(words, start=1):
#     #  i = which line, line = all the text of the line
#     #this is for the line str
#     #for line in my_file:

#         if lf in line:
#            i = str(i)
#            #                     line contain a /n, so dont need to add one
#            #f"{var1}...{var2}" it write the variable  
#            my_result.write(f"{i} {line.strip()}")
#            #since line has a /n, it takes end='' for not having a hole new line
#            print(i, line, end='')
\
\
\
\
\
# #USER ACCOUNT
# # for 1var: number of the line, 2var: the words in the line in the_file 
# # for 1var,2var in the_file:...
# def create_account(username,password,email):
#     with open('accounts.txt','r+', encoding='utf-8') as create:
#         info = create.read()
#         #strip() to remove all extra space of the end and start
#         #replace("what do you want to replace", "with what")
#         # "".join(text.split())   
#         #.split() to make each word have a space and identifying each of them
#         all = info.split()
        
#         #if the object is in the list:
#         if  username in all:
            
#             return print("Username already exist")
#         if email in all:
#             return print("email already exist")
#         create.write(f"{username}   {email}   {password}""\n")
#         return print("Created")
# def login(email,password):
#     with open('accounts.txt','r',encoding='utf-8') as account:
#         #readline to read the line, and readlines to read every line
#         readline = account.readlines()
#         print(readline)
#         print('in')
#         for line_num,user_info in enumerate(readline, start=1):
#             # print(line_num,user_info.strip())
#             if email in user_info.strip():
#                 print("found email")
#                 find = user_info.split()
#                 #all lists, sets, dicts, tuples start their number at 0
#                 username,useremail,userpassword = find[0],find[1],find[2]
#                 print(len(find))
#                 #len starts a 1, not 0
#                 if len(find) < 3:
#                     continue
#                 if userpassword == password:
#                     return print("Login succesful")
            
#         return print("email or password invalid")
# # create_account('cookie','cookie123','cookiefre@gmail.com')

# # login('cookiefre@gmail.com','cookie123')
\
\
##simple terminal commands
# python: to look pyhton file, or you can write the path
#   import sys, sys:system
#       sys.executable: where is the file
#       sys.version: python version
#   import pip, pip: package
#       pip install (package_name): download a package
#       pip show (package_name): information of the package
# import pip
# import sys
# print(sys.executable, sys.version)

# # 
\
\
\
# import datetime
# today = datetime.datetime.now()
##"%A": telling the week of the day, like monday...
##"%B": Name of the month
##"%D": the day
##"%Y": the year
##"%I": hour
##"%M": minute
##"%p": Am or Pm
# extra_format = today.strftime("%A,")
# print(today)
\
\
\
\
\
#auto parsing and renaming of mutiple file
# ####FAILED EXPEREMENT
# import os
# import re
# print(os.getcwd())
# # os.makedirs("osfile.txt")
# os.chdir("\\Users\\YL\\GitHub\\new\\osfile.txt")
# # os.makedirs("test1.txt"),os.makedirs("test2.txt"),os.makedirs("test3.txt")
# for f in os.listdir():
#     f = f.strip(".txt")
#     print(f)
#     f_name = ""
#     f_num = ""
#     for letters in f:
#         if letters.isalpha:
#             f_name.join(letters)
#         elif letters.isdigit:
#             f_num += letters

#     f_name = f_name.join()
#     f_num = f_num.join()
#     #.format to make it a path
#     print(f"{f_num}{f_name}".format)
\
\
\
\
\
\
# import csv
# with open("account.txt", "r", encoding="utf-8", newline="") as f:
#     # CSV NORMAL
#     #csv.reader to read in your format
#                                             #skipinitialspace to remove the space after the comma
#     csv_reader = csv.reader(f, delimiter=",", skipinitialspace=True)
#                                             #newline="" to prevent extra blank lines in output on Windows# you can use end="" to do the same thing
#     with open("x2.txt", "w+", encoding="utf-8", newline="") as f2:
#         # csv.writer("what file to import in", delimiter="what string would you put between them")
#         csv_writer = csv.writer(f2, delimiter="\t")
#         ## Delimiter \t writes tab-separated output.
#         for line in csv_reader:
#             csv_writer.writerow(line)
#         f2.seek(0)#need to go back, or it will read from the end

#         #this is where it sort and read the file as a dict
#         csv_dictreader = csv.DictReader(f2,delimiter="\t")
#         with open("x3.txt","w+",encoding="utf=8") as f3:
#             field_name = ["name","username","email","password"]
#                                             #You can use the original field name that it takes from the first line
#             csv_Dictwriter = csv.DictWriter(f3,fieldnames=csv_dictreader.fieldnames,delimiter="\t")
#             csv_Dictwriter.fieldnames
#             csv_Dictwriter.writeheader()
#             for lines in csv_dictreader:
#                 #to take it off
#                 del lines["email"]
                #it doesnt take the header off and the delimiter, so you'll need to fix that
#                 csv_Dictwriter.writerow(lines)
\
\
\
\
\
# import csv 
# with open("Cosmicinfo.txt","w+",encoding="utf-8") as cosmic_info:
#     fieldname = "name","age","hobbies"
#     yachiyiinfo = {"name": "yachiyo","age":"8000","hobbies":"sing",}
#     irohainfo = {"name":"iroha","age":"17","hobbies":"sing"}
#     kaguyainfo = {"name":"kaguya","age":"16","hobbies":"sing"}
#     infos = yachiyiinfo,irohainfo,kaguyainfo
#     # infos = dict.values(infos)
#     # print(infos)
#     # dict_reader = csv.DictReader(infos,fieldnames=fieldname,)
#     dict_writer =csv.DictWriter(cosmic_info,fieldnames=fieldname,delimiter="\t")
#     dict_writer.writeheader()
#     for line in infos:
#         print(line)
#         dict_writer.writerow(line)
# import csv
# with open("read_info.txt","w",encoding="utf-8")as reader:
#     with open("Cosmicinfo.txt","r",encoding="utf-8")as info:
#         #csv.Dictreader doesnt need fieldname
#         info_csv = csv.DictReader(info,delimiter="\t")
#         writer_csv = csv.DictWriter(reader,fieldnames=info_csv.fieldnames,delimiter=";")
#         #next to skip a line in this situation
#         name_age = []
#         next(info_csv)
#         for line in info_csv:
#             #append to add item to list
            
#             name_age.append(f"{line['name']} {line['age']}")
#             writer_csv.writerow(line)
#             print(name_age)
\
\
\
\
\
\
# ##DATETIME
# import datetime
# # #datetime.DATE
# # d =datetime.date.today()
# # #d.year : year
# # #d.month : month
# # #d.day : day
# # #d.weekday() : the day of the week from 0:monday - 6:sunday
# # #d.isoweekday() : the day of the week from 1:monday - 7:sunday
# # print(d.isoweekday())
# # #date.timedelta(days='num'): add attribut to the num
# # tdelta = datetime.timedelta(days=7)
# # print(d - tdelta)
# # birthday = datetime.date(2026,7,16)
# # #day until birthday
# # delta_answer = birthday - d
# # #how many day left, 
# # #its a delta, so you could add compliment like days...
# # print(delta_answer.total_seconds())
# # #delta_answer.total_seconds() convert to total second

# # #datetime.TIME()
# # #it give hour,minute,seconde, ms
# # t = datetime.time(16,36,23,10000)
# # print(t.minute)

# #datetime.DATETIME()
# import zoneinfo
#                     #year, month, date, hour, minute, seconde, ms
# dt = datetime.datetime(2026,6,7,8,16,43,1000)
# #datetime.datetime.today() : using your local tz
# #datetime.datetime.now() : make you able to chose your tz, default is your timezone
# #datetime.datetime.utcnow() : using the utc that you are, it will input the date and time
# dt2 = datetime.datetime.now(tz=zoneinfo.ZoneInfo("EST"))
# #you can grab a groupe or individual attributes
# print(dt.date(),dt.time())

# #because now(i'm) we are in a depository, the utc is set at 00:00
# #you can make time change to what utc you want or city
# nyc_tz = zoneinfo.ZoneInfo("America/New_York")
# nyc_time = dt.astimezone(nyc_tz)
# print(nyc_time)
# #dt.tzinfo : get the tzinfo , Need to have a timezone
# print(dt.tzinfo)
# #zoneinfo.available_timezones(): to print all timezone
# # print(zoneinfo.available_timezones())
# #normal format : .isoformat()
# dt.isoformat
# #to print your format:
# ##"%A": telling the week of the day, like monday...
# ##"%B": Name of the month
# ##"%D": The hole date d,m,y
# ##"%d": the day
# ##"%Y": the year
# ##"%I": hour
# ##"%M": minute
# ##"%p": Am or Pm
# ##"%z": time zone
# formated = dt.strftime("%d,%B %Y")
# print(formated)
# #convert a str to a date
# converted = datetime.datetime.strptime('07,June 2026', "%d,%B %Y")
# print(converted-)
# #.strftime(): convert a date to a string
# #.strptime(): convert a string to a date
\
\
\
\
\
\
# #Variable 
# #LEGB
# #Local, Enclosing, Global, Built-in
# #built-ins
# import builtins
# print(dir(builtins))
# #global exemple
# x = 'this is global'            
# def Local():
#     #to make it global :
#     #global x(the variable)
#     #Local exemple
#     x = 'this is local'
#     def Enclosing():
#         #to use Enclosing:
#         # nonlocal x
#         #local x(variable)
#         #Enclosing exemple
#         print(x)
#     Enclosing()
#     print(x)
# Local()
# print(x)
# # so local is something to his own function
# #global is a variable outside of function
# #enclosinf is the local variable of the fonction that he is in
\
\
\
\
\
\
# # #SORT
# # # li = [6,4,8,1,9,3,5]
# # # tu = (3,8,4,0,5)
# # # dic = {"age": "13","name":"bob","last_name":"y"}
# # # li.sort()
# # # #or
# # # li_s = sorted(li,reverse=True)
# # # #tuple and dict only work with sorted
# # # dic_s = sorted(dic)
# # # print(dic_s)
# # #Absolut value
# # li = [-2,-3,-4,1,5]
# # #to read only the key, not negations 
# # li.sort(key=abs)
# # li_s = sorted(li,key=abs)
# # print(li)
# #CUSTOM SORTING
# class employe():
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def __repr__(self):
#         return f"{self.name},{self.age},{self.salary}"


# e1 = employe("carl",13,2000)
# e2 = employe("bob",14,3000)
# e3 = employe("elli",12,1000)
# employe = [e1,e2,e3]

# def attribut(emp):
#     return emp.age
# from operator import attrgetter
# s_employe = sorted(employe, key= attribut) or sorted(employe, key= lambda e: e.age) or sorted(employe, key= attrgetter("name"))
# print(s_employe)
\
\
\
\
\
\
\
# # Try And Errror 
# #try to try the code that you want to run
# try:
#     print(e)
# #exception is for all error
# except Exception as prob:
#     print("there is a prob")
#     #print the error in simple format
#     print(prob)
# # specific error
# except ValueError as te:
#     #print something to the user
#     print("the vallue isnt correct")
# #if there is no error
# else:
#     print("no error")
# #always execute, even if there is or not errors
# finally:
#     print("runned")
\
\
\
\
\
\
\
# #__name__ and __main__
# #__name__ will print file name that is running
# #if its the main file(the file that you are running on), it will print main
# print("file name:" , __name__)
# #If you import it from another file, it will print the file name
# \
# #To confirm if the file is runned from the main, you can do this
# import Test_name
\
\
\
\
\
\
\
\
\
\
# #unittest, Testing unit
# import unittest
# import calc

# class calc(unittest.TestCase):
#     def calc_add(self):
#         result = 0
\
\
\
\
\
\
# #RANDOM
# import random
# #to have a random number betwen 0 and 1(not inclusive)
# r01 = random.random()
# #number 1-10
# r010 = random.uniform(1,10)
# #number int betwen 1-10
# r0010 = random.randint(1,10)
# #To get one choice answer from str
# cpk =["Kaguya","Iroha","Yachiyo"]
# ranstr = random.choice(cpk)
# # print(ranstr)
# #To have a list of choice
# ranstr10 = random.choices(cpk, k=10)
# # print(ranstr10)
# #And if you want to chose the probability
# #weights = [first str,sceond str,...]
# ranstr10prob = random.choices(cpk, weights=[20,10,5], k=10)
# # print(ranstr10prob)
# #To shufle number is
# shuf = random.shuffle(cpk)
# #To select special card and to not reselect
# #Use Sample
# samp = random.sample(cpk, k=3)
# print(samp)
\
\
\
\
\
\
\
\
# # #CLASS 
# # #Class is a like a function that let you variable be able to set attribut
# # class employee:
# #     #__init__ is like the initial 
# #     #you normaly use 
# #     #U need to put self as the variable that is getting attribut
# #     def __init__(self,first,last,pay):
# #         #we call those instance
# #         self.first = first
# #         self.last = last
# #         self.pay = pay
# #     def fullname(self):
# #         return f"{self.first} {self.last}"
# # emp1 = employee("jaydon","gooner",6700)
# # print(emp1.fullname())
# # print(emp1.__dict__)
# #So, the instance variable is the first to be talen then the class variable
# class variable:
#     #This is a class variable
#     var1 = 1
#     def __init__(self):
        
#         pass
#     def my_value(self):
#         return f"{self.var1} {variable.var1}" 
# m1 = variable()
# #This is a instance variable
# m1.var1 = 2
# print(m1.my_value())
\
\
\
\
\
\
# #Closure
# #quick recap
# def outer(msg):
#     message = msg
#     def inner():
#         print(message)
#     return inner
# #this makes the say_hi = inner, so you can run the function
# #And the good part is that you can set diffrent attribut for each
# say_hi = outer("hi")
# say_bye = outer("bye")
# #since can't instanly acces inner after closing the function
# #you will need to do a closure
# #It remembers the msg variable
# say_hi()
# say_bye()
#it works in classes too
\
\
\
\
\
\
\
# #Decorators

# def decorator_function(og_func):
#     def wrapper_func(*args,**kwds):
#         print(f"this executed before the function{og_func.__name__}")
#         return og_func(*args,**kwds)
#     return wrapper_func

# class decorator_class(object):

#     def __init__(self,og_func):
#         self.func = og_func
#     def __call__(self, *args, **kwds):
#             print(f"this executed before the function{self.func.__name__}")
#             return self.func(*args,**kwds) 

        
# @decorator_class
# def display():
#     print("hi")

# @decorator_class
# def display_info(name, age):
#     print(f"the name is {name} and the age is {age}")
# display()
# display_info("Iroha",17)

#Advance Decorator, you can find logging under this

from functools import wraps
def my_logger(og_func):
    import logging
    logging.basicConfig(filename=f"{og_func.__name__}.log", level= logging.INFO) 
    @wraps(og_func)   
    def wrapper(*args,**kwds):
        logging.info(f"ran with {args}args and {kwds}")
        return og_func(*args,**kwds)
    return wrapper

def timer(og_func):
    import time
    @wraps(og_func)   
    def wrapper(*args,**kwds):
        t1 = time.time()
        result = og_func(*args,**kwds)
        t2 = time.time() - t1
        print(f"{og_func.__name__} runned in {t2} sec ")
        return result
    return wrapper
@timer
@my_logger
def display_info(name:str,age:int):
    import time
    time.sleep(1)
    print(f"my name is {name} and i'm {age}")
display_info("Yachiyo",8000)

















\
\
\
\
\
\
\
\
\
# import logging
# #There are 5 level of logging
# #You can't acces lower level, only higher 
# #DEBUG: Detailed information, only when probleme occure
# #INFO: confirmation that things are working as expected
# #WARNING: Indicate that something unexpected happened,or indicative of some problem in the near future(e.g. 'disk space low'). The software is still working a s expected.
# #Error: Due to a more serious problem, the software has not been able to prefore some function.
# #CRITICAl: A serious error that may indicate the program it self not even be able to continue runnnig
# logging.basicConfig(filename = "Log.txt",level = logging.INFO, format=None)

# \
# \
# \
# \
# \
# \
# \

# class charater:
#     def __init__(self,age):

#         self.name = self
#         self.age =age

# bob = charater(15)
# #Please head to the file "character_log.py"
# import character_log
# character_log.charater_config("yachiyo",8000, "singing")