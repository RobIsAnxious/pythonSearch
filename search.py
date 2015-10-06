from tkinter import *
import webbrowser

engine_dict = {"google":"https://www.google.com/search?q=",
                "bing":"https://www.bing.com/search?q=",
                "yahoo":"https://search.yahoo.com/search?p="}

def select_engine():
    prompt = "Select a search engine. (Google, Bing, Yahoo)"
    print(prompt)
    while True:
        search_engine = input('> ').lower()
        if search_engine in engine_dict:
            engine_name = search_engine.capitalize()
            base_url = engine_dict[search_engine]
        else:
            print('I couldn\'t find that search engine. Try again.\n')
            print(prompt)
            continue
        return engine_name, base_url

engine_name, base_url = select_engine()

root = Tk()
root.title('Search in ' + engine_name)


String_Entry = Entry(root)
String_Entry.grid(row=0, column=0, padx=50, pady=50)


def search():
    url = base_url + str(String_Entry.get())
    webbrowser.open(url)

Search_Button = Button(root, text='Search', command=search)
Search_Button.grid(row=0, column=1)



Quit_Button = Button(root, text='Quit', command=quit)
Quit_Button.grid(row=0, column=2)

root.mainloop()
