# Function to join given strings
def combo_string(a, b):

    # your code here
    if(len(a) < len(b)):
        short = a
        longer = b
    else:
        short = b
        longer = a

    return short + longer + short