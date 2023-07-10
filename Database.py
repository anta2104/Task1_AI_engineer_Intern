from Class import *
from Student import *
from Teacher import *
import pickle
import time
import csv
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
        # with open(self.table_name + ".txt", newline='') as f: 
        #     reader = csv.reader(f, delimiter='|')
        #     rows = list(reader)
        # for i in rows[0] :
        #     for j in list :
        #         if not j in i : return "Không có thông tin trên"
        return self

    # Thêm dữ liệu
    def insert(self, table_name, data):
        self.table_name = table_name + ".txt"
        self.data = data 
        
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)
            
            # kiểm tra độ dài của data có bằng độ dài của row không
            if len(rows[0]) != len(self.data):
                print("Error with data length")
            else: 
                # nếu thỏa mãn thì chèn data vào dòng cuối
                with open(self.table_name, 'a', newline='') as f: 
                    writer = csv.writer(f, delimiter='|')
                    writer.writerow(self.data)     

    # Cập nhật dữ liệu 
    def update(self, table_name, data):
        self.table_name = table_name + ".txt"
        self.data = data
        
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader) 
        
        # lấy index của column thỏa mãn phương thức where     
        index_column = rows[0].index(self.columns_name)
        for index, row in enumerate(rows[1:], start=1):
            if str(row[index_column]) == str(self.value): 
                # thay row thỏa mãn phương thức where bằng data
                rows[index] = self.data              

        # cập nhập lại file
        with open(self.table_name, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows) 

    # Xóa dữ liệu 
    def delete(self, table_name):
        self.table_name = table_name + ".txt"
        
        with open(self.table_name, newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)

        # lấy index của column thỏa mãn điều kiện where
        index_column = rows[0].index(self.columns_name)
        for row in rows[1:]:
            if str(row[index_column]) == str(self.value): 
                rows.remove(row)
                
        with open(self.table_name, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerows(rows)  
        return self        
    
    # Tạo index trên column_name đã chọn
    def create_index(self, table_name, column_name):
        self.table_name = table_name
        self.columns_name = column_name
        
        with open(self.table_name + ".txt", newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)
        # Tạo file để lưu index
        index_file = f"{self.table_name}_{self.columns_name}_index.pkl"
        try:
            with open(index_file, 'rb') as f:
                self.index = pickle.load(f)
        except FileNotFoundError:
                # Dùng 1 self.index để lưu STT 
                # Ví dụ : self.index = [[0,'tan'],[1,'huy'],[2,'hung']]
                column_index = rows[0].index(column_name)
                for i in range(1, len(rows)):
                    self.index.append([i-1, rows[i][column_index]])
                # Sắp xếp lại theo column_name đã chọn 
                # Ví dụ self.index sau khi sắp xếp : self.index = [[1,'huy'],[2,'hung'],[0,'tan']]
                self.index.sort(key=lambda x: x[1])
            # Lưu lại self.index vào file
        with open(index_file, 'wb') as f:
            pickle.dump(self.index, f)


    # Sử dụng index trên cột đã chọn để truy vấn    
    def get_use_index(self): 
        with open(self.table_name + ".txt", newline='') as f: 
            reader = csv.reader(f, delimiter='|')
            rows = list(reader)
        # Load file index đã create từ trước
        index_file = f"{self.table_name}_{self.columns_name}_index.pkl"
        try:
            with open(index_file, 'rb') as f:
                self.index = pickle.load(f)
                index = self.binary_search(self.index, self.value)
                if index != -1 : 
                    i = self.index[index][0] + 1
                    output = [rows[i][j] for j in range(len(rows[i])) if rows[0][j] in self.list]
                else: exit("Sai giá trị truyền vào hàm Where")
            return output
        except FileNotFoundError:
            results = []
            index_column = rows[0].index(self.columns_name)
            for row in rows[1:]:
                if str(row[index_column]) == str(self.value): 
                    results.append(row)
            columns_selected = []
            for field in self.list:
                columns_selected.append(rows[0].index(field))
                
            results_last = []
            for result in results:
                new_list = [result[i] for i in range(len(result)) if i in columns_selected]
                results_last.append(new_list)
            
            return results_last
            
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

# x = dbQuery()
# # x.create_index("Teacher","Name")

# # start_time = time.time()

# test = x.select(['Phone', 'Name','ID']).Where('Name', 'XCINNZOQYY').From('Teacher').get_use_index()
# print(test)
# test = x.select(['Phone', 'Name']).Where('Name', 'NGNMJNIR').From('Student').get()

# end_time = time.time()
# time_in_sec = end_time - start_time
# print("Time taken:", round(time_in_sec, 4), "seconds")




# test = x.select(['Phone', 'Name']).Where('Class', 'K77CB\n').From('Student').get()
# x.insert(table_name='Teacher', data=["06", "ta", "01/01", "43536765", "K65CB"])
# x.Where('ID', '06').update(table_name='Teacher', data=["06", "tuu", "01/01", "43536765", "K65CB"])
# x.Where("ID","06").delete(table_name ="Teacher")

