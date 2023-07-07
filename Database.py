from Class import *
from Student import *
from Teacher import *
import pickle
import time
class dbQuery:

    # Định nghĩa các tham số có thể của truy vấn
    def __init__(self):
        self.table_name = None
        self.list = None 
        self.columns_name = None
        self.value = None
        self.data = None 
        self.index = []
    
    
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
    
    # Tạo index trên column_name đã chọn
    def create_index(self, table_name, column_name):
        self.table_name = table_name
        self.columns_name = column_name
        
        # Tạo file để lưu index
        index_file = f"{self.table_name}_{self.columns_name}_index.pkl"
        try:
            with open(index_file, 'rb') as f:
                self.index = pickle.load(f)
        except FileNotFoundError:
            if (str(self.table_name) == "Student"):
                temp = self.read_data()

                # Dùng 1 self.index để lưu STT 
                # Ví dụ : self.index = [[0,'tan'],[1,'huy'],[2,'hung']]
                for i in range (0,len(temp.listStudent)) :
                    self.index.append([i,getattr(temp.listStudent[i],self.columns_name)])

                # Sắp xếp lại theo column_name đã chọn 
                # Ví dụ self.index sau khi sắp xếp : self.index = [[1,'huy'],[2,'hung'],[0,'tan']]
                self.index.sort(key=lambda x: x[1])
            elif (str(self.table_name) == "Teacher"):
                temp = self.read_data()
                for i in range (0,len(temp.listTeacher)) :
                    self.index.append([i,getattr(temp.listStudent[i],self.columns_name)])
                self.index.sort(key=lambda x: x[1])
            elif (str(self.table_name) == "Class"):
                temp = self.read_data()
                for i in range (0,len(temp.listClass)) :
                    self.index.append([i,getattr(temp.listStudent[i],self.columns_name)])
                self.index.sort(key=lambda x: x[1])

            # Lưu lại self.index vào file
            with open(index_file, 'wb') as f:
                pickle.dump(self.index, f)


    # Sử dụng index trên cột đã chọn để truy vấn    
    def get_use_index(self): 
        # Load file index đã create từ trước
        index_file = f"{self.table_name}_{self.columns_name}_index.pkl"
        with open(index_file, 'rb') as f:
            self.index = pickle.load(f)

        
        if (str(self.table_name) == "Student") :
            temp = self.read_data()

            # dùng tím kiếm nhị phân để tìm vị trí của self.valua trong self.index 
            index = self.binary_search(self.index, self.value)
        
        if index != -1 : 
            i = temp.listStudent[self.index[index][0]]
            for column_name in self.list:
                print(getattr(i, column_name))  
    
    # Lấy dữ liệu ra không dùng index
    def get(self):
        if (str(self.table_name) == "Student") :
            temp = self.read_data()
            # print(self.columns_name)
            for i in temp.listStudent :
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


        
    def binary_search(self,arr, target):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][1] == target:
                return mid
            elif arr[mid][1] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

x = dbQuery()
# x.create_index("Student","Name")

# start_time = time.time()

test = x.select(['Phone', 'Name','ID']).Where('Name', 'NGNMJNIR').From('Student').get_use_index()
# test = x.select(['Phone', 'Name']).Where('Name', 'NGNMJNIR').From('Student').get()

# end_time = time.time()
# time_in_sec = end_time - start_time
# print("Time taken:", round(time_in_sec, 4), "seconds")




# test = x.select(['Phone', 'Name']).Where('Class', 'K77CB\n').From('Student').get()
# x.insert(table_name='Teacher', data=["06", "ta", "01/01", "43536765", "K65CB"])
# x.Where('ID', '06').update(table_name='Teacher', data=["06", "tuu", "01/01", "43536765", "K65CB"])
# x.Where("ID","06").delete(table_name ="Teacher")

