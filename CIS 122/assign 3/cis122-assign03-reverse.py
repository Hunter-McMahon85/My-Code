# CIS 122 spring 2021 reverse
# Author: Hunter McMahon
# Partner: completed solo 
# Description: *beep beep beep beep beep* as the truck reverses

#reverses the order of charecters in a string
def reverse(textgoeshere):
    """
    reverses the order of charecters in a string
    uses a for loop to reveres the charecter order in a string
    Args:
    textgoeshere (should be a string but code will convert it if not):string that we want to reverse the order of
    Returns:
    output is a textgoeshere reversed
    """
    textout = ""
    instring = str(textgoeshere)
    textlength = len(instring)
    for i in range(textlength):
        textout = textout + instring[(textlength-1)-i]
    print('Original:', instring)
    #print('Reversed:', textout)
    return textout

#test case

#reverse("When in  the Course of human events"                                                                         When in  the Course of human events")

#submission case
print('Reversed:', reverse("The quick brown fox jumps over the lazy dog"))
