ADDRESSBOOK = {}


def input_error(inner):
    def wrap(*args):
        try:
            return inner(*args)
        except IndexError:
            return "Give me name and phone please"
    return wrap


@input_error
def add_handler(data):
    name = data[0].title()
    phone = data[1]
    ADDRESSBOOK[name] = phone
    return f"Contact {name} with phone {phone} was saved"


@input_error
def change_handler(data):
    name = data[0].title()
    phone = data[1]
    if name in ADDRESSBOOK:
        ADDRESSBOOK[name] = phone
        return f"Phone number for {name} was updated to {phone}"
    else:
        return f"Contact {name} does not exist"


@input_error
def phone_handler(data):
    name = data[0].title()
    if name in ADDRESSBOOK:
        return f"{name}'s phone number is {ADDRESSBOOK[name]}"
    else:
        return f"Contact {name} does not exist"


def exit_handler(*args):
    return "Good bye!"


def hello_handler(*args):
    return "How can I help you?"


def show_all_handler(*args):
    if ADDRESSBOOK:
        contacts = "\n".join(f"{name}: {phone}" for name, phone in ADDRESSBOOK.items())
        return contacts
    else:
        return "No contacts found."


def command_parser(raw_str: str):
    elements = raw_str.split()
    command = elements[0].lower()
    for handler, aliases in COMMANDS.items():
        for cmd in aliases:
            if cmd.startswith(command):
                return handler(elements[1:])


COMMANDS = {
    add_handler: ["add", "додай", "+"],
    change_handler: ["change"],
    phone_handler: ["phone"],
    show_all_handler: ["show all"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"],
}


def main():
    while True:
        user_input = input(">>> ")
        result = command_parser(user_input)
        print(result)
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()