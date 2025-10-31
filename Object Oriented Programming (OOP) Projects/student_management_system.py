#StudentMangementSystem  #Using OOP concepts

class Student:

    def __init__(self,name,age,student_id,grade):
            self.name=name
            self.age=age
            self.student_id=student_id
            self.grade=grade

    def display_info(self):
          print(f"Name:  {self.name}")
          print(f"Age:  {self.age}")
          print(f"ID:  {self.student_id}")
          print(f"Grade:  {self.grade}")

    def update_grade(self,new_grade):
          self.grade= new_grade
          print(f"Grade Updated For {self.name} to {self.grade}")

class StudentManagementSystem:
      
    def __init__(self):
          self.students=[]

    def add_student(self,name,age,student_id,grade):
        student=Student(name,age,student_id,grade)
        self.students.append(student)
        print(f"Student {name} added succesfully")

    def view_student(self):
         if not self.students:
              print("No Student Found")
         else:
            print("\n===Student List===")
            for student in self.students:
                 student.display_info()

    def search_student(self,student_id):
        for student in self.students:
             if student.student_id==student_id:
                  print("Student Found")
                  student.display_info()
                  return
        print("Student Not Found")

    def update_student_grade(self,student_id,new_grade):
        for student in self.students:
             if student.student_id== student_id:
                  student.update_grade(new_grade)
                  return
        print("Student Not Found")

    def remove_student(self,student_id):
         for student in self.students:
              if student.student_id==student_id:
                self.students.remove(student)
                print(f"Student {student.name} removed successfully")
                return
         print("Student Not Found")

# --- Main program ---

def main():
     system=StudentManagementSystem()

     while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Grade")
        print("5. Remove Student")
        print("6. Exit")

        choice =input("Enter Your Choice: ")

        if choice =="1":
             name=input("Enter Your Name: ")
             age=int(input("Enter Your Age: "))
             student_id=input("Enter Your ID: ")
             grade=input("Enter Your Grade: ")
             system.add_student(name,age,student_id,grade)

        elif choice== "2":
             system.view_student()

        elif choice =="3":
             student_id=input("Enter the student ID to search: ")
             system.search_student(student_id)

        elif choice == '4':
            student_id = input("Enter student ID to update: ")
            new_grade = input("Enter new grade: ")
            system.update_student_grade(student_id, new_grade)

        elif choice == '5':
            student_id = input("Enter student ID to remove: ")
            system.remove_student(student_id)

        elif choice == '6':
            print(" Exiting...!")
            break

        else:
            print("Invalid choice. Please enter a number from 1-6.")


if __name__ == "__main__":
    main()
             
        

          


                               

    
                 

          
    

