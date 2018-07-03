import tkinter as tk

window = tk.Tk()

window.title("Pic Grabber")
tk.Label(window, text="Enter Url Below").pack()

window.configure(background="grey")
window.geometry("300x300")

entry = tk.Entry(window)
entry.place(x=60, y=75)
entry.insert(0, 'URL')


def pressed():
    print("button")


tk.Button(window, text='Get Pics', command=pressed).place(x=110, y=200)


window.mainloop()




