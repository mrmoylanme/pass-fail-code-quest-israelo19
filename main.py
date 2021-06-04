def problem1():
  with open("inputs/Prob01.in.txt", "r") as f:
    grades = f.read()
    grades_int = [int(x) for x in grades.split()]
    #print(sum(grades_int)) 
#add if statements, conditions to see if a grade is higer than 70, if so pass otherwise fail.
  if (grades_int[0] >= 70):
    print("PASS")
  else:
      print("FAIL")

  if (grades_int[1] >= 70):
    print("PASS")
  else:
      print("FAIL")

  if (grades_int[2] >= 70):
    print("PASS")
  else:
      print("FAIL")
  
  if (grades_int[3] >= 70):
    print("PASS")
  else:
      print("FAIL")

  if (grades_int[4] >= 70):
    print("PASS")
  else:
      print("FAIL")

  if (grades_int[5] >= 70):
    print("PASS")
  else:
      print("FAIL")

  if (grades_int[6] >= 70):
    print("PASS")
  else:
      print("FAIL")
pass
problem1()
