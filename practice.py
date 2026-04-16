import Yachiyo_info
import os
print(os.getcwd())
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
n1 =open('exemple.txt', 'w')
n2 =open('exemple2.txt', 'w')
n1.close(),n2.close()
with open('exemple.txt', 'r+') as nu1, open('exemple2.txt', 'w')as nu2:
    nu1.write('test exemple')
    nu2.seek(0)
    sizen2 = 1
    whatisreading = nu1.read(sizen2)
    while len(whatisreading)>0:
        print(whatisreading,end='')
        nu2.write(whatisreading)
        whatisreading = nu1.read(sizen2)

