import password_generator

# Try Yourself
# Convert the previous example to a package in your project.
# Import password_generator_02 from the package into main.py.
# Write a program in main.py that prints the annotations for the function and inspects its arguments.
# PyCharm makes it quick and easy to create packages and modules. Consult this tutorial Links to an external site.(JetBrains 2021) if you need guidance.

password = password_generator.password_generator_01(15, "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+{}|>?<[];'\,./~`><")
print("this is my password: ", password)