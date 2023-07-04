import argparse
from Class import *

def main():
    parser = argparse.ArgumentParser(description="Classroom management CLI")
    subparsers = parser.add_subparsers(dest="command", help="sub-command help")

    add_parser = subparsers.add_parser("add", help="add a new classroom")
    add_parser.add_argument("id", help="the ID of the new classroom")
    add_parser.add_argument("name", help="the name of the new classroom")


    edit_parser = subparsers.add_parser("edit", help="edit the name of a classroom")
    edit_parser.add_argument("id", help="the ID of the classroom to edit")
    edit_parser.add_argument("new_name", help="the new name of the classroom")

    remove_parser = subparsers.add_parser("remove", help="remove a classroom")
    remove_parser.add_argument("id", help="the ID of the classroom to remove")

    list_parser = subparsers.add_parser("list", help="list all classrooms")
    # list_parser.add_argument("filename", help="the name of the input file")

    args = parser.parse_args()
    x = Class("01", "XX")
    x.read_data()
    if args.command == "add":
        new = Class(args.id , args.name)
        x.add_classroom(new)
        x.save()
    elif args.command == "edit":
        # x = Class(args.id, args.new_name)
        x.edit_classroom(args.id, args.new_name)
        x.save()
    elif args.command == "remove":
        x.remove_classroom(args.id)
        x.save()
    elif args.command == "list":
        x.list_classrooms()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()