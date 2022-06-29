import tkinter as tk

gui = tk.Tk()
gui.geometry("450x420")

pic = tk.PhotoImage(file="vegpizza.png")
pic2 = tk.PhotoImage(file="meatpizza.png")
pic3 = tk.PhotoImage(file="coke.png")

can = tk.Canvas(gui, width=130, height=140)
can.create_image(70, 70, image=pic)
can.grid(row=2, column=0)

can2 = tk.Canvas(gui, width=130, height=140)
can2.create_image(70, 70, image=pic2)
can2.grid(row=2, column=1)

can3 = tk.Canvas(gui, width=130, height=140)
can3.create_image(70, 70, image=pic3)
can3.grid(row=2, column=2)


def orderConfirmation():
    win1 = tk.Toplevel(gui)
    win1.geometry("400x400")
    confirmationvegtitle = tk.Label(win1, text = "The vegetables on your pizza are:")
    confirmationvegtitle.grid(row=0, column=0)
    confirmationveg = tk.Label(win1, text = str(listveg))
    confirmationveg.grid(row=1, column=0)
    
    confirmationmeatstitle = tk.Label(win1, text = "The meats on your pizza are:")
    confirmationmeatstitle.grid(row=2, column=0)
    confirmationmeats = tk.Label(win1, text = str(listmeats))
    confirmationmeats.grid(row=3, column=0)

    confirmationdrinkstitle = tk.Label(win1, text = "The drinks in your order are:")
    confirmationdrinkstitle.grid(row=4, column=0)
    confirmationdrinks = tk.Label(win1, text = str(listdrinks))
    confirmationdrinks.grid(row=5, column=0)

    
    #confirmationlist = tk.Listbox(win1)
    #for v in listveg:
        #confirmationlist.insert(tk.END, v)
    #confirmationlist.grid(row=1, column=0)
    

def  orderPrice():
    win2 = tk.Toplevel(gui)
    win2.geometry("200x200")
    pricebasepizza = 10.00
    pricetotalveg = sum(costveg)
    pricetotalmeats = sum(costmeats)
    pricetotaldrinks = sum(costdrinks)
    totalpricepizza = pricebasepizza + pricetotalveg + pricetotalmeats
    subtotalorder = totalpricepizza + pricetotaldrinks
    tax = subtotalorder * .10
    pricetotalorder = subtotalorder + tax
    
    basepricetitle = tk.Label(win2, text = "Base price pizza: ")
    basepricetitle.grid(row=0, column=0)
    basepricenumber = tk.Label(win2, text = format(pricebasepizza, ".2f"))
    basepricenumber.grid(row=0, column=1)
    
    pricevegtitle = tk.Label(win2, text = "Total for vegetables: ")
    pricevegtitle.grid(row=1, column=0)
    pricevegnumber = tk.Label(win2, text = format(pricetotalveg, ".2f"))
    pricevegnumber.grid(row=1, column=1)

    pricemeattitle = tk.Label(win2, text = "Total for meats: ")
    pricemeattitle.grid(row=2, column=0)
    pricemeatnumber = tk.Label(win2, text = format(pricetotalmeats, ".2f"))
    pricemeatnumber.grid(row=2, column=1)

    pricedrinkstitle = tk.Label(win2, text = "Total for drinks: ")
    pricedrinkstitle.grid(row=3, column=0)
    pricedrinksnumber = tk.Label(win2, text = format(pricetotaldrinks, ".2f"))
    pricedrinksnumber.grid(row=3, column=1)

    pricepizzatitle = tk.Label(win2, text = "Total for pizza: ")
    pricepizzatitle.grid(row=4, column=0)
    pricepizzanumber = tk.Label(win2, text = format(totalpricepizza, ".2f"))
    pricepizzanumber.grid(row=4, column=1)

    pricesubtitle = tk.Label(win2, text = "Subtotal order: ")
    pricesubtitle.grid(row=5, column=0)
    pricesubnumber = tk.Label(win2, text = format(subtotalorder, ".2f"))
    pricesubnumber.grid(row=5, column=1)
    
    pricetaxtitle = tk.Label(win2, text = "Tax: ")
    pricetaxtitle.grid(row=6, column=0)
    pricetaxnumber = tk.Label(win2, text = format(tax, ".2f"))
    pricetaxnumber.grid(row=6, column=1)

    pricetotaltitle = tk.Label(win2, text = "Order total: ")
    pricetotaltitle.grid(row=7, column=0)
    pricetotalnumber = tk.Label(win2, text = format(pricetotalorder, ".2f"))
    pricetotalnumber.grid(row=7, column=1)
                                
                                

def  Exit():
     quit()


title =tk.Label(gui, text="Brad's Pizza Shop")
title.grid(row=0, column=0, columnspan=3)
titlebaseprice = tk.Label(gui, text="Base Price For Cheese Pizza 10.00")
titlebaseprice.grid(row=1, columnspan=3)

order = tk.Button(gui, text="Order Confirmation", command=orderConfirmation)
order.grid(row=6, column=1)

orderprice = tk.Button(gui, text="Order Price", command=orderPrice)
orderprice.grid(row=7, column=1)


exit = tk.Button(gui, text="Exit", command=Exit)
exit.grid(row=8, column=1)

listveg = []
costveg = []
listmeats = []
costmeats = []
listdrinks = []
costdrinks = []

onionvar = tk.IntVar()
gpeppervar = tk.IntVar()
mushroomvar = tk.IntVar()
bolivevar = tk.IntVar()

pepperonivar = tk.IntVar()
sausagevar = tk.IntVar()
hamvar = tk.IntVar()
baconvar = tk.IntVar()

cokevar = tk.IntVar()
dietcokevar = tk.IntVar()
sevenupvar = tk.IntVar()
drpeppervar = tk.IntVar()



