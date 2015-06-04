##: testing

##: WHY?
##: To understand our code better
##: To learn when we made a mistake
##: To know when we are finished
##: To ensure any future program changes/additions don't break our program

def adding(a,b):
    return a + b

def test_adding():
    assert adding(3,4) == 7
    assert adding(3,2) == 5
    assert adding(99,49) == 7
    return "All tests passed for function adding()"

print(test_adding())