""" 
Why we implement the else functionality with for loops?
We mostly use such implementations in our program when we want to encounter less logical errors and want to know that our program is functioning correctly. In such cases, we will most probably send a print statement inside the code, and based on its execution, we could see if our code is working correctly. In bigger level projects, there are more chances of bugs occurrence, so we try to implement as many such techniques as possible, so we do not have to spend too much time debugging. This will help us to know if our loop is functioning properly or not.

In this tutorial, we learned the implementation of loop-else statement and learned the concept behind it. There is no such case where the use of else statement with for loop is mandatory. It is completely optional. Without using else, we can also set a flag that checks if any of the values met the condition or not. We use the else with a loop because it makes the code more elegant and readable.


"""


khana = ["roti", "Sabzi", "chawal"]

for item in khana:
    if item == "rotiroll":
        break

else:
    print("Your item was not found")
