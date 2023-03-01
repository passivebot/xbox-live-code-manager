# xbox-live-code-manager
An open-source Python program to store and manage Xbox Game Pass membership codes in an SQLite database. The program uses Tkinter to create a graphical user interface (GUI) to enter and display codes. The program uses an SQLite database to store the codes, allowing the user to delete codes from the database. The program also includes a radio button group to select the code type and the membership length.

<img src="https://i.imgur.com/BlSKsqX.png">

### Overview
The Xbox Game Pass Membership Codes Program allows users to store and manage Xbox Game Pass membership codes in an SQLite database. The program provides a graphical user interface (GUI) for users to enter and display codes. The program allows users to select the code type and the membership length via radio buttons. The program also allows users to delete codes from the database. The program is written in Python and uses the Tkinter library to create the GUI.

### Frameworks:
[SQLite](https://www.sqlite.org/index.html) - a relational database management system. 

[Tkinter](https://docs.python.org/3/library/tkinter.html) - a GUI library for Python.

### Language: 

- [Python](https://www.python.org/)

### Flow diagrams:


Insert Code Flow Diagram:

1. User inputs code, type, and length in the GUI.
2. The program connects to the database and checks to see if the code already exists in the database.
3. If the code does not exist, the program generates a code_id and inserts the code into the database.
4. The program displays a success message and clears the input fields.
5. If the code already exists, the program displays an error message.

View Codes Flow Diagram:

1. The user clicks the “View Codes” button.
2. The program connects to the database and queries the codes.
3. The program displays the codes in a message box.
4. The user selects a code to delete.
5. The program deletes the code from the database.
6. The program displays a success message and clears the listbox.

### Requirements:

- Python 3.x 
- SQLite 
- Tkinter


### API:

### Classes:

### Functions:

1. insert_code(): This function inserts a code into the database.
2. view_codes(): This function queries and displays the codes in the database.
3. delete_code(): This function deletes a code from the database.
4. validate_code(): This function validates a code before inserting it into the database.
5. generate_code_id(): This function generates a code_id for a new code.

### Procedure:

1. Install Python and the required libraries.
2. Create the GUI.
3. Connect to the database.
4. Create the functions to insert, view, and delete codes.
5. Create the functions to validate codes and generate code_ids.
6. Add radio buttons to select the code type and the membership length.
7. Test the program.
8. Deploy the program.


