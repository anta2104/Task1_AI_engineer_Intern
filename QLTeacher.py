import argparse
from Teacher import *

def main():
    parser = argparse.ArgumentParser(description="Teacher management CLI")
    subparsers = parser.add_subparsers(dest="command", help="sub-command help")

    add_parser = subparsers.add_parser("add", help="add a new teacher")
    add_parser.add_argument("id", help="the ID of the new teacher")
    add_parser.add_argument("name", help="the name of the new teacher")
    add_parser.add_argument("bod", help="the bod of the new teacher")
    add_parser.add_argument("phone", help="the phone number of the new teacher")
    add_parser.add_argument("headclass", help="the class of the new teacher")



    edit_parser = subparsers.add_parser("edit", help="edit the name of a teacher")
    edit_parser.add_argument("id", help="the ID of the teacher to edit")
    edit_parser.add_argument("new_name", help="the new name of the teacher")
    edit_parser.add_argument("new_bod", help="the  new bod of the teacher")
    edit_parser.add_argument("new_phone", help="the new phone number of the teacher")
    edit_parser.add_argument("new_headclass", help="the new class of the teacher")



    remove_parser = subparsers.add_parser("remove", help="remove a teacher")
    remove_parser.add_argument("id", help="the ID of the teacher to remove")

    list_parser = subparsers.add_parser("list", help="list all teacher")
    # list_parser.add_argument("filename", help="the name of the input file")

    args = parser.parse_args()
    x = Teacher("01", "XX","ll","ll","ll")
    x.read_data()
    if args.command == "add":
        new = Teacher(args.id , args.name, args.bod, args.phone, args.headclass)
        x.add_teacher(new)
        x.save()
    elif args.command == "edit":
        # x = Class(args.id, args.new_name)
        x.edit_teacher(args.id, args.new_name, args.new_bod, args.new_phone, args.new_headclass)
        x.save()
    elif args.command == "remove":
        x.remove_teacher(args.id)
        x.save()
    elif args.command == "list":
        x.list_teacher()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()