def auth():
 p=input("Введите пароль:")
 c=input("Подтвердите пароль:")
 if p!=c:print("Пароли не совпадают")
 else:
  a=input("Введите пароль для авторизации:")
  if a==p:print("Access")
  else:print("Denied")

auth()