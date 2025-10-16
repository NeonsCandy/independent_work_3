import sys

def print_help():
    print("Використання: python sys_tool.py [--help]")
    print("Виводить 'командна строка' при прямому запуску.")
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print_help()
    print("командна строка")