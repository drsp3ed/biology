I will firstly explain how the code works before i write it
(I mostly do it for myself just to check up on the instructions while i code)

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
