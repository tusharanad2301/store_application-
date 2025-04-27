from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Food Store")
root.config(bg="#2C3E50")  # Dark blue-gray background

def Total_Bill():
    vdosa = 100
    vcake = 150
    vmomos = 90
    vpizza = 240
    vfry = 99
    vburger = 70

    ndosa = int(dosa.get()) if dosa.get() else 0
    ncake = int(cake.get()) if cake.get() else 0
    nmomos = int(momos.get()) if momos.get() else 0
    npizza = int(pizza.get()) if pizza.get() else 0
    nfrench = int(fry.get()) if fry.get() else 0
    nburger = int(burger.get()) if burger.get() else 0

    total = (ndosa * vdosa) + (nmomos * vmomos) + (ncake * vcake) + (npizza * vpizza) + (nfrench * vfry) + (nburger * vburger)

    prnt.delete(1.0, END)
    prnt.insert(END, "--------------------------------------\n")
    prnt.insert(END, f"{'Item':<15}{'Qty':<5}{'Price':<10}{'Total'}\n")
    prnt.insert(END, "--------------------------------------\n")
    
    if ndosa > 0:
        prnt.insert(END, f"Dosa           {ndosa:<7}   {vdosa:<15}{ndosa * vdosa}\n")
    if ncake > 0:
        prnt.insert(END, f"Cake           {ncake:<7}   {vcake:<15}{ncake * vcake}\n")
    if nmomos > 0:
        prnt.insert(END, f"Momos      {nmomos:<7}  {vmomos:<15}{nmomos * vmomos}\n")
    if npizza > 0:
        prnt.insert(END, f"Pizza          {npizza:<7}  {vpizza:<15}{npizza * vpizza}\n")
    if nfrench > 0:
        prnt.insert(END, f"French Fry   {nfrench:<7}  {vfry:<15}{nfrench * vfry}\n")
    if nburger > 0:
        prnt.insert(END, f"Burger       {nburger:<7}  {vburger:<15}{nburger * vburger}\n")

    prnt.insert(END, "--------------------------------------\n")
    prnt.insert(END, f"{'Total':<30}{total}\n")
    prnt.insert(END, "--------------------------------------\n")   

    prnt.insert(END, f"\n Total: {total}")
    
def clear():
    prnt.delete(1.0, END)

Label(root, text="MEGA MART", fg="#ECF0F1", bg="#2C3E50", font=("Helvetica", 24, "bold")).pack(fill=BOTH)

# Menu
f = Frame(root, width=250, height=380, relief=RAISED, bd=4, highlightbackground="#ECF0F1", bg="#34495E", highlightthickness=2)
f.place(x=10, y=50)

# Order 
f1 = Frame(root, width=550, height=150, relief=RAISED, bd=4, highlightbackground="#ECF0F1", bg="#34495E", highlightthickness=2)
f1.place(x=10, y=440)

# Bill View
f2 = Frame(root, width=520, height=380, relief=RAISED, bd=4, highlightbackground="#ECF0F1", bg="#34495E", highlightthickness=2)
f2.place(x=270, y=50)

Label(f, text="MENU", font=("Helvetica", 20, "bold"), fg="#ECF0F1", bg="#34495E").place(x=80, y=0)

# Dish
Label(f, text="Dosa       ---------         100/-", font=("Helvetica", 14, "bold"), fg="#ECF0F1", bg="#34495E").place(x=4, y=55)
Label(f, text="Cake       ---------         150/-", font=("Helvetica", 14, "bold"), fg="#ECF0F1", bg="#34495E").place(x=4, y=95)
Label(f, text="Momos      ---------        90/-", font=("Helvetica", 14, "bold"), fg="#ECF0F1", bg="#34495E").place(x=4, y=135)
Label(f, text="Pizza      ---------          240/-", font=("Helvetica", 14, "bold"), fg="#ECF0F1", bg="#34495E").place(x=4, y=175)
Label(f, text="French Fry ---------      99/-", font=("Helvetica", 14, "bold"), fg="#ECF0F1", bg="#34495E").place(x=4, y=215)
Label(f, text="Burger     ---------         70/-", font=("Helvetica", 14, "bold"), fg="#ECF0F1", bg="#34495E").place(x=4, y=255)

dosa = StringVar()
cake = StringVar()
momos = StringVar()
pizza = StringVar()
fry = StringVar()
burger = StringVar()

# Entry fields for the menu items
Label(f1, text="Dosa", font=("Times new roman", 15, "bold"), width=12, bg="#34495E", fg="#ECF0F1").grid(row=1, column=0)

edosa = Entry(f1, font=("arial", 15, "bold"), textvariable=dosa, width=12, bd=6)
edosa.grid(row=1, column=1)

Label(f1, text="Cake", font=("Times new roman", 15, "bold"), bg="#34495E", fg="#ECF0F1", width=12).grid(row=2, column=0)

ecake = Entry(f1, font=("arial", 15, "bold"), width=12, bd=6, textvariable=cake)
ecake.grid(row=2, column=1)

Label(f1, text="Momos", font=("Times new roman", 15, "bold"), width=12, bg="#34495E", fg="#ECF0F1").grid(row=3, column=0)

emomos = Entry(f1, font=("arial", 15, "bold"), width=12, bd=6, textvariable=momos)
emomos.grid(row=3, column=1)

Label(f1, text="Pizza", font=("Times new roman", 15, "bold"), bg="#34495E", fg="#ECF0F1", width=12).grid(row=1, column=3)

epizza = Entry(f1, font=("arial", 15, "bold"), width=12, bd=6, textvariable=pizza)
epizza.grid(row=1, column=4)

Label(f1, text="French Fry", font=("Times new roman", 15, "bold"), width=12, bg="#34495E", fg="#ECF0F1").grid(row=2, column=3)

efrench = Entry(f1, font=("arial", 15, "bold"), textvariable=fry, width=12, bd=6)
efrench.grid(row=2, column=4)

Label(f1, text="Burger", font=("Times new roman", 15, "bold"), bg="#34495E", fg="#ECF0F1", width=12).grid(row=3, column=3)

eburger = Entry(f1, font=("arial", 15, "bold"), width=12, bd=6, textvariable=burger)
eburger.grid(row=3, column=4)

# Text widget to display the bill
prnt = Text(f2, font=("calibri", 15, "bold"), fg="#ECF0F1", bg="#2C3E50", width=45, height=15)
prnt.place(x=18, y=0)

Button(root, text="Buy", command=Total_Bill, bg="#1ABC9C", fg="white", font=("Helvetica", 15, "bold")).place(x=700, y=455)

Button(root, text="Exit", command=clear, bg="#E74C3C", fg="white", font=("Helvetica", 15, "bold")).place(x=700, y=500)

root.mainloop()
