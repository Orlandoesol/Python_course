'''
Continuación clase de poo

'''
class User:
    userName = ""
    email = ""
    password = ""

user1 = User()
user2 = User()
user3 = User()



user1.userName = "JohnDoe"
user1.email = "jhondoe@dominio.com"
user1.password = "123456"

user2.userName = "JaneFonda"
user2.email = "fondajane@dominio.com"
user2.password = "Fj123456"

user3.userName = "AnibalSmith"
user3.email = "colonel@dominio.com"
user3.password = "Ateam1980"
print("\n***** Usuario 1********")
print(user1.userName)
print(user1.email)  
print(user1.password)
print("\n***** Usuario 2********")
print(user2.userName)
print(user2.email)
print(user2.password)
print("\n***** Usuario 3********")
print(user3.userName)
print(user3.email)
print(user3.password)