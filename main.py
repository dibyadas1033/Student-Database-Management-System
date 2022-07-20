#python project
#"STUDENT MANAGEMENT SYSTEM"
#.................login info.............................
#     people     Default username        Default password
#1:-   admin       "admin"                "admin"
#2:-   student   idd(given by admin)      "password"
#3:-  teacher    idd(given by admin)      "password"

# Add student
from prompt_toolkit import prompt
import getpass
def add_Student(idd,name,grade,m1,m2,m3,m4,m5):
    
        with open("student.txt","a") as f:
            f.write(",".join(map(str,(idd,name,grade,m1,m2,m3,m4,m5))))
            f.write("\n")
            
        with open("login.txt","a") as g:
            g.write(str(idd) + "," + "password" + "," + "S" + "," + "D" + "\n")
            
        print(" sucessfully added!!!")

# Add teacher        
def add_Teacher(idd,name,grade,sub):
        
                with open("Teacher.txt","a") as f:
                        f.write(",".join(map(str,(idd,name,grade,sub))))
                        f.write("\n")
                with open("login.txt","a") as g:
                        g.write(str(idd) + "," + "password" + "," + "T"+"," + "D" +"\n")
                print("\n !!! Teacher added successfully   !!!") 

                 
                  
# search student        
def search_Student(idd):
    try:
        flag=False
        f=open("student.txt","r")
        a=[i.strip().split(",") for i in f.readlines()]
        for i in a:
            if i[0]==str(idd):
                flag=True
                print("\nSearch Student Details:")
                print("Id:",i[0])
                print("Name:",i[1])
                print("Grade:",i[2])
                print("Marks 1:",i[3])
                print("Marks 2:",i[4])
                print("Marks 3:",i[5])
                print("Marks 4:",i[6])
                print("Marks 5:",i[7])
                print("\n")
        if(not flag):
            print("Student's information not found\n")

    except:
            print("file does not exist\n")

#seach teacher           
def search_teacher(idd):
        try:
            flag = False
            with open("Teacher.txt","r") as f:
                a=[i.strip().split(",") for i in f.readlines()]
                for i in a:
                    if(i[0] == idd):
                        print("\n Search Teacher Details:")
                        print("Id:",i[0])
                        print("Name:",i[1])
                        print("Grade:",i[2])
                        print("Subject:",i[3])
                        print("\n")
                        flag = True
                        return flag
                if not flag:
                    print("!!! Teacher id not found !!!")
        except:
                print("file doesnot exist")

# Update student marks            
def updateStudentMarks(idd,grade,m1=0,m2=0,m3=0,m4=0,m5=0):
    try:
            f = open("student.txt","r")
            a = [word.strip().split(",") for word in f.readlines()]
            g = open("student.txt","w")
            k = False
            for i in a:
                if i[0]!= str(idd) :
                    g.writelines(",".join(map(str ,i)))
                    g.write("\n")
                    k = True
                    
                elif i[0] == str(idd):
                    g.writelines(",".join(map(str ,(idd,i[1],grade,m1,m2,m3,m4,m5))))
                    g.write("\n")
                    k = True
                     
            if k== True:
                    print("!!! Marks updated sucessfully !!!\n")
                    pass
            else:
                    print("id not present\n")
            f.close()
            g.close()

    except:
            print(" file doesnot exists\n")
            
                
# Delete   
def delete(file_name,idd):
        try:
                f = open(file_name,"r")
                a = [word.strip().split(",") for word in f.readlines()]
                g = open(file_name,"w")
                for i in a:
                        if i[0]!= str(idd):
                                temp = ",".join(map(str,i))+"\n"
                                g.write(temp)     
                        else:
                             pass
                f.close()
                g.close()
        except:
                print("file doesnot exist\n")

# change password
def change_pswd(idd):
        f= open("login.txt","r") 
        a = [word.strip().split(",") for word in f.readlines()]
        g = open("login.txt","a")
        print("\nRULES FOR PASSWORD:")
        print("========================\n")
        print("At least 1 letter between [a-z]")
        print("At least 1 number between [0-9]")
        print("At least 1 letter between [A-Z]")
        print("At least 1 special character from [!@#$%&]")
        print("Minimum length of password: 6")
        print("Maximum length of password: 12")
        for i in a:
                if idd == i[0]:
                        pwd = input("\nEnter the new password: ")
                        if(valid(pwd)):
                            print("password changed succesfully!!!\n")
                            delete("login.txt",idd)
                            g.write(",".join(map(str,(idd,pwd,i[2],"y"))))
                            g.write("\n")
                            g.close()
                            f.close()
                            break
                        else:
                            print("try again!!!")
