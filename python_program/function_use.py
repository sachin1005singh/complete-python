#use of function
def greet(name,msg ="good morning"):
    """ this function is for basic use of
    function."""
    print("hello",name + ',' , msg)

greet("sachin","good morning!")

# use of arbitrary arguments
def greets(*names):
    for nam in names:
        print("weclcome to delhi ",nam)
    
