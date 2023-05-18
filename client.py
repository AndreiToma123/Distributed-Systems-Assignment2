import xmlrpc.client

# Connect to the server
server = xmlrpc.client.ServerProxy('http://localhost:8000')

# Define a function to print the menu options
def print_menu():
    print('What do you want to do?')
    print('1. Add a note:\n2. Get note:\n3. Exit\n')

# Loop until the user chooses to exit
while True:
    print_menu()
    choice = input('Enter your choice: ')

    if choice == '1':
        topic = input('Enter the topic: ')
        text = input('Enter the text: ')
        timestamp = input('Enter the timestamp: ')
        result = server.add_note(topic, text, timestamp)
        print(result)
    elif choice == '2':
        topic = input('Enter the topic: ')
        notes = server.get_notes(topic)
        if notes:
            for note in notes:
                print('Text:', note[0])
                print('Timestamp:', note[1])
        else:
            print('Error! Note does not exist')
    elif choice == '3':
        break
    else:
        print('Error! Choose again (1, 2, 3).\n')