# validate password                            
def valid(pwd):
    c1=c2=c3=c4=0
    if (len(pwd) >= 6 and len(pwd)<=12): 
        for i in pwd:  
            if (i.islower()): 
                c1+=1             
            if (i.isupper()): 
                c2+=1            
            if (i.isdigit()): 
                c3+=1             
            if(i=='@'or i=='$' or i=='_' or i=='#' or i=='%' or i=='&' or i=='!'): 
                c4+=1           
    if (c1>=1 and c2>=1 and c3>=1 and c4>=1 and c1+c2+c3+c4 == len(pwd)): 
        return True
    else: 
        return False                  
def validate_name(name):
    if name.replace(" ", "").isalpha():
        return True
    return False
   
# admin menu
def admin_menu():
    print("\n++++++ Welcome to  Student Management System ++++++\n")
    while True:
        print("\n=======Operations======")
        print("1:addStuddent\n2:addTeacher\n3:findteacher\n4:findstudent\n5:update marks\n6:delete\n7:Display Students\n8:Display Teachers\n9-exit")
        ch=int(input("enter choice : "))
        if ch == 1:
            idd =input("enter id:")
            name = input("enter name :")
            grade =input("enter grade :")
            m1  = eval(input("enter marks of sub1:"))
            m2  = eval(input("enter marks of sub2:"))
            m3  = eval(input("enter marks of sub3:"))
            m4  = eval(input("enter marks of sub4:"))
            m5  = eval(input("enter marks of sub5:"))
            if idd.isnumeric()==True and validate_name(name)==True and len(grade)==1:
                add_Student(idd,name.upper(),grade.upper(),m1,m2,m3,m4,m5)
            else:
                print("\ninvalid credenntials !!!!!")
             
        elif ch == 2:
            idd =input("enter id: ")
            name = input("enter name: ")
            grade = input("enter grade:")
            sub = input("enter sub:")
            if idd.isnumeric()==True and validate_name(name)==True and len(grade)==1:
                    add_Teacher(idd,name.upper(),grade.upper(),sub.upper())
            else:
                  print("\n!!!!! invalid credentials !!!!!")  
                    
        elif ch == 3:
            idd =input("enter id:")
            if idd.isnumeric()==True:
                    search_teacher(idd)
            else:
                    print("\n!!! invalid credentials !!!")
                    
        elif ch == 4:
            idd =input("enter id:")
            if idd.isnumeric()==True:
                    search_Student(idd)
            else:
                    print("\n!!!!! invalid credentials !!!!!")                   
            
        elif ch==5:
            idd =input("enter id:")
            grade = input("enter grade:")
            m1  = eval(input("enter marks of sub1:"))
            m2  = eval(input("enter marks of sub2:"))
            m3  = eval(input("enter marks of sub3:"))
            m4  = eval(input("enter marks of sub4:"))
            m5  = eval(input("enter marks of sub5:"))
            if idd.isnumeric()==True and len(grade)==1:
                    updateStudentMarks(idd,grade.upper(),m1,m2,m3,m4,m5)
            else:
                print("\n!!!!! invalid credentials !!!!!")            

        elif ch==6:
            p = int(input("1- delete student\n 2-delete teacher\n enter ur choice:"))
            if p == 1:
                idd =input("enter id:")
                if idd.isnumeric()==True:
                        delete("student.txt",idd)
                        delete("login.txt",idd)
                        print("student details deleted succesfully!!!\n")
                else:
                        print("\n!!!!! invalid credentials !!!!!")            

            elif p==2:
                idd =input("enter id:")
                if idd.isnumeric()==True:
                        delete("teacher.txt",idd)
                        delete("login.txt",idd)
                        print("teacher details deleted succesfully!!!\n")
                else:
                        print("\n!!!!! invalid credentials !!!!!")

            else:
                    print("!!!!! invalid option\n !!!!!")
        elif ch==7:
                Show_Students()
        elif ch==8:
                Show_Teachers()
        elif ch==9:
                break
        else:
            print("\n Invalid option")

