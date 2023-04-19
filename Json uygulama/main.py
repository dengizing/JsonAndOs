import json
import os

class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password =password
        self.email =email



class UserRepository:
    def __init__(self):
        self.users =[]#boş bir kullanıcı dosyası
        self.isLoggedIn=False
        self.currentUser = {}

        #load users from.json file
        self.loadUser()

    def loadUser(self):
        if os.path.exists('user.json'):
            with open('users.json','r',encoding='utf-8')as file:
                users=json.load(file)
                for user in users:
                    user =json.loads(user)
                    print(user['username'])
                    newUser =User(username=user['username'],password=user['password'],email=user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user: User):#ullanıcı oluşturmak için
        self.users.append(user)
        #self.savetoFile():bir kayıt işlemi yaptığımızda bu yapılan kayıt işlemi ile birlikte listeyi dosyaya kayıt etmekdir.
        print('Kullanıcı oluşturuldu')
    def login(self,username,password):#giriş bilgisi
        for user in  self.users:
            if user.username ==username and user.password ==password:
                self.isLoggedIn =True
                self.currentUser =user
                print('logn yapıldı. ')
                break
    def logout(self):
            self.isLoggedIn = False
            self.currentUser ={}
            print('çıkış yapıldı')
    def identity(self):
            if self.isLoggedIn:
                print(f'username: {self.currentUser.username}')
            else:
                print('giriş yapılmadı')

    def savetoFile(self):#dosyaları alıp kaydedicek
        list=[]

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json','w') as file:
            json.dump(list,file)
repository = UserRepository()
while True:
    print('Menü'.center(50,'*'))
    secim =input('1-Register\n2-Login\n3-Logout\n4-identity\n5-Exit\nseçiminiz:')
    if secim=='5':
        break
    else:
        if secim=='1':
            username = input('username: ')
            password = input('password: ')
            email = input('email: ')

            user=User(username=username,password=password,email=email)
            repository.register(user)
            print(repository.users)

             #register
        elif secim=='2':
            username=input('username: ')
            password=input('password: ')
            repository.login(username,password)
             #logput
        elif secim =='3':
           repository.logout()
           #display username

        elif secim =='4':
            repository.identity()
        else:
            print('yanlış seçim')

