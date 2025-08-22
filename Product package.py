def package_product(name,price,quantity):
 total = price*quantity
 return(name , price , quantity,total)
product1=package_product("tea",15,100)
product2=package_product("pepsi",25,100)
x=input("Enter the product: ")
if x=="tea":
 print("NO")
 print(f"Name:{product1[0]}")
 print(f"Price:{product1[1]}")
 print(f"Quantity:{product1[2]}")
 print(f"Total:{product1[3]}")
else :
 if x=="pepsi":
  print("NO")
  print(f"Name:{product2[0]}")
  print(f"price:{product2[1]}")
  print(f"Quantity:{product2[2]}")
  print(f"Total:{product2[3]}")
