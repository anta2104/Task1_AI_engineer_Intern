class Student:
    
    listStudent = []
    # Đọc dữ liệu từ file txt
    def read_data_student(self) : 
        f = open("Student.txt")
        data = list(f)
        # print(len(data))
        for i in range (1,len(data)) :
            temp = data[i]
            temp = temp.split("|")
            if len(temp) < 4: continue
            x = Student(temp[0],temp[1],temp[2],temp[3],temp[4])
            self.listStudent.append(x)

    # Thêm học sinh
    def add_student(self, new_student):
        for student in self.listStudent:
            if student.ID == new_student.ID:
                exit("Error")
        self.listStudent.append(new_student)

    # Sửa tt học sinh
    def edit_student(self, ID, new_name, bod , phone, Class):
        tam = 1
        for student in self.listStudent:
            if student.ID == ID:
                student.Name = new_name
                student.Birthday = bod 
                student.Phone = phone
                student.Class = Class
                tam = 0
        if(tam != 0) : exit("ERROR")
    
    # Xóa học sinh
    def remove_student(self, id):
        tam = 1 
        for student in self.listStudent:
            if student.ID == id:
                self.listStudent.remove(student)
                tam = 0
        if(tam != 0) : exit("ERROR")

    #Lưu dữ liệu
    def saveS(self) :
        
        self.listStudent = sorted(self.listStudent, key=lambda x: x.ID)
        with open("Student.txt", "w") as f:
            content = ""
            for student in self.listStudent:
                content += f"{student.ID}|{student.Name}|{student.Birthday}|{student.Phone}|{student.Class}"
            f.write(content)
                
        with open("Student.txt", "r+") as f:
            content = f.read()
            f.seek(0)
            f.write("ID|Name|BOD|PHONE|Class\n" + content + "\n")
        f.close()

    # Đưa ra danh sách học sinh
    def list_student(self):
        print("ID | Name | BOD | Phone | Class")
        for student in self.listStudent:
            print(f"{student.ID}|{student.Name}|{student.Birthday}|{student.Phone}|{student.Class}")
    
    def listStudent_inClass(self, class_name) :
        print("ID | Name | BOD | Phone | Class")
        for student in self.listStudent:
            # print(str(student.Class) + " " + str(class_name))
            if str(student.Class) == str(class_name) + "\n" : 
                print(f"{student.ID}|{student.Name}|{student.Birthday}|{student.Phone}|{student.Class}")


    def __init__(self, ID, Name, Birthday, Phone, Class) :
        self.ID = ID 
        self.Name = Name
        self.Birthday = Birthday
        self.Phone = Phone
        self.Class = Class 

    def setID(self,ID) : 
        self.ID = ID

    def getID(self) :
        return self.ID
    
    def setName(self, Name) :
        self.Name = Name
    
    def getName(self) :
        return self.Name
    
    def setBirthday(self, Birthday) :
        self.Birthday = Birthday
    
    def getBirthday(self) :
        return self.Birthday
    
    def setPhone(self, Phone) :
        self.Birthday = Phone
    
    def getPhone(self) :
        return self.Phone
    
    def setClass(self, Class) :
        self.Class = Class

    def getClass(self) :
        return self.Class    
    


