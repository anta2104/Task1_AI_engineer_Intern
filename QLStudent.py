import argparse
from Student import *

def main():
    parser = argparse.ArgumentParser(description="Student management CLI")
    subparsers = parser.add_subparsers(dest="command", help="sub-command help")

    add_parser = subparsers.add_parser("add", help="add a new student")
    add_parser.add_argument("id", help="the ID of the new student")
    add_parser.add_argument("name", help="the name of the new student")
    add_parser.add_argument("bod", help="the bod of the new student")
    add_parser.add_argument("phone", help="the phone number of the new student")
    add_parser.add_argument("Class", help="the class of the new student")



    edit_parser = subparsers.add_parser("edit", help="edit the name of a student")
    edit_parser.add_argument("id", help="the ID of the student to edit")
    edit_parser.add_argument("new_name", help="the new name of the student")
    edit_parser.add_argument("new_bod", help="the  new bod of the student")
    edit_parser.add_argument("new_phone", help="the new phone number of the student")
    edit_parser.add_argument("new_class", help="the new class of the student")



    remove_parser = subparsers.add_parser("remove", help="remove a student")
    remove_parser.add_argument("id", help="the ID of the student to remove")

    list_parser = subparsers.add_parser("list", help="list all student")

    listInclass_parser = subparsers.add_parser("listIn", help="list all student in a class")
    listInclass_parser.add_argument("Class",help="The class of the student")
    # list_parser.add_argument("filename", help="the name of the input file")

    args = parser.parse_args()
    x = Student("01", "XX","ll","ll","ll")
    x.read_data()
    if args.command == "add":
        new = Student(args.id , args.name, args.bod, args.phone, args.Class)
        x.add_student(new)
        x.save()
    elif args.command == "edit":
        # x = Class(args.id, args.new_name)
        x.edit_student(args.id, args.new_name, args.new_bod, args.new_phone, args.new_class)
        x.save()
    elif args.command == "remove":
        x.remove_student(args.id)
        x.save()
    elif args.command == "list":
        x.list_student()
    elif args.command == "listIn":
        x.listStudent_inClass(args.Class)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()