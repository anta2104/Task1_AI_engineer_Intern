class Class:

    listClass = []

    # Đọc dữ liệu từ file txt 
    def read_data_Class(self) : 
        f = open("Class.txt")
        data = list(f)
        print(len(data))
        for i in range (1,len(data)) :
            temp = data[i]
            temp = temp.split("|")
            if len(temp) < 2: continue
            x = Class(temp[0],temp[1])
            self.listClass.append(x)


    # Định nghĩa các thuộc tính của lớp
    def __init__(self, ID, Name) :
        self.ID = ID 
        self.Name = Name

    def setID(self,ID) : 
        self.ID = ID

    def getID(self) :
        return self.ID
    
    def setName(self, Name) :
        self.Name = Name
    
    def getName(self) :
        return self.Name
    
    def getListClass(self) :
        return self.listClass()
    
    # Thêm class
    def add_classroom(self, new_classroom):
        for classroom in self.listClass:
            if classroom.ID == new_classroom.ID:
                exit("Error")
        self.listClass.append(new_classroom)
    
    # Sửa class
    def edit_classroom(self, ID, new_name):
        tam = 1
        for classroom in self.listClass:
            if classroom.ID == ID:
                classroom.Name = new_name
                tam = 0
        if(tam != 0) : exit("ERROR")

    # Xóa class
    def remove_classroom(self, id):
        tam = 1 
        for classroom in self.listClass:
            if classroom.ID == id:
                self.listClass.remove(classroom)
                print(classroom.ID)
                tam = 0
        if(tam != 0) : exit("ERROR")
    
    #Lưu dữ liệu
    def saveC(self) :
        
        self.listClass = sorted(self.listClass, key=lambda x: x.ID)
        with open("Class.txt", "w") as f:
            content = ""
            for classroom in self.listClass:
                content += f"{classroom.ID}|{classroom.Name}"
            f.write(content)
                
        with open("Class.txt", "r+") as f:
            content = f.read()
            f.seek(0)
            f.write("ID|Name\n" + content + "\n")
        f.close()
    
    def list_classrooms(self):
        print("ID | Name")
        for classroom in self.listClass:
            print(f"{classroom.ID} | {classroom.Name}")



