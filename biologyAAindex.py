"""
I will firstly explain how the code works before i write it
(I mostly do it to myself just to check up on the instructions while i code)

Here is the algorithm:
We have an entry field. User inputs number of specie A to the entry field. If user wants to input more, he pushes
the button to clear an empty field and register the prev number to the system.
When user is finished, he pushed the button and the label field shows the result
(result will be shown to 4 significant figures after the point).
Calculation: 

1) numerator. A function will take all of the values from the entry fields and adds them to the list. We will need this
list for the calculation of the denominator further. Then, sum() function is used to sum up all the elements of the list.
total = sum(list)
numerator = total*(total-1)

2) denominator. For loop will be used here. Now i think of making this a readme file and uploading this thing
to github but i will think about it. Anyways.
So basically, denominator is a variable that will initially be equal to zero. if there will be a trouble with division (for example,
if the denominator is zero or the answer is negative), respectful exception will be thrown (in python language: raised). The for loop
will go through the elements of the list that I have mentioned earlier. For each iteration, the denominator variable
will be increased (+= operator) by element*(element-1).

At the end, result = numerator / denominator
and the result variable will be outputted.

I am using the customtkinter library for this task. 

I will do my best to comment (documentate) all of the important lines.

UPD: 03.05.2024 08:52 apparently teacher wants to add names as well. Well ok, I added another label, another entry field, another list
and modified the void new() function a little bit. I hope now he will like it.

UPD: 06.05.2024 03:19 i decided to add a saving feature. Now after calculating the index user will be able to click the save button and
the result (lists of names and amounts in a form of dictionary) together with the index will be saved as a .txt file.
After user hits the "refresh" buttonn, the "save" button will be unpacked. If the user presses the "save" button again while
having the file, content of the file will be rewritten.
"""

import customtkinter as ctk

root = ctk.CTk()
ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('system')
root.geometry('500x500')
root.title('Biodiversity Index Calculator')

labframe = ctk.CTkFrame(root)
enframe = ctk.CTkFrame(root)
butframe = ctk.CTkFrame(root)

entry = ctk.CTkEntry(enframe, width = 190, placeholder_text="Input the amount of a specie.")
nentry = ctk.CTkEntry(enframe, width = 190, placeholder_text="Input the name of a specie.")
label = ctk.CTkLabel(labframe, text="Continue to add numbers and names until you are done.")
numlabel = ctk.CTkLabel(labframe, text="Current list of numbers: []")
namelabel = ctk.CTkLabel(labframe, text="Current list of names: []")

l: list = []
l2: list = []
di: dict = {}

def new() -> None:
    global l
    global l2
    text = entry.get()
    name = nentry.get()

    try: 
        if float(text) > 0 and name.strip() != "":
            l.append(float(entry.get()))
            l2.append(name)
            label.configure(text="Continue to add species until you are done.")

        elif float(text) < 0:
            label.configure(text="Amount of your species cannot be negative.")
        elif name.strip() == "":
            label.configure(text="Please, enter the name of your specie.")
        else:
            label.configure(text="If amount of this specie is 0, do not add it here.")  

    except:
        label.configure(text = "Input value is Not a Number (NaN).")

    entry.delete(0, len(text))
    nentry.delete(0, len(name))
    namelabel.configure(text = f'Current list of names: {l2}')
    numlabel.configure(text = f'Current list of numbers: {l}')

def convert(l, di) -> dict:
    di = dict(l)
    return di

def calculate() -> None:
    global l
    total = sum(l)
    numerator = total*(total-1)

    denominator = 0

    for i in l:
        denominator += i*(i-1)

    if denominator == 0:
        raise ZeroDivisionError("Denominator equal to zero. All of your species' amounts are 1.")
        res.configure(text = "Denominator equal to zero. All of your species' amounts are 1.")

    elif numerator == 0:
        res.configure(text = "Numerator equal to zero. You have 1 organism.")

    else:
        result = numerator/denominator
        if result > 0:
            res.configure(text = f"Biodiversity Index is equal to {result:.4f}")
        else:
            res.configure(text = f"Biodiversity Index is equal to {result:.4f}. Please, try again. Your data is incorrect.")

    global lists
    lists = convert(list(zip(l2, l)), di)

    save.pack(pady = 5)

def refresh() -> None:
    global l
    global l2

    l.clear()
    l2.clear()
    namelabel.configure(text = f'Current list of names: {l2}')
    numlabel.configure(text = f'Current list of numbers: {l}')

    res.configure(text = "Result")
    save.pack_forget()

def save() -> None:
    f = open("biodiversity_index.txt", "w")
    f.write(f"{lists}\n{res.cget('text')}")
    f.close()

    
plus = ctk.CTkButton(butframe, text = "Add Specie", command = new)
done = ctk.CTkButton(butframe, text = "I'm done", command = calculate)
save = ctk.CTkButton(butframe, text = "Save data", command = save)
refresh = ctk.CTkButton(root, text = "Refresh", command = refresh, fg_color="green")
res = ctk.CTkLabel(root, text = "Result")


labframe.pack()
label.pack()
namelabel.pack()
numlabel.pack()

enframe.pack()
nentry.pack()
entry.pack()

butframe.pack(pady = 5)
plus.pack()
done.pack(pady=5)

res.pack(padx=5)
refresh.pack(padx=5)

root.mainloop()
#ok so in total i spent like 3-4 hours on this :/