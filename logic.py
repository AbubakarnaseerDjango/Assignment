import json

# User
def user():
  file = open("users.json","r")
  x = file.read()
  data = json.loads(x)
  key = data[0].keys()
  print(key)
  k = input("Enter the key you want to search = ")
  val = input("Enter a value = ")
 
  for i in data:
    if k in key:
      if val == str(i[k]):
       print("Value is =", i)
      else:
        print("This value is not avilable")
        break
    else:
      print("this key is not available ", k)
      break

# Tickets
def ticket():
    # json 
    file = open("tickets.json","r")
    x = file.read()
    data = json.loads(x)
    
    
    #list of searchable values
    key = data[0].keys()
    print(key)
    # list of values
    k = input("Enter the key you want to search = ")
    
    val = input("Enter a value = ")
    for i in data:
      if k in key:
        if val == str(i[k]):
          print("Value is =", i)
      else:
        print("This key is not availabel",k)
        break

# organiztions

def organizations():
  file = open("organizations.json","r")
  x = file.read()
  data = json.loads(x)


  key = data[0].keys()
  print(key)
  k = input("Enter the key you want to search = ")
  
  val = input("Enter a value = ")
  for i in data:
    if k in key:
      if val == str(i[k]): 
        print("Value is = ",i)
    else:
        print("this key is not available ", k)
        break
    

k="" 
while k != "quit":
    print("Welcome to zendesk search")
    print("Type quit to exit anytime,press 'Enter' to continue")
    print("             *press 1 to zendesk search")
    
    val = int(input("Select 1) Users or 2) Tickets or 3) Organizations = "))
    if val == 1:
        user()
    elif val == 2:
        ticket()
    elif val == 3:
        organizations()
    else:
        print("Wrong Input")
    k=input("             *If u want to continue press 'Enter' if u want to terminate print 'quit' ")
    