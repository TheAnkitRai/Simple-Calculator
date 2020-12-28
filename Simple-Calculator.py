# Program to build a GUI based simple calculator


from tkinter import *


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnclrdisplay():
    global operator
    operator=""
    text_input.set("")

def btnEqualsinto():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""


cal = Tk()
cal.title("Calculator")
operator=""
text_input=StringVar()

# Displaying the pressed button on the calculator
txt_display= Entry(cal, font=('arial',20, 'bold'), textvariable = text_input, bd=30, insertwidth=4, bg="powder blue", justify= 'right').grid(columnspan=4)


# Creating number and operators buttons

#======================================= First row buttons ======================================================
btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='7', command = lambda: btnclick(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='8', command = lambda: btnclick(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='9', command = lambda: btnclick(9)).grid(row=1, column=2)
btn_add = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='+', command = lambda: btnclick('+')).grid(row=1, column=3)


#======================================= Second Row buttons ==============================================================

btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='4', command = lambda: btnclick(4)).grid(row=2, column=0)
btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='5', command = lambda: btnclick(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='6', command = lambda: btnclick(6)).grid(row=2, column=2)
subtract = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='-', command = lambda: btnclick('-')).grid(row=2, column=3)


#======================================= Third row buttons ================================================================

btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='1', command = lambda: btnclick(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='2', command = lambda: btnclick(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='3', command = lambda: btnclick(3)).grid(row=3, column=2)
multiply = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='*', command = lambda: btnclick('*')).grid(row=3, column=3)


#======================================= Fourth row buttons ===============================================================

btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='0', command = lambda: btnclick(0)).grid(row=4, column=0)
btn_clear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='C', command = lambda: btnclrdisplay()).grid(row=4, column=1)
btn_equals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='=', command = lambda: btnEqualsinto()).grid(row=4, column=2)
btn_divide = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('arial',20, 'bold'), bg="powder blue", text='/', command = lambda: btnclick('/')).grid(row=4, column=3)


cal.mainloop()