# Teacher menu 
def Show_Teachers():
        try:
            print("ID\t| Name\t\t\t\t| grade\t| Subject")
            print("--------------------------------------------------")
            with open("Teacher.txt","r") as f:
                a=[i.strip().split(",") for i in f.readlines()]
                for i in a:
                    
                        print(i[0]+"\t"+"|"+ i[1]+"\t\t\t"+"| "+ i[2]+"\t"+"| "+i[3])
    

        except:
                print("file doesnot exist")

def Show_Students():
        try:
            print("ID\t\t| Name\t\t")
            print("--------------------------------------------------")
            with open("student.txt","r") as f:
                a=[i.strip().split(",") for i in f.readlines()]
                for i in a: 
                        print(i[0]+"\t"+"|"+ i[1])
    

        except:
                print("file doesnot exist")     

def Show_StudentsBYGrade(grade):
        try:
            print("ID\t | Name\t\t\t|Grade\t\t")
            print("--------------------------------------------------")
            with open("student.txt","r") as f:
                a=[i.strip().split(",") for i in f.readlines()]
                for i in a:
                        if(i[2]==grade): 
                            print(i[0]+""+"|"+ i[1]+"\t"+"|"+i[2])
    

        except:
                print("file doesnot exist")     

   
def teacher_menu():
        print("\n++++++ Welcome to  Student Management System ++++++\n")
        while True:
                print("\n=======Operations======")
                print("1: findteacher\n2: findstudent\n3: update marks\n4: Change password\n5:Display Students\n6:Display Students by grade\n7: Exit")
                ch=int(input("enter choice : "))
                if  ch==1:    
                    idd =input("enter id: ")
                    search_teacher(idd)
        
                elif ch==2:
                    idd =input("enter id: ")
                    search_Student(idd)
        
                elif ch==3:
                    idd =input("enter id:")
                    grade = input("enter grade: ")
                    m1  = eval(input("enter marks of sub1:"))
                    m2  = eval(input("enter marks of sub2:"))
                    m3  = eval(input("enter marks of sub3:"))
                    m4  = eval(input("enter marks of sub4:"))
                    m5  = eval(input("enter marks of sub5:"))
                    updateStudentMarks(idd,grade.upper(),m1,m2,m3,m4,m5)

                elif ch==4:
                        idd =input("enter id")
                        change_pswd(idd)
                        
                elif ch==5:
                     Show_Students()
                
                elif ch==6:
                     s = input("Enter the Grade :")
                     Show_StudentsBYGrade(s)
                elif ch==7:
                        break

                else:
                     print("invalid option\n")
# Student menu
def Student_menu(user):
         while True:
                print("1:get details\n2:-change password\n3:-exit ")
                ch=int(input("enter choice : "))
                if  ch==1:    
                    #idd =input("enter id: ")
                    search_Student(user)
        
                elif ch==2:
                        idd =input("enter id: ")
                        change_pswd(idd)

                elif ch==3:
                     break

                else:
                     print("invalid option\n")
                        
                
# To login into student DBMs                                                                                  
def login():                
        user = input("enter the username:")
        pwd =  prompt("Password: ", is_password=True)
        if user=="admin" and pwd =="admin":
                print("\n=======welcome admin=======")

                admin_menu()
        else:
                with open("login.txt","r") as f:
                     lst = [word.strip().split(",") for word in f.readlines()]
                k = False
                for i in lst:
                        if i[0] == user and i[1] == pwd:
                                k =True
                                if i[3]=="D":
                                    change_pswd(user)
                                    if i[2]=="S":
                                        print("\n------------Welcome Student---------")
                                        Student_menu(user)
                                    else:
                                        print("\n-------------Welcome Teacher---------")
                                        teacher_menu()
                                                
                                else:
                                        if i[2]=="S":
                                                print("\n------------Welcome Student---------")
                                                Student_menu(user)
                                        else:
                                                print("\n-------------Welcome Teacher---------")
                                                teacher_menu()   
                if k == True:
                      pass
        
                else:
                      print("invalid credentials\n")
                      
while True:
        print("\n=============Welcome User=============")
        print("\n1: login\n2:-exit\n" )
        ch = int(input("enter choice : "))                        
        if  ch == 1:
                login()        
        elif ch == 2:
                print("thank u!!")
                break
        else:
                print("invalid option\n")
