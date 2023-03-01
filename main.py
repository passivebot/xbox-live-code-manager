import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Create a GUI window
root = tk.Tk()
root.geometry('600x400')
root.title('Xbox Game Pass Membership Codes')

# Create a label and entry widget for the code
code_label = ttk.Label(root, text='Enter Membership Code:')
code_label.pack(pady=10)
code_entry = ttk.Entry(root)
code_entry.pack()

# Create a radio button group for the code type
type_label = ttk.Label(root, text='Membership Type:')
type_label.pack(pady=10)
type_var = tk.StringVar()
type_var.set('Ultimate')
type_radios = ttk.Frame(root)
type_radios.pack()
console_radio = ttk.Radiobutton(type_radios, text='Console', variable=type_var, value='Console')
console_radio.pack(side='left', padx=10)
pc_radio = ttk.Radiobutton(type_radios, text='PC', variable=type_var, value='PC')
pc_radio.pack(side='left', padx=10)
ultimate_radio = ttk.Radiobutton(type_radios, text='Ultimate', variable=type_var, value='Ultimate')
ultimate_radio.pack(side='left', padx=10)

# Create a radio button group for the code length
length_label = ttk.Label(root, text='Membership Length:')
length_label.pack(pady=10)
length_var = tk.StringVar()
length_var.set('14 Days')
length_radios = ttk.Frame(root)
length_radios.pack()
fourteen_day_radio = ttk.Radiobutton(length_radios, text='14 Days', variable=length_var, value='14 Days')
fourteen_day_radio.pack(side='left', padx=10)
one_month_radio = ttk.Radiobutton(length_radios, text='1 Month', variable=length_var, value='1 Month')
one_month_radio.pack(side='left', padx=10)
three_month_radio = ttk.Radiobutton(length_radios, text='2 Months', variable=length_var, value='2 Months')
three_month_radio.pack(side='left', padx=10)
six_month_radio = ttk.Radiobutton(length_radios, text='6 Months', variable=length_var, value='6 Months')
six_month_radio.pack(side='left', padx=10)
twelve_month_radio = ttk.Radiobutton(length_radios, text='12 Months', variable=length_var, value='12 Months')
twelve_month_radio.pack(side='left', padx=10)

# Create a function to insert the code into the database
def insert_code():
    # Get the values from the GUI widgets
    code = code_entry.get()
    code_type = type_var.get()
    code_length = length_var.get()
    
    # Connect to the database and insert the code
    conn = sqlite3.connect('xbox_codes.db')
    c = conn.cursor()

    # Check if the table exists, if not create it
    c.execute('''CREATE TABLE IF NOT EXISTS codes
                 (code_id INTEGER PRIMARY KEY,
                  code TEXT NOT NULL,
                  code_type TEXT NOT NULL,
                  code_length TEXT NOT NULL,
                  used BOOLEAN NOT NULL DEFAULT 0)''')
                  
    # Check if the code already exists in the database
    c.execute("SELECT * FROM codes WHERE code = ?", (code,))
    result = c.fetchone()
    
    # If the code doesn't exist, insert the new code
    if result is None:
        # Get the maximum code_id in the table and increment by 1 for the new code_id
        c.execute("SELECT MAX(code_id) FROM codes")
        result = c.fetchone()
        if result[0] is not None:
            code_id = result[0] + 1
        else:
            code_id = 1
    
        # Insert the new code with the generated code_id
        c.execute("INSERT INTO codes (code_id, code, code_type, code_length, used) VALUES (?, ?, ?, ?, ?)",
                  (code_id, code, code_type, code_length, 0))
        conn.commit()
        conn.close()
        
        # Clear the input fields
        code_entry.delete(0, 'end')
        type_var.set('Ultimate')
        length_var.set('1 Month')

        # Display a success message
        messagebox.showinfo(title='Success', message='Code successfully added!')
    else:
        # Display an error message
        messagebox.showerror(title='Error', message='Code already exists!')
        
# Create a function to display the codes in the database
def view_codes():
    # Connect to the database and query the codes
    conn = sqlite3.connect('xbox_codes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM codes")
    codes = c.fetchall()

    # Display the codes in a message box
    code_list = '\n'.join([f'{code[0]}: {code[1]} ({code[2]} - {code[3]})' for code in codes])
    if not code_list:
        messagebox.showinfo('No Codes Found', 'No membership codes found in the database.')
        return

    # Create a message box to display the codes
    code_box = tk.Toplevel(root)
    code_box.title('Membership Codes')
    code_box.geometry('400x400')

    # Add a label to the message box
    code_label = ttk.Label(code_box, text='Select a code to delete:')
    code_label.pack(pady=10)

    # Add a listbox to the code_box
    list_box = tk.Listbox(code_box, width=50, height=10, selectmode=tk.SINGLE)
    list_box.pack(pady=10)
    
    # Add a scrollbar to the listbox on the right side
    scrolledtext = ttk.Scrollbar(code_box, orient=tk.VERTICAL, command=list_box.yview)
    
    # Add all saved codes to the listbox
    for code in codes:
        list_box.insert(tk.END, f'{code[0]}: {code[1]} ({code[2]} - {code[3]})')
    
    # Add a delete button to the message box
    def delete_code():
        # Get the code_id of the selected code
        selected = list_box.get(tk.ACTIVE)
        code_id = int(selected.split(':')[0])
        
        # Open a connection to the database
        conn = sqlite3.connect('xbox_codes.db')
        c = conn.cursor()
        
        # Delete the code from the database
        c.execute("DELETE FROM codes WHERE code_id=?", (code_id,))
        conn.commit()
        messagebox.showinfo('Code Deleted', 'Membership code has been deleted.')
        list_box.delete('1.0', tk.END)
        list_box.insert(tk.END, '\n'.join([f'{code[0]}: {code[1]} ({code[2]} - {code[3]})' for code in c.fetchall()]))
    
    delete_button = ttk.Button(code_box, text='Delete Code', command=delete_code)
    delete_button.pack(pady=10)

    # Close the connection
    conn.close()

    
    
# Create a button to insert the code into the database
insert_btn = ttk.Button(root, text='Add Code', command=insert_code)
insert_btn.pack(pady=10)

# Create a button to view the codes in the database
view_codes_btn = ttk.Button(root, text='View Codes', command=view_codes)
view_codes_btn.pack(pady=10)


# Start the GUI
root.mainloop()