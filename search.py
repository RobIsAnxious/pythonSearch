from tkinter import *
from tkinter import ttk
import webbrowser

engine_dict = {"google":"https://www.google.com/search?q=",
                "bing":"https://www.bing.com/search?q=",
                "yahoo":"https://search.yahoo.com/search?p="}

search_engines = ['Google', 'Yahoo', 'Bing']


def search():
    if combo.get() == search_engines[0]:
        base_url = engine_dict["google"]
        url = base_url + str(String_Entry.get())
        webbrowser.open(url)
    elif combo.get() == search_engines[1]:
        base_url = engine_dict["yahoo"]
        url = base_url + str(String_Entry.get())
        webbrowser.open(url)
    elif combo.get() == search_engines[2]:
        base_url = engine_dict["bing"]
        url = base_url + str(String_Entry.get())
        webbrowser.open(url)


root = Tk()
root.title('Search in ')



String_Entry = Entry(root)
String_Entry.grid(row=0, column=0, padx=10, pady=50)

Search_Button = Button(root, text='Search', command=search)
Search_Button.grid(row=0, column=1)

Quit_Button = Button(root, text='Quit', command=quit)
Quit_Button.grid(row=0, column=2, padx=10)

combotest = StringVar()
combo = ttk.Combobox(root, textvariable=combotest)
combo['values'] = search_engines
combo.grid(row=1, column=1)

root.configure(background='grey')
root.mainloop()
