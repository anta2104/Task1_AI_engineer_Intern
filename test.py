from Database import *

x = dbQuery()

########### Test method select #############
# Các trường hợp select đúng các trường
print(x.select(['ID']).Where('ID', "01").From('Student').get_use_index())
print(x.select(['ID', 'BOD']).Where('ID', "01").From('Student').get_use_index())
print(x.select(['ID', 'BOD', 'Name']).Where('ID', "01").From('Student').get_use_index())
print(x.select(['ID', 'BOD', 'Name', 'Phone']).Where('ID', "01").From('Student').get_use_index())
print(x.select(['ID', 'BOD', 'Name', 'Phone', 'Class']).Where('ID', "01").From('Student').get_use_index())


# Trường hợp trường trong select không đúng 
# print(x.select(['Age']).Where('ID', 1).From('Student').get_use_index())
print('\n')

########### Test method where #############
#Các trường hợp where đúng các trường
print(x.select(['ID', 'Name']).Where('ID', '01').From("Student").get_use_index())
print(x.select(['ID', 'Name']).Where('Name', 'RHIKMJ').From("Student").get_use_index())
print(x.select(['ID', 'Name']).Where('Phone', '6901951').From("Student").get_use_index())
print(x.select(['ID', 'Name']).Where('Class', 'K66CB').From("Student").get_use_index())
# Trường hợp sai thông tin của Where
print(x.select(['ID', 'Name']).Where('Phone', '00000000').From("Student").get_use_index())
print('\n')

########### Test method From #############
#Các trường hợp From đúng các trường
print(x.select(['ID', 'Name']).Where('Class', 'K66CB').From("Student").get_use_index())
print('\n')

########### Test method insert #############
#Các trường hợp insert đúng đủ 
x.insert(table_name='Student', data=["15", "tan", "09/09", "1277646"])
print(x.select(['ID', 'Name']).Where('ID', '15').From("Student").get_use_index())
print('\n')

########### Test method update #############
x.Where('ID', '01').update('Student', data=["00", "tan", "01/01", "54635324", "K65CC"])
x.Where('Name','tan').update('Student', data=["01", "tu", "02/02", "3454345", "K65CC"])
x.Where('BOD','02/02').update('Student', data=["01", "tu", "03/02", "54334534", "K65CC"])
print('\n')

########### Test method delete #############
x.Where('ID', '01').delete('Student')
x.where('Name', 'ABVEZP').delete('Student')
x.where('BOD', '09/02').delete('Student')
x.where('Phone', '6625489').delete('Student')
print('\n')















