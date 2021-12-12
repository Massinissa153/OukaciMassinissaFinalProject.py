# create a pizza ordering app using tkinter.
# first I will import everything from tkinter.
from tkinter import *
from PIL import ImageTk, Image

# create a window.
pizza = Tk()
pizza.geometry("1300x800")
pizza.title("My Pizza Ordering App")

# create labels and entry widgets
# for the user to enter their names, addresses, and phone numbers
name_label = Label(pizza, text="Enter your name: ")
name_label.grid(row=0, column=0)

name_entry = Entry(pizza, width=20, borderwidth=5)
name_entry.grid(row=0, column=1)

address_label = Label(pizza, text="Enter your address: ")
address_label.grid(row=0, column=3)

address_entry = Entry(pizza, width=20, borderwidth=5)
address_entry.grid(row=0, column=4)

phone_label = Label(pizza, text="Enter your phone number: ")
phone_label.grid(row=0, column=5)

phone_entry = Entry(pizza, width=20, borderwidth=5)
phone_entry.grid(row=0, column=6)

# creating a label to welcome the customers to Indianapolis Pizza.
lbl12 = Label(pizza, text="Welcome to Indianapolis Pizza", font="Helvetica 12", bg="#58F", borderwidth=10)
lbl12.grid(row=5, column=4)

# I added two pictures and resized to fit in the window.
my_pic = Image.open("pizza1.jfif")
resized = my_pic.resize((320, 200), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)

my_label = Label(image=new_pic)
my_label.grid(row=4, column=0)

# Adding pictures and resizing them
my_pic_2 = Image.open("Pizza_High_quality_wallpapers0.jpg")
resized_2 = my_pic_2.resize((320, 200), Image.ANTIALIAS)
new_pic_2 = ImageTk.PhotoImage(resized_2)

my_label = Label(image=new_pic_2)
my_label.grid(pady=70)

# Added an exit button in the window.
button_exit = Button(pizza, text="Exit", command=pizza.quit, borderwidth=5)
button_exit.grid(row=300, column=100)

# creating a pizza list.
my_pizza_list = ["Pepperoni", "Cheese", "Mushrooms", "Steak", "Olives"]
# Adding the pizza listbox to my window.
pizza_list = Listbox(pizza, selectmode=MULTIPLE, bg="#58F", borderwidth=5)
pizza_list.grid(row=4, column=1)
for item in my_pizza_list:
    pizza_list.insert(0, item)

# Adding a label that lets the customer know where to select the toppings for their pizza.
label10 = Label(pizza, text="select your topping:", bg="#58F", fg="Black", borderwidth=10)
label10.grid(row=3, column=1)

# Adding a label to let the customer where to select their drinks
label11 = Label(pizza, text="Select your drink: ", bg="red", fg="Yellow", borderwidth=10)
label11.grid(row=3, column=3)

# creating a drinks list.
my_drinks_list = ["Pepsi", "Coca", "Corona", "Stella"]

drinks_list = Listbox(pizza, selectmode=MULTIPLE, bg="red", fg="Yellow", borderwidth=5)
drinks_list.grid(row=4, column=3)
for drink in my_drinks_list:
    drinks_list.insert(0, drink)


# define the add pizza button.
def add_pizza():
    result = ""
    for item in pizza_list.curselection():
        result = result + str(pizza_list.get(item)) + "\n"

        add_lbl.config(text="Your topping selection: " + "\n" + result)


# define the add_ drink button
def add_drink():
    result = ""
    for drink in drinks_list.curselection():
        result = result + str(drinks_list.get(drink)) + "\n"

        add_lbl2.config(text="Your drink selection: " + "\n" + result)


# defining the checkout button.
# creating a new window that will open after the user click the checkout button
def checkout():
    top = Toplevel()
    top.geometry("400x400")
    top.title('view your receipt')
    text1 = name_entry.get()
    new_lbl = Label(top, text="Name: " + text1)
    new_lbl.grid(row=5, column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(top, text="Address: " + text2)
    new_lbl2.grid(row=5, column=3)

    text3 = phone_entry.get()
    new_lbl3 = Label(top, text="Phone: " + text3)
    new_lbl3.grid(row=5, column=4)


# after adding the toppings the customer can click add toppings then they will display on the screen.
add_lbl = Label(pizza, text="")
add_lbl.grid(row=5, column=1)

# after adding the toppings the customer can click add toppings then they will display on the screen
add_lbl2 = Label(pizza, text="")
add_lbl2.grid(row=6, column=1)

# Adding a add_pizza button to confirm the toppings that customer selected.
add_button = Button(pizza, text="Add Topping", command=add_pizza, borderwidth=5)
add_button.grid(row=3, column=11)

# Adding add_drink button to confirm the drink that the customer has selected.
add_Drink_btn = Button(pizza, text="Add Drink", command=add_drink, borderwidth=5)
add_Drink_btn.grid(row=3, column=12)

# Adding a checkout button
btn = Button(pizza, text="CheckOut", command=checkout, borderwidth=5)
btn.grid(row=2, column=11)

mainloop()
