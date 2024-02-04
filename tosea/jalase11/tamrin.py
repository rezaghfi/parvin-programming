
tosea = int(input("نمره توسعه رو وارد کن"))
web = int(input("نمره وب رو وارد کن"))
arab = int(input("نمره وب رو وارد کن"))

def moadel(tosea, web, arab):
  return (2*tosea + 2* web + arab)/5

m = moadel(tosea, web, arab)

print("معدل هست:", m)

def model2(tosea, web , arab):
  print((2*tosea+ 2* web+ arab)/5)