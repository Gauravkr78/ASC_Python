# Global variable (global namespace)

global_var = "I'm global"


def outer_function():

# Enclosing variable

    enclosing_var = "I'm in outer function"


    def inner_function():

        # Local variable

        local_var = "I'm in inner function"

        print(local_var) # Local scope

        print(enclosing_var) # Enclosing scope

        print(global_var) # Global scope

        print(len("hello")) # Built-in scope


    inner_function()


# Test the scopes

outer_function()

print(global_var) # Accessible from global scope