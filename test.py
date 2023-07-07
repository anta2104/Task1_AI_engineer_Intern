rows = [
    ["name", "age", "gender"],
    ["Alice", 25, "female"],
    ["Bob", 30, "male"],
    ["Charlie", 35, "male"]
]

list = ['age', 'gender']
x =[1,2]
i = 2
res = [rows[i]]

new_list = []
column_name = "name"  # Tên cột cần lấy
column_index = rows[0].index(column_name)  # Lấy chỉ số của cột cần lấy

output = [rows[i][j] for j in range(len(rows[i])) if rows[0][j] in list]

print(output)
# Kết quả sẽ là: [[0, 'Alice'], [1, 'Bob'], [2, 'Charlie']]