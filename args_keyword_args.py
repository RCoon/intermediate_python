##: * arguments & ** key word arguments

##: expressions

# Single asterisk "*" means the function is looking for a list
# Double asterisk "**" means the function is looking for a dictionary
def F(*args, **kwargs):
    pass

def F(hair, eyes='Green'):
    print(hair, eyes)

hair_color = 'Brown'

F(hair_color)

F(hair_color, eyes='Blue')