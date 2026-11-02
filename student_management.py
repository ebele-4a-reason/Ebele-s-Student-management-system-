print("EBELE STUDENT MANAGEMENT SYSTEM👨‍💻")
print()

choice = 0
student_no = 0
student = []
while choice != 9:
  print()
  print("******MAIN MENU******")
  # properties of main MENU
  print()
  print("1.REGISTER STUDENT")
  print("2.VIEW ALL STUDENTS")
  print("3.SEARCH STUDENT")
  print("4.VIEW STUDENT RESULT")
  print("5.UPDATE STUDENT")
  print("6.DELETE STUDENT")
  print("7.SCHOOL STATISTICS")
  print("8.ABOUT SYSTEM")
  print("9.EXIT")
  
# asks user to choose a menu
  print()
  
  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid input, Enter a number.")
    continue
  if choice == 1:
    # if the user chooses option 1 then it prints a message
   name = (input("ENTER STUDENT'S FULL NAME: "))
   print()
   age = 0
   while age < 10 or age > 30:
     
    try:
     age = int(input("ENTER STUDENT'S AGE: "))
    except ValueError:
     print("Invalid input, Enter a number")
     age = 0 
     continue
    if age < 10:
       print("Invalid age. Student must be at least ten years old")
    elif age > 30:
       print("Invalid age. Student must be at most thirty years")
   print() 
   gender = input("Enter Student Gender(M/F): ")
   while gender.upper() != "M" and gender.upper() != "F":
    print("Invalid Gender, Please Enter M(Male) or F(Female)")
    gender = input("Enter Student Gender(M/F): ")
   if gender.upper() == "M":
      print("Gender: Male")
   elif gender.upper() == "F":
      print("Gender: Female")
   print()
   clas = input("Enter Student's Class: ")
  # generating student Id
   print()
   student_no += 1
   student_id = "STU00"+str(student_no)
   print(student_id)
   print()
   m_score = -1
   while m_score < 0 or m_score > 100:
    try:
     m_score = float(input("Enter Student Mathematics Score(0-100): "))
 
    except ValueError:
      print("Invalid Score, score must be a number")
      m_score = -1
      continue
    if m_score < 0:
      print("Invalid score, score must not be less than zero.")
    elif m_score > 100:
      print("Invalid Score, score must not be greater than 100 ")
   e_score = -1
   while e_score < 0 or e_score > 100:
    try:
     e_score = float(input("Enter Student English Score(0-100): "))
 
    except ValueError:
     print("Invalid Score, score must be a number")
     e_score = -1
     continue
      
    if e_score < 0:
      print("Invalid score, score must not be less than zero.")
    elif e_score > 100:
      print("Invalid score, score must not be greater than 100.")
      
   p_score = -1
   while p_score < 0 or p_score > 100:
    try:
     p_score = float(input("Enter Student Physics Score(0-100): "))

    except ValueError:
     print("Invalid Score, score must be a number")
     p_score = -1
     continue
    if p_score < 0:
     print("Invalid score, score must not be less than zero.")
    elif p_score > 100:
     print("Invalid Score, score must not be greater than 100 ")


   c_score = -1
   while c_score < 0 or c_score > 100:
    try:
     c_score = float(input("Enter Student Chemistry Score(0-100): "))

    except ValueError:
      print("Invalid Score, score must be a number")
      c_score = -1
      continue

    if c_score < 0:
      print("Invalid score, score must not be less than zero.")
    elif c_score > 100:
      print("Invalid Score, score must not be greater than 100 ")


   b_score = -1
   while b_score < 0 or b_score > 100:
    try:
     b_score = float(input("Enter Student Biology Score(0-100): "))

    except ValueError:
      print("Invalid Score, score must be a number")
      b_score = -1
      continue

    if b_score < 0:
      print("Invalid score, score must not be less than zero.")
    elif b_score > 100:
      print("Invalid Score, score must not be greater than 100 ")   
   total = m_score + p_score + e_score+ c_score + b_score
   total_average = total/5
   print(" Average = ", total_average)
   if total_average >= 70:
    grade = "A"
   elif total_average >= 60:
    grade = "B"
   elif total_average >= 50:
    grade = "C"
   elif total_average >= 45:
    grade = "D"
   elif total_average >= 40:
    grade = "E"
   else:
    grade = "F"
   print("Your Average is", total_average,"Therefore you have an/a", grade)  
   if total_average >= 50:
    status = "Pass"
    print("Congratulations You Pass🎉")
   else:
    status = "Fail"
    print("Fail")
   student_rec = {
    "Student_id": student_id,
    "Name": name,
    "Age": age,
    "Gender": gender,
    "Class" : clas,
    "Mathematics_Score": m_score,
    "English_Score": e_score,
    "Physics_Score": p_score,
    "Chemistry_Score": c_score,
    "Biology_Score": b_score,
    "Total_Score": total,
    "Average": total_average,
    "Grade": grade,
    "Status(Pass/Fail)": status
   }
   student.append(student_rec)
  if choice == 2:
   print("**************************")
   if not student:
    print("No Student registered yet...")
   else:
    for student_rec in student:
     print()
     print("Name:" ,student_rec["Name"])
     print("Student Id:" ,student_rec["Student_id"])
     print("Age:" ,student_rec["Age"])
     print("Gender:" ,student_rec["Gender"]) 
     print("Class:" ,student_rec["Class"])
     print("Maths Score:" ,student_rec["Mathematics_Score"])
     print("English Score:" ,student_rec["English_Score"])
     print("Physics Score:" ,student_rec["Physics_Score"])
     print("Chemistry Score:" ,student_rec["Chemistry_Score"])
     print("Biology 9Score:" ,student_rec["Biology_Score"])
     print("Total Score:" ,student_rec["Total_Score"])
     print("Average:" ,student_rec["Average"])
     print("Grade:" ,student_rec["Grade"])
     print("Status:" ,student_rec["Status(Pass/Fail)"])
  if choice == 3:
    print("************ **************")
    print("1. SEARCH BY NAME.")
    print("2. SEARCH BY STUDENT ID.")
    choice_1 = int(input("Enter your choice: "))
    if choice_1 == 1:
      name_1 = input("What is the student's name? ")
      found = False 
      for student_rec in student:
        if name_1 == student_rec["Name"]:
          print(student_rec)
          found = True
      if found == False:
        print("Student not found!!")
    elif choice_1 == 2:
      id_1 = input("Enter the Student's ID ")
      found = False
      for student_rec in student:
        if id_1 == student_rec["Student_id"]:
          print(student_rec)
          found = True
      if found == False:
        print("Student not found!!")
          
        
        
      
        
        
      
    