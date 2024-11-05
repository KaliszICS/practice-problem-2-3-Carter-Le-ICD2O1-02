

def q1(): 
  #Write Assignment code here
  wor = input("In: ")
  if (wor.endswith("ey")):
    print("-eys")
  elif(wor.endswith("y")):
    print("-ies")
  elif(wor.endswith("ife")):
    print("-ives")
  else:
    print("-s")



def q2(): 
  #Write Assignment code here
  num = float(input("In: "))
  if num > 0:
    num = int(num)
    print (str(num) + " is positive")
  elif num < 0:
    num = int(num)
    print (str(num) + " is negative")



def q3(): 
  #Write Assignment code here
  bum3 = float(input("Input a number: "))
  bum2 = float(input("Input a number: "))
  bum1 = float(input("Input a number: "))
  if bum3 == bum2 == bum1:
    print("Equilateral")
  elif bum1 == bum2 or bum2 == bum3 or bum3 == bum1:
    print("Isosceles")
  elif not bum3 == bum2 == bum1:
    print("Scalene")
  elif (bum1 + bum2) == bum3 or (bum2 + bum3) == bum1 or (bum3 + bum1) == bum2:
    print("No triangle")





  



#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()
