#Pass by Value

def change_string(s):
    s = s + " World"
    print("Inside function:", s)

text = "Hello"
change_string(text)
print("Outside function:", text)


#Pass by Reference

def add_element(s):
    s.add(50)
    print("Inside function:", s)

myset = {10, 20, 30}
add_element(myset)
print("Outside function:", myset)
