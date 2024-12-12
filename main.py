from tkinter import *


window = Tk()
window.title("BMI Calculater")
window.minsize(width=200, height=200)
window.config(padx=30,pady=30)

def calculateBMI():
    weight = weight_entry.get()
    height = height_entry.get()

    if weight == "" or height == "":
        label3.config(text="Enter your weight and height")

    else:
        try:
            bmi = float(weight) / (float(height)/100) ** 2
            label3.config(text=f"Your BMI: {bmi}")
        except:
            label3.config(text=("Enter a valid number"))


        if bmi <= 18.5:
            label4.config(text="You are Underweight")

        elif 18.5 < bmi <= 24.9:
            label4.config(text="You are Normalweight")
        elif 25 <= bmi <= 29.9:
            label4.config(text="You are Pre-obesity")
        elif 30 <= bmi <= 34.9:
            label4.config(text="You are Obesity1")
        elif 35 <= bmi <= 39.9:
            label4.config(text="You are Obesity2")
        elif 40 <= bmi:
            label4.config(text="You are Obesity3")





label = Label(text="Enter Your Weight(kg)")
label.pack()

weight_entry = Entry(width=10)
weight_entry.pack()

label2 = Label(text="Enter Your Height(cm)")
label2.pack()

height_entry = Entry(width=10)
height_entry.pack()



calculate = Button(text="Calculate", command=calculateBMI)
calculate.pack()

label3 = Label()
label3.pack()

label4 = Label()
label4.pack()








window.mainloop()