s1=int(input("enter number of students"))
sqn=["SID","Name","Gender","Course Name","CGPA"]
for i in range (s1):
     sqnc=[]
     SID=int(input("enter SID"))
     Name=input("enter Name")
     Gender=input("enter Gender:")
     Course_Name=input("enter the Course:")
     CGPA=float(input("enter CGPA:"))
     sqnc.append(SID)
     sqnc.append(Name)
     sqnc.append(Gender)
     sqnc.append(Course_Name)
     sqnc.append(CGPA)
     print(sqn)
     print(sqnc)
