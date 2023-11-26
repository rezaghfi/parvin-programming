a = 1
b= 3
c = 10
d = max(a,b,c)
print(d)

def moghayese(adad1, adad2, adad3):
  if(adad1 > adad2 and adad1 > adad3):
    print("عدد یک بزرگتر است")
  elif(adad2 > adad1 and adad2 > adad3):
    print("عدد دوم بزرگتر است")
  elif(adad3 > adad1 and adad3 > adad2):
    print("عدد سوم بزرگتر است")
  elif(adad1 == adad2 and adad1 == adad3):
    print("سه عدد باهم برابراند")
  else:
    print("دو عدد بزرگتر مساوی اند")

# صدا زدن
a = int(input("adad1: "))
b = int(input("adad2: "))
c = int(input("adad3: "))
moghayese(a, b, c)