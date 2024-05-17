import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime


WIDTH = 300
HEIGHT = 350

window = tk.Tk()
window.title("Body Monitor")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)
window.iconphoto(False, tk.PhotoImage(file='heart.png'))


#
#功能運作
def get_value():
    user = getname.get()
    sexual = gender.get()
    h = getheight.get()
    w = getweight.get()
    age = getage.get()

    #build user's data
    user_data = {
        'name':user,
        'sexual':gender,
        'height':h,
        'weight':w,
        'age':age }
    
    userdata = [user, sexual, h, w, age]
    return userdata



# 按鈕動作
def pop_up():
    user_data = get_value()
    cond = False

    # 有東西沒填就False
    for x in user_data:
        
        if x == '':
            messagebox.showwarning("Warning", "Something miss")
            cond = False
            break

        else:
            cond = True

    # True才執行按鈕動作
    if cond == True:
        age_dict = {1: 'boy', 2: 'girl'}
        h = float(getheight.get()) / 100
        w = float(getweight.get())
        bmi = w / h / h
        text = BMI_Standard(bmi)
        
        t1 = f"Hi, {getname.get()}. \n"
        if gender.get() == 1 or gender.get() == 2:
            t2 = f"You are a {getage.get()}-year-old {age_dict[gender.get()]}, \n"
            t3 = f"with {getheight.get()} cm and {getweight.get()} kg. \n"
            t4 = f"Your BMI is {bmi:.2f} \n"

            messagebox.showinfo("Result", t1 + t2 + t3 + t4 + text)

        else:
            t2 = "How can you not know your gender? \n"

            messagebox.showinfo("Result", t1 + t2)


    #return t1 + t2 + t3 + t4



#存檔的
def save():
    #get date
    current_dateTime = datetime.now()
    y = current_dateTime.year
    m = current_dateTime.month
    d = current_dateTime.day

    date = str(y) + '-' + str(m) + '-' + str(d)

    #get user's data
    userdata = get_value()
    user = userdata[0]
    sexual = userdata[1]
    h = float(userdata[2]) / 100
    w = float(userdata[3])
    bmi = w / h / h
    text = BMI_Standard(bmi)
    
    
    ofile = user + '_' + date + '.dat'
    
    with open (ofile, 'w') as outfile:
        t1 = f"Hey, {user}! \n"

        if sexual == 1 or sexual == 2:
            t2 = f"Your BMI is {bmi:.2f} on {m}/{d}, {y}. \n"

        else:
            t2 = f"You do not know your gender on {m}/{d}, {y} is {bmi:.2f}, haha! \n"

            
        outfile.write(t1 + t2 + text)

    messagebox.showinfo("Result", "Data saved!")


# BMI的標準
def BMI_Standard(bmi: float):
    
    standard = [18.5, 24, 27]
    if bmi < standard[0]:
        t = 'You are underweight, eat more!'

    elif standard[0] <= bmi < standard[1]:
        t = 'Great! You are in a perfect shape!'

    elif standard[1] <= bmi < standard[2]:
        t = 'Ooh! You are a little bit overweight!'

    else:
        t = 'You are too heavy!! Try to lose weight!'

    return t




#版面配置
#menu
menu = tk.Menu()  #建立一條menu列
menu2 = tk.Menu(menu, tearoff = 0)  #在menu下建立一行menu2，並把虛線刪掉
menu2.add_command(label = '存檔', command = save)   #新增一個menu2的功能
menu2.add_command(label = '關閉', command = window.destroy)
menu.add_cascade(label = '功能', menu = menu2)  #主視窗加入主選單
window.config(menu = menu)  #顯示menu


#
#label
#name
lb = tk.Label(text = "你叫啥: ", fg = "black", font = ('bold', 10), height = 1)
lb.place(x = 0, y = 0)

#gender
lb2 = tk.Label(text = "男的女的: ", fg = "black", font = ('bold', 10), height = 1)
lb2.place(x = 0, y = 50)

#height
lb3 = tk.Label(text = "你多高: ", fg = "black", font = ('bold', 10), height = 1)
lb4 = tk.Label(text = "公分", fg = "black", font = ('bold', 10), height = 1)
lb3.place(x = 0, y = 100)
lb4.place(x = 262, y = 100)

#weight
lb5 = tk.Label(text = "你多重: ", fg = "black", font = ('bold', 10), height = 1)
lb6 = tk.Label(text = "公斤", fg = "black", font = ('bold', 10), height = 1)
lb5.place(x = 0, y = 150)
lb6.place(x = 262, y = 150)

#age
lb7 = tk.Label(text = "你多老: ", fg = "black", font = ('bold', 10), height = 1)
lb7.place(x = 0, y = 200)

#
#Entry
#get user's name
getname = tk.Entry(width = 33)
getname.place(x = 55, y = 0)

#get user's height
getheight = tk.Entry(width = 28)
getheight.place(x = 55, y = 100)

#get user's weight
getweight = tk.Entry(width = 28)
getweight.place(x = 55, y = 150)

#get user's age
getage = tk.Entry(width = 33)
getage.place(x = 55, y = 200)

#
#Radiobutton
#mygender = tk.StringVar()
gender = tk.IntVar() #這組的名稱為gender
radio1 = tk.Radiobutton(text = '男的', variable = gender, value = 1, command = 'getsex') 
radio2 = tk.Radiobutton(text = '女的', variable = gender, value = 2, command = 'getsex')
radio3 = tk.Radiobutton(text = '我不知道', variable = gender, value = 3, command = 'getsex') 
radio1.place(x = 70, y = 50)
radio2.place(x = 140, y = 50)
radio3.place(x = 210, y = 50)




#
#Button
button1 = tk.Button(text = "確認", width = 7, height = 2, command = pop_up)
button1.place(x = 120, y = 255)



window.mainloop()




