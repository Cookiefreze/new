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
list = [1,2,3,4,]
print(list)
##CREATE FILE, DIR
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
#     for i, line in enumerate(my_file, start=1):
#     #  i = which line, line = all the text of the line
#     #this is for the line str
#     #for line in my_file:

#         if lf in line:
#            i = str(i)
#            #                     line contain a /n, so dont need to add one
#            #f"{var1}...{var2}" it write the variable  
#            my_result.write(f"{i} {line.strip()}")
#            #since line has a /n, it takes end='' for not having a space
#            print(i, line, end='')
#USER ACCOUNT
with open('accounts', 'w+'):
    pass
def create_account(username,password,email):
    with open('accounts','w') as create:
        create.write(f"user name: {username}    password: {password}    email: {email}"/n)
def login(email,password):
    with open('accounts','r') as account:
        for line, find_user in enumerate(account, start = 1):
            if find_user == email:
                where_is_password = find_user.find(password)
                print(where_is_password)
create_account('cookie,','cookie123','cookiefre@gmail.com')
login('cookiefreze@gmail.com','cookie123')