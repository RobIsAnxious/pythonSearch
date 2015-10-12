from tkinter import *
from tkinter import ttk
import webbrowser

engine_dict = {"google":"https://www.google.com/search?q=",
                "bing":"https://www.bing.com/search?q=",
                "yahoo":"https://search.yahoo.com/search?p="}

search_engines = ['Google', 'Yahoo', 'Bing']


def search():
    if combo.get() == '':
        combo.set('Google')
        
    url = engine_dict[combo.get().lower()] + str(String_Entry.get())
    webbrowser.open(url)


#Interface setup
root = Tk()
root.title('pythonSearch')

String_Entry = Entry(root)
String_Entry.grid(row=0, column=0, padx=10)

Search_Button = Button(root, text='Search', command=search)
Search_Button.grid(row=0, column=2)

Quit_Button = Button(root, text='Quit', command=quit)
Quit_Button.grid(row=0, column=3, padx=10)

Drop_Down = StringVar()
combo = ttk.Combobox(root, textvariable=Drop_Down)
combo['values'] = search_engines
combo.grid(row=1, column=0)

root.configure(background='grey')
root.mainloop()
