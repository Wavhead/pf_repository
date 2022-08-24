from tkinter import *
from datetime import datetime

window = Tk()
window.title("Chatbot")
window.geometry("400x520")
window.resizable(width=FALSE, height=FALSE)

# Menu
main_menu = Menu(window)
#Submenu
file_menu = Menu(window)

main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Save As")
file_menu.add_command(label="Quit", command=window.destroy)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
window.config(menu=main_menu)

# Chatbot Dialog
def send():
    send = "You => "+ entry.get().lower()
    chat.insert(END, "\n" + send)
    
    if(entry.get().lower()=="hi"):
        chat.insert(END, "\n" + "Bot => Hello, how can i help you?")

    elif(entry.get().lower()=="date") or (entry.get().lower()=="time") or (entry.get().lower()=="what is the time?"):
        chat.insert(END, "\n" + "Bot => The current time is:" + str(datetime.now()))

    elif(entry.get().lower()=="python") or (entry.get().lower()=="what is python?"):
        chat.insert(END, "\n" + "Bot => Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.")

    elif(entry.get().lower()=="indesign") or (entry.get().lower()=="what is indesign?") or (entry.get().lower()=="should i use indesign?"):
        chat.insert(END, "\n" + "Bot => I would rather divide by 0 than use InDesign!")

    elif(entry.get().lower()=="help"):
        chat.insert(END, "\n" + "Bot => You can ask me questions about programming languages, date and time, or other IM related topics.")

    elif(entry.get().lower()=="kjartan") or (entry.get().lower()=="kjartan haavik"):
        chat.insert(END, "\n" + "Bot => Kjartan is a cool dude.")

    elif(entry.get().lower()=="åsmund") or (entry.get().lower()=="åsmund kringlebotten"):
        chat.insert(END, "\n" + "Bot => Åsmund is mathematically the most chill person ever.")

    elif(entry.get().lower()=="marko"):
        chat.insert(END, "\n" + "Bot => Polo.")

    elif(entry.get().lower()=="html"):
        chat.insert(END, "\n" + "Bot => HTML (HyperText Markup Language) is the most basic building block of the Web. It defines the meaning and structure of web content.")

    elif(entry.get().lower()=="java") or (entry.get().lower()=="javascript") or (entry.get().lower()=="js"):
        chat.insert(END, "\n" + "Bot => JavaScript, often abbreviated JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.")

    elif(entry.get().lower()=="im") or (entry.get().lower()=="informasjonsteknologi og medieproduksjon"):
        chat.insert(END, "\n" + "Bot => Cool Kids Club or somthin, idk...")

    else:
        chat.insert(END, "\n" + "Bot => I dont recognize that command, have you checked your spelling?")


chat = Text(window, bg="black", font=("Consolas", 12), foreground="#efefef")
chat.place(x=6,y=6, height=385, width=370)

entry = Entry(window, width=100, bg="black", font=("Consolas", 12), foreground="#efefef")
entry.place(x=128, y=400, height=88, width=260)

send = Button(window, text="SEND", command=send, bg="black", font=("Consolas", 20), activebackground="#efefef", foreground="#efefef")
send.place(x=6, y=400, height=88, width=115)

scrollbar = Scrollbar(window, command=chat.yview, cursor="heart")
scrollbar.place(x=375, y=5, width=385)

window.mainloop()