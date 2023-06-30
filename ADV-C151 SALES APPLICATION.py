from tkinter import *

root = Tk()
root.title("Sales Application")
root.geometry("900x400")
root.configure(background = "yellow")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000)

monthlabel = Label(root)
monthlabel["text"] = "Months : " + str(months)
monthlabel.place(relx = 0.5, rely = 0.2, anchor = CENTER)

profitlabel = Label(root)
profitlabel["text"] = "Profits : " + str(profits)
profitlabel.place(relx = 0.5, rely = 0.3, anchor = CENTER)

maxlabel = Label(root)
maxlabel.place(relx = 0.5, rely = 0.5, anchor = CENTER)

minlabel = Label(root)
minlabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)

def max_btn():
    maxprofit = max(profits)
    maxprofitindex = profits.index(maxprofit)
    maxprofitmonth = months[maxprofitindex]
    maxlabel["text"] = "Maximum profit of " + str(maxprofit) + " was given in the month of " + str(maxprofitmonth) + " ."

def min_btn():
    minprofit = min(profits)
    minprofitindex = profits.index(minprofit)
    minprofitmonth = months[minprofitindex]
    minlabel["text"] = "Minimum profit of " + str(minprofit) + " was given in the month of " + str(minprofitmonth) + " ."
    
btn_max = Button(root, text = "Show Max Profitable Month", command = max_btn, bg = "blue", fg = "white")
btn_max.place(relx = 0.5, rely = 0.4, anchor = CENTER)

btn_min = Button(root, text = "Show Min Profitable Month", command = min_btn, bg = "blue", fg = "white")
btn_min.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()

