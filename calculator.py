import tkinter as tk 

HEIGHT=1000
WIDTH=1000

expression = ""

def button_plus_clicked():
    global expression
    expression = expression + "+"
    print(expression)
    text_box.insert(tk.INSERT, "+")

def button_minus_clicked():
    global expression
    expression = expression + "-"
    print(expression)
    text_box.insert(tk.INSERT , "-")

def button_multi_clicked():
    global expression
    expression = expression + "*"
    print(expression)
    text_box.insert(tk.INSERT , "*")

def button_divide_clicked():
    global expression
    expression = expression + "/"
    print(expression)
    text_box.insert(tk.INSERT , "/")

def button_1_clicked():
    global expression
    expression = expression + "1"
    print(expression)
    text_box.insert(tk.INSERT , "1")

def button_2_clicked():
    global expression
    expression = expression + "2"
    print(expression)
    text_box.insert(tk.INSERT , "2")

def button_3_clicked():
    global expression
    expression = expression + "3"
    text_box.insert(tk.INSERT , "3")
   

def button_4_clicked():
    global expression
    expression = expression + "4"
    print(expression)
    text_box.insert(tk.INSERT , "4")

def button_5_clicked():
    global expression
    expression = expression + "5"
    print(expression)
    text_box.insert(tk.INSERT , "5")

def button_6_clicked():
    global expression
    expression = expression + "6"
    print(expression)
    text_box.insert(tk.INSERT , "6")

def button_7_clicked():
    global expression
    expression= expression + "7"
    print(expression)
    text_box.insert(tk.INSERT , "7")

def button_8_clicked():
    global expression
    expression= expression + "8"
    print(expression)
    text_box.insert(tk.INSERT , "8")

def button_9_clicked():
    global expression
    expression= expression + "9"
    print(expression)
    text_box.insert(tk.INSERT , "9")

def button_0_clicked():
    global expression
    expression= expression + "0"
    print(expression)
    text_box.insert(tk.INSERT , "0")

def cleared():
    text_box.delete('1.0' , tk.END)
    global expression
    expression = ""

def equate():
    text_box.insert(tk.INSERT , "\n" + "= " + str(eval(expression)))

root = tk.Tk()

root.title('Calculator')
text_box = tk.Text(root, font=10)
text_box.pack()

canvas = tk.Canvas(root , height=HEIGHT , width=WIDTH , bg="cyan")
canvas.pack()


frame = tk.Frame(root , bg="medium spring green", bd=10)
frame.place(relx=0 , rely=0.4 ,  relwidth=1 , relheight=0.6)

button=tk.Button(frame , text="+" , font=1000000000, bg="cyan" , command=button_plus_clicked)
button.place(relx=0, rely=0, relwidth=0.2 , relheight=0.3) 

button_2 = tk.Button(frame , text="-" , font=100000000 , bg="cyan", command=button_minus_clicked)
button_2.place(relx=0 , rely=0.25 , relwidth=0.2 , relheight=0.3)

button_3 = tk.Button(frame , text="*" , font=100000000 ,bg="cyan" ,  command=button_multi_clicked)
button_3.place(relx=0 , rely=0.5 , relwidth=0.2 , relheight=0.3)

button_100 = tk.Button(frame , text="/" , font=1000000000 ,bg="cyan" , command=button_divide_clicked)
button_100.place(relx=0 , rely=0.75 , relwidth=0.2 , relheight=0.3)

button_4 = tk.Button(frame , text="1" , font=10000 ,bg="peachpuff" ,  command=button_1_clicked)
button_4.place(relx=0.3 , rely=0 , relwidth=0.15 , relheight=0.3)

button_5 = tk.Button(frame , text="2" , font=10000 ,bg="peachpuff" ,  command=button_2_clicked)
button_5.place(relx=0.45 , rely=0 , relwidth=0.15 , relheight=0.3)

button_6 = tk.Button(frame , text="3" , font=10000 ,bg="peachpuff" , command=button_3_clicked)
button_6.place(relx=0.6 , rely=0 , relwidth=0.15 , relheight=0.3)

button_7 = tk.Button(frame , text="4" , font=10000 ,bg="peachpuff" ,  command=button_4_clicked)
button_7.place(relx=0.3 , rely=0.3 , relwidth=0.15 , relheight=0.3)

button_8 = tk.Button(frame , text="5" , font=10000 ,bg="peachpuff" ,  command=button_5_clicked)
button_8.place(relx=0.45 , rely=0.3 , relwidth=0.15 , relheight=0.3)

button_9 = tk.Button(frame , text="6" , font=10000 ,bg='peachpuff' , command=button_6_clicked)
button_9.place(relx=0.6 , rely=0.3 , relwidth=0.15 , relheight=0.3)

button_10 = tk.Button(frame , text="7" , font=10000 ,bg="peachpuff" ,  command=button_7_clicked)
button_10.place(relx=0.3 , rely=0.6 , relwidth=0.15 , relheight=0.3)

button_11 = tk.Button(frame , text="8" , font=10000 ,bg="peachpuff", command=button_8_clicked)
button_11.place(relx=0.45 , rely=0.6 , relwidth=0.15 , relheight=0.3)

button_12 = tk.Button(frame , text="9" , font=10000 ,bg="peachpuff" ,  command=button_9_clicked)
button_12.place(relx=0.6 , rely=0.6 , relwidth=0.15 , relheight=0.3)

button_13 = tk.Button(frame , text="0" , font=10000 ,bg="slateblue1" , command=button_0_clicked)
button_13.place(relx=0.8 , rely=0 , relwidth=0.15 , relheight = 0.3)

button_14 = tk.Button(frame , text="C" , font=10000 ,bg="slateblue1", command=cleared)
button_14.place(relx=0.8 , rely=0.3 , relwidth=0.15 , relheight = 0.3)

button_15 = tk.Button(frame , text="=" , font=10000 ,bg="slateblue1", command=equate)
button_15.place(relx=0.8 , rely=0.6 , relwidth=0.15 , relheight = 0.3)

root.mainloop()