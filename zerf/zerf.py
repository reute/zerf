import sys, enum

class Command(enum.Enum):
    addw = 0
    addp = 1

commands = {
        "addw": Command.addw,
        "addp": Command.addp,
}

# checking for first argument
if len(sys.argv) <= 1:
    print("no arguments, exiting")
    sys.exit(0)

# first argument must be a command
command = commands.get(sys.argv[1])
if command == None:
    print("command not found")
    sys.exit(0)

print("command is " + command.name)
print("moving on")

if command == Command.addw:
    pass
    # second Argument must be a Date