def isonion():
    if onionvar.get() == 1:
        listveg.append("Onion")
        costveg.append(1.25)
    else:
        listveg.remove("Onion")
        costveg.pop()
        
def isgpepper():
    if gpeppervar.get() == 1:
        listveg.append("Green Pepper")
        costveg.append(1.25)
    else:
        listveg.remove("Green Pepper")
        costveg.pop()
        

def ismushroom():
    if mushroomvar.get() == 1:
        listveg.append("Mushroom")
        costveg.append(1.25)
    else:
        listveg.remove("Mushroom")
        costveg.pop()

def isbolive():
    if bolivevar.get() == 1:
        listveg.append("Black Olive")
        costveg.append(1.25)
    else:
        listveg.remove("Black Olive")
        costveg.pop()


def ispepperoni():
    if pepperonivar.get() == 1:
        listmeats.append("Pepperoni")
        costmeats.append(1.50)
    else:
        listmeats.remove("Pepperoni")
        costmeats.pop()


def issausage():
    if sausagevar.get() == 1:
        listmeats.append("Sausage")
        costmeats.append(1.50)
    else:
        listmeats.remove("Sausage")
        costmeats.pop()

def isham():
    if hamvar.get() == 1:
        listmeats.append("Ham")
        costmeats.append(1.50)
    else:
        listmeats.remove("Ham")
        costmeats.pop()

def isbacon():
    if baconvar.get() == 1:
        listmeats.append("Bacon")
        costmeats.append(1.50)
    else:
        listmeats.remove("Bacon")
        costmeats.pop()


def iscoke():
    if cokevar.get() == 1:
        listdrinks.append("Coke")
        costdrinks.append(2.50)
    else:
        listdrinks.remove("Coke")
        costdrinks.pop()

def isdietcoke():
    if dietcokevar.get() == 1:
        listdrinks.append("Diet Coke")
        costdrinks.append(2.50)
    else:
        listdrinks.remove("Diet Coke")
        costdrinks.pop()
    

def issevenup():
    if sevenupvar.get() == 1:
        listdrinks.append("7 up")
        costdrinks.append(2.50)
    else:
        listdrinks.remove("7 up")
        costdrinks.pop()

def isdrpepper():
    if drpeppervar.get() == 1:
        listdrinks.append("Dr. Pepper")
        costdrinks.append(2.50)
    else:
        listdrinks.remove("Dr. Pepper")
        costdrinks.pop()



containerveg = tk.Frame(gui, bd=4, relief="groove")
titleveg = tk.Label(containerveg, text="Vegetables")
titlecostveg = tk.Label(containerveg, text="1.25 each")
titlecostveg.grid(row=1, column=0)

onion = tk.Checkbutton(containerveg, text="Onion", variable=onionvar, onvalue=1, offvalue=0, command=isonion)
onion.grid(row=2, column=0)

gpepper = tk.Checkbutton(containerveg, text="Green Pepper", variable=gpeppervar, onvalue=1, offvalue=0, command=isgpepper)
gpepper.grid(row=3, column=0)

mushroom = tk.Checkbutton(containerveg, text="Mushroom", variable=mushroomvar, onvalue=1, offvalue=0, command=ismushroom)
mushroom.grid(row=4, column=0)

bolive = tk.Checkbutton(containerveg, text="Black Olive", variable=bolivevar, onvalue=1, offvalue=0, command=isbolive)
bolive.grid(row=5, column=0)


containermeats = tk.Frame(gui, bd=4, relief="groove")
titlemeats = tk.Label(containermeats, text="Meats")
titlecostmeats = tk.Label(containermeats, text="1.50 each")
titlecostmeats.grid(row=1, column=0)


pepperoni = tk.Checkbutton(containermeats, text="Pepperoni", variable=pepperonivar, onvalue=1, offvalue=0, command=ispepperoni)
pepperoni.grid(row=2, column=0)

sausage = tk.Checkbutton(containermeats, text="Sausage", variable=sausagevar, onvalue=1, offvalue=0, command=issausage)
sausage.grid(row=3, column=0)

ham = tk.Checkbutton(containermeats, text="Ham", variable=hamvar, onvalue=1, offvalue=0, command=isham)
ham.grid(row=4, column=0)

bacon = tk.Checkbutton(containermeats, text="Bacon", variable=baconvar, onvalue=1, offvalue=0, command=isbacon)
bacon.grid(row=5, column=0)


containerdrinks = tk.Frame(gui, bd=4, relief="groove")
titledrinks = tk.Label(containerdrinks, text="Drinks")
titlecostdrinks = tk.Label(containerdrinks, text="2.50 each")
titlecostdrinks.grid(row=1, column=0)


coke = tk.Checkbutton(containerdrinks, text="Coke", variable=cokevar, onvalue=1, offvalue=0, command=iscoke)
coke.grid(row=2, column=0)

dietcoke = tk.Checkbutton(containerdrinks, text="Diet Coke", variable=dietcokevar, onvalue=1, offvalue=0, command=isdietcoke)
dietcoke.grid(row=3, column=0)

sevenup = tk.Checkbutton(containerdrinks, text="7 up", variable=sevenupvar, onvalue=1, offvalue=0, command=issevenup)
sevenup.grid(row=4, column=0)

drpepper = tk.Checkbutton(containerdrinks, text="Dr. Pepper", variable=drpeppervar, onvalue=1, offvalue=0, command=isdrpepper)
drpepper.grid(row=5, column=0)

titleveg.grid(row=0, column=0)
titlemeats.grid(row=0, column=0)
titledrinks.grid(row=0, column=0)

containerveg.grid(row=3, column=0)
containermeats.grid(row=3, column=1)
containerdrinks.grid(row=3, column=2)













gui.mainloop()
