from module import Add
a = Add(1,2)
print("app.py",a)
"""
    Output
    module.py 3
    app.py 3

    # If we debug the code we will see that when interpreter is encoutering import the module it is running all the code inside the module then it is running the app

    if we do print __name__ along with the other ojects in both the files we will see this ouput

    module.py 3 module # name of the module file
    app.py 3 __main__ # name of the current file
"""