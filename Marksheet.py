print("Enter subject marks out of 100.")

english = float(input("English: "))
urdu = float(input("Urdu: "))
math = float(input("Mathematics: "))
physics = float(input("Physics: "))
chemistry = float(input("Chemistry: "))

totalMarks = english + urdu + math + physics + chemistry
percentage = (totalMarks / 500) * 100
grade = ""

if percentage >= 80:
    grade = "A+"
elif percentage >= 71 and percentage <= 79:
    grade = "A "
elif percentage >= 61 and percentage <= 69:
    grade = "B "
elif percentage >= 51 and percentage <= 59:
    grade = "C "

print (percentage)
print (grade)

print ("-------------------------------------------------------------------------")
print ("|                               MARK SHEET                              |")
print ("-------------------------------------------------------------------------")
print ("|       Subject      |      Total Marks      |      Obtained Marks      |")
print ("-------------------------------------------------------------------------")
print ("|       English      |          100          |            " + str(english) + "          |")
print ("|       Urdu         |          100          |            " + str(urdu) + "          |")
print ("|       Math         |          100          |            " + str(math) + "          |")
print ("|       Physics      |          100          |            " + str(physics) + "          |")
print ("|       Chemistry    |          100          |            " + str(chemistry) + "          |")
print ("-------------------------------------------------------------------------")
print ("| Total Marks: " + str(totalMarks) + "                                Grade: " + grade + "           |")
print ("-------------------------------------------------------------------------")