# TKINTER TUTORIAL 4
# CALCULATOR APP
# PYTHON TUTORIALS

from tkinter import *
from tkinter import messagebox
#functions
def btn(numbers):
    global operator 
    operator+=str(numbers)
    txt_input.set(operator)
    
def clear():
    global operator
    operator=''
    txt_input.set('')
    Display.insert(0,'')
def equal():
    global operator
    try:
        sumup = float(eval(operator))
        txt_input.set(sumup)
        operator=''
    except ZeroDivisionError:
        messagebox.showinfo('ZeroDivisionError','division by zero not supported')
    except ValueError:
        messagebox.showinfo('ValueError','Bad format!')
    except SyntaxError:
        messagebox.showinfo('SyntaxError','Bad format!')
    except TypeError:
        messagebox.showinfo('TypeError','Bad format!')
    
root = Tk()
root.title('calculator')
root.resizable(0,0)
operator=''
txt_input = StringVar()
# entry field
Display = Entry(root,font = ('normal',30,'bold'),fg ='white',bg = 'black',justify = 'right',bd = 45,textvariable = txt_input)
Display.grid(columnspan = 4)

# buttons

btc = Button(root,text = 'c',padx = 30 , pady = 10,bd = 4,fg = 'white' ,font = ('arial',30,'bold'), bg = 'black',command = clear)
btc.grid(row = 1, column = 0)

btlb = Button(root, text = '(', padx = 30, pady = 10 , bd = 4, fg = 'white' , bg = 'black', font = ('arial',30,'bold'),command = lambda: btn('('))
btlb.grid(row = 1, column = 1)

btrb = Button(root, text = ')', padx = 30, pady = 10 , bd = 4, fg = 'white' , bg = 'black', font = ('arial',30,'bold'),command = lambda: btn(')'))
btrb.grid(row = 1, column = 2)

btd = Button(root, text = '/', padx = 30, pady = 10 , bd = 4, fg = 'white' , bg = 'black', font = ('arial',30,'bold'),command = lambda: btn('/'))
btd.grid(row = 1, column = 3)

bt7=Button(root,padx=30,pady=10,bd=4,fg='white',bg='black',font=('arial',30,'bold'),text='7',command=lambda:btn(7))
bt7.grid(row=2,column=0)

bt8=Button(root,padx=30,pady=10,bd=4,fg='white',bg='black',font=('arial',30,'bold'),text='8',command=lambda:btn(8))
bt8.grid(row=2,column=1)

bt9=Button(root,padx=30,pady=10,bd=4,fg='white',bg='black',font=('arial',30,'bold'),text='9',command=lambda:btn(9))
bt9.grid(row=2,column=2)

btmul=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='x',bg='black',command=lambda:btn('*'))
btmul.grid(row=2,column=3)

bt4=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),bg = 'black',text='4',command=lambda:btn(4))
bt4.grid(row=3,column=0)

bt5=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),bg = 'black',text='5',command=lambda:btn(5))
bt5.grid(row=3,column=1)

bt6=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),bg = 'black',text='6',command=lambda:btn(6))
bt6.grid(row=3,column=2)

btminus=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='- ',bg='black',command=lambda:btn('-'))
btminus.grid(row=3,column=3)

bt1=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),bg ='black',text='1',command=lambda:btn(1))
bt1.grid(row=4,column=0)

bt2=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='2',bg='black',command=lambda:btn(2))
bt2.grid(row=4,column=1)

bt3=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='3',bg='black',command=lambda:btn(3))
bt3.grid(row=4,column=2)

btplus=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='+',bg='black',command=lambda:btn('+'))
btplus.grid(row=4,column=3)

btpoint=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='. ',bg='black',command=lambda:btn('.'))
btpoint.grid(row=5,column=0)

bt0=Button(root,padx=30,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='0',bg='black',command=lambda:btn(0))
bt0.grid(row=5,column=1)

btequal=Button(root,padx=97,pady=10,bd=4,fg='white',font=('arial',30,'bold'),text='=',bg='black',command=equal)
btequal.grid(row=5,column=2 ,columnspan = 2)

root.mainloop()
