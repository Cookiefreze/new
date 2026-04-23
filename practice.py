import Yachiyo_info
import os

\
\
\
\
\
##str = string
##int = number with out decimal
##Floats = number with decimal
##list
##tuples = tup()
##list = []
##sets = set{}
# list = [1,2,3,4,]
# print(list)
##CREATE FILE, DIR
##os.getcwd : get file path
##os.chdir : chose dir
#print(os.getcwd())
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



             

            


            


