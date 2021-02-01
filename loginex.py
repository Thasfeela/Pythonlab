class LoginEx (Exception) : pass
try: 
  x="python"
  a=input("Enter username :")
  b=input("Enter password :")
  if a!=x:
    raise LoginEx ("Invalid Username")
  print("Login successful")
except LoginEx as e:
  print(e)