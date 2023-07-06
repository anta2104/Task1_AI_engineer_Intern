class Teacher:
    
    listTeacher = []

    # Đọc dữ liệu từ file txt
    def read_data_teacher(self) : 
        f = open("Teacher.txt")
        data = list(f)
        # print(len(data))
        for i in range (1,len(data)) :
            temp = data[i]
            temp = temp.split("|")
            if len(temp) < 4: continue
            x = Teacher(temp[0],temp[1],temp[2],temp[3],temp[4])
            # print(self.list_teacher)
            self.listTeacher.append(x)

    # Thêm giáo viên
    def add_teacher(self, new_teacher):
        for teacher in self.listTeacher:
            if teacher.ID == new_teacher.ID:
                exit("Error")
        self.listTeacher.append(new_teacher)

    # Sửa tt giáo viên 
    def edit_teacher(self, ID, new_name, bod , phone, headclass):
        tam = 1
        for teacher in self.listTeacher:
            if teacher.ID == ID:
                teacher.Name = new_name
                teacher.Birthday = bod 
                teacher.Phone = phone
                teacher.HeadClass = headclass
                tam = 0
        if(tam != 0) : exit("ERROR")

    # Xóa giáo viên
    def remove_teacher(self, id):
        tam = 1 
        for teacher in self.listTeacher:
            if teacher.ID == id:
                print("XXXXX")
                self.listTeacher.remove(teacher)
                tam = 0
        if(tam != 0) : exit("ERROR")
    
    #Lưu dữ liệu
    def saveT(self) :
        
        self.listTeacher = sorted(self.listTeacher, key=lambda x: x.ID)
        with open("Teacher.txt", "w") as f:
            content = ""
            for teacher in self.listTeacher:
                content += f"{teacher.ID}|{teacher.Name}|{teacher.Birthday}|{teacher.Phone}|{teacher.HeadClass}"
            f.write(content)
                
        with open("Teacher.txt", "r+") as f:
            content = f.read()
            f.seek(0)
            f.write("ID|Name|BOD|Phone|HeadClass\n" + content + "\n")
        f.close()
    
    def list_teacher(self):
        print("ID | Name | BOD | Phone | HeadClass")
        for teacher in self.listTeacher:
            print(f"{teacher.ID}|{teacher.Name}|{teacher.Birthday}|{teacher.Phone}|{teacher.HeadClass}")


    def __init__(self, ID, Name, Birthday, Phone, HeadClass) :
        self.ID = ID 
        self.Name = Name
        self.Birthday = Birthday
        self.Phone = Phone
        self.HeadClass = HeadClass

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
    
    def setHeadClass(self, HeadClass) :
        self.HeadClass = HeadClass
    
    def getHeadClass(self) :
        return self.HeadClass
    
    


