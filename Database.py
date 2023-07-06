from Class import *
from Student import *
from Teacher import *

class dbQuery:

    # Định nghĩa các tham số có thể của truy vấn
    def __init__(self):
        self.table_name = None
        self.list = None 
        self.columns_name = None
        self.value = None
        self.data = None 
    
    # Trỏ đến bảng
    def From(self, table_name):
        self.table_name = table_name
        return self
    
    # Lấy giá trị của 1 đối tượng 
    def Where(self, column_name, value):
        self.columns_name = column_name
        self.value = value
        return self
    
    # Lấy các thông tin cần trích xuất
    def select(self, list):
        self.list = list
        return self
    
    # Đọc dữ liệu từ file
    def read_data(self):
        f = open(self.table_name + ".txt")
        if (str(self.table_name) == "Class") : 
            x = Class("","")
            x.read_data_Class()
        elif (str(self.table_name) == "Student") :
            x = Student("","","","","")
            x.read_data_student()
        else : 
            x = Teacher("","","","","")
            x.read_data_teacher()
        return x


    # Lấy dữ liệu ra 
    def get(self):
        if (str(self.table_name) == "Student") :
            # print(self.columns_name)
            for i in self.read_data().listStudent :
                # print(getattr(i, self.columns_name))
                if getattr(i, self.columns_name) == self.value:
                    for column_name in self.list:
                        print(getattr(i, column_name))

        if (str(self.table_name) == "Teacher") :
            for i in self.read_data().listTeacher :
                if getattr(i, self.columns_name) == self.value:
                    for column_name in self.list:
                        print(getattr(i, column_name))
        
        if (str(self.table_name) == "Class") :
            for i in self.read_data().listClass :
                if getattr(i, self.columns_name) == self.value:
                    for column_name in self.list:
                        print(getattr(i, column_name))

    # Thêm dữ liệu
    def insert(self, table_name, data):
        self.table_name = table_name
        self.data = data 
        if self.table_name == "Class" :
            new = Class(data[0],data[1])
            temp = self.read_data()
            temp.add_classroom(new)    
            temp.saveC()
        if self.table_name == "Student" :
            new = Student(data[0],data[1],data[2],data[3],data[4])
            temp = self.read_data()
            temp.add_student(new)    
            temp.saveS()
        if self.table_name == "Teacher" :
            new = Teacher(data[0],data[1],data[2],data[3],data[4])
            temp = self.read_data()
            temp.add_teacher(new)
            temp.saveT()

    # Cập nhật dữ liệu 
    def update(self, table_name, data) :
        self.table_name = table_name
        self.data = data
        if self.table_name == "Class" :
            temp = self.read_data()   
            for i in temp.listClass :
                if getattr(i, self.columns_name) == self.value: temp.edit_classroom(data[0],data[1])
            temp.saveC()
        if self.table_name == "Student" :
            temp = self.read_data()
            for i in temp.listStudent :
                if getattr(i, self.columns_name) == self.value: temp.edit_student(data[0],data[1],data[2],data[3],data[4])
            temp.saveS()
        if self.table_name == "Teacher" :
            temp = self.read_data()
            for i in temp.listTeacher :
                if getattr(i, self.columns_name) == self.value: temp.edit_teacher(data[0],data[1],data[2],data[3],data[4])
            temp.saveT()

    # Xóa dữ liệu 
    
    def delete(self, table_name) :
        self.table_name = table_name
        if self.table_name == "Class" :
            temp = self.read_data()   
            for i in temp.listClass :
                if getattr(i, self.columns_name) == self.value: temp.remove_classroom(self.value)
            temp.saveC()
        if self.table_name == "Student" :
            temp = self.read_data()
            for i in temp.listStudent :
                if getattr(i, self.columns_name) == self.value: temp.remove_student(self.value)
            temp.saveS()
        if self.table_name == "Teacher" :
            temp = self.read_data()
            for i in temp.listTeacher :
                if getattr(i, self.columns_name) == self.value: temp.remove_teacher(self.value)
            temp.saveT()
  


x = dbQuery()
# test = x.select(['Phone', 'Name']).Where('Class', 'K77CB\n').From('Student').get()
# test = x.select(['Phone', 'Name']).Where('HeadClass', 'K77CB\n').From('Teacher').get()
# x.insert(table_name='Teacher', data=["06", "ta", "01/01", "43536765", "K65CB"])
# x.Where('ID', '06').update(table_name='Teacher', data=["06", "tuu", "01/01", "43536765", "K65CB"])
# x.Where("ID","06").delete(table_name ="Teacher")

