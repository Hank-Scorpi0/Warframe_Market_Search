import requests as req
import urllib
import urllib.request
from urllib.request import urlopen as req_url
import string
import json
#import tkinter as tk
from tkinter import *

#user_input = input("Enter names as comma seperate values:")

#convert_list = user_input.split(", ")

def searchval(inputvalue):
    try:

        inputvalue = inputvalue.lower()
        inputvalue = inputvalue.replace(" ", "_")
        #print(inputvalue)
        res = req_url("https://api.warframe.market/v1/items/" + inputvalue + "/statistics")
        data = res.read()
        parsed = json.loads(data)
        
        length = len(parsed['payload']['statistics_closed']['48hours'])-1
        cleaned = json.dumps(parsed, indent=4)
        
        part_val = str(parsed['payload']['statistics_closed']['48hours'][length]['avg_price'])
        inputvalue = inputvalue.replace("_", " ")
        inputvalue = inputvalue.title()

        #print(inputvalue + ": " + part_val)
        chat.configure(state='normal')
        chat.insert('end', inputvalue + ": " + part_val + '\n')
        chat.configure(state='disabled')

    except:
        inputvalue = inputvalue.replace("_", " ")
        inputvalue = inputvalue.title()
        chat.configure(state='normal')
        chat.insert('end', inputvalue + ": " + "Part not found" + '\n')
        chat.configure(state='disabled')

def create_val():
    user_input = textBox.get()
    convert_list = user_input.split(", ")
    print(convert_list)
    for i in convert_list:
        searchval(i)

root = Tk()
chatBox = Scrollbar(root)
chat = Text(root, wrap='word', state='disabled', width=50,
            yscrollcommand=chatBox.set)
chatBox.configure(command=chat.yview)

chat.grid(row=0, columnspan=2, sticky='ewns')
chatBox.grid(row=0, column=2, sticky='ns')
Label(root, text="Parts: ").grid(row=1, column=0)

#textBox = Entry(root, bd=0, width=40, bg="gray")
textBox = Entry(root, bd=0, width=50)
textBox.grid(row=1, column=1)

Button(root, text="Search", command=create_val).grid(row=2, columnspan=2)

root.mainloop()


