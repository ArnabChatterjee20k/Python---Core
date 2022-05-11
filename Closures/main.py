def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function

        print(msg+"dff")

    return printer  # returns the nested function


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
del print_msg # still after deleting print_msg another() will run.
another()