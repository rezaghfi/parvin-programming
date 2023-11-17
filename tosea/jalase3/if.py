# دستور شرطی


#  دندانه گذاری باید کدنویسی رعایت شود
weather = "rainy"
v = 1
if(weather == "sunny"):
  print("برو مدرسه")
else:
  print("مدرسه نرو")

# عملگر ها ی مقایسه ای < > <= >= != ==

if(weather != "sunny"):
  print("مدرسه نرو")
else:
  print("مدرسه برو")

moadel = 15.1

if(moadel >= 12):
  print("قبول")
else:
  print("مردود")

sen = -50

# عملگر منطقی and or not
if(sen >= 1 and sen <= 10):
  print("kodak")
elif(sen >10 and sen <20):
  print("nojavan")
elif(sen >= 20 and sen < 30):
  print("javan")
elif(sen >= 30 and sen <= 60):
  print("meansal")
elif(sen >60 and sen < 200):
  print("per")
else:
  print("wrong number")