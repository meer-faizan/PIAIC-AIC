print("Enter subject marks out of 100.")

english = float(input("English: "))
urdu = float(input("Urdu: "))
math = float(input("Mathematics: "))
physics = float(input("Physics: "))
chemistry = float(input("Chemistry: "))

totalMarks = english + urdu + math + physics + chemistry
percentage = (totalMarks / 500) * 100

print ("-------------------------------------------------------------------------")
print ("|                               MARK SHEET                              |")
print ("-------------------------------------------------------------------------")
print ("|      Subject       |       Max Marks       |      Obtained Marks      |")
print ("-------------------------------------------------------------------------")
print ("|      English       |          100          |            " + str(english) + "          |")
print ("|      Urdu          |          100          |            " + str(urdu) + "          |")
print ("|      Mathematics   |          100          |            " + str(math) + "          |")
print ("|      Physics       |          100          |            " + str(physics) + "          |")
print ("|      Chemistry     |          100          |            " + str(chemistry) + "          |")
print ("-------------------------------------------------------------------------")
print ("| Total Obtained Marks: " + str(totalMarks) + "                                           |")
print ("-------------------------------------------------------------------------")
print ("| Obtained Percentage: " + str(percentage) + "%                                            |")
print ("-------------------------------------------------------------------------")