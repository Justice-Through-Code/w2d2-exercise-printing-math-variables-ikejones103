
def convert_100_to_celsius():
    # Convert a temperature of 100 degrees fahrenheit to celsius
    fahrenheit_100 = 100
    celsius_100 = (fahrenheit_100 - 32) * 5/9
    # Save this to a variable called celsius_100, and use print() to print out the value
    print("100 degrees Fahrenheit is equal to", celsius_100, "degrees Celsius.")

    # Is the resulting temperature you get an integer or float?
   
    # Print 'float' if it is a float or 'int' if it is an int

    # How do you know? Write a comment below your code explaining how you know which it is

#convert_100_to_celsius()

def convert_0_to_celsius():
    # Convert a temperature of 0 degrees fahrenheit to celsius
    fahrenheit_0 = 0
    celsius_0 = (fahrenheit_0 - 32) * 5/9
    # Save this to a variable called celsius_0, and use print() to print out the value
    print("0 degrees Fahrenheit is equal to", celsius_0, "degrees Celsius.")
    #convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    fahrenheit_34_2 = 34.2
    celsius_34_2 = (fahrenheit_34_2 - 32) * 5/9
    # Do this one all in one print statement without saving any variables
    print("34.2 degrees Fahrenheit is equal to", celsius_34_2, "degrees Celsius.")
    #convert_34_2_to_celsius()
    
    # Convert 5 degrees Celsius to Fahrenheit
    celsius_5 = 5
    fahrenheit_5 = (celsius_5 * 9/5) + 32
    print("5 degrees Celsius is equal to", fahrenheit_5, "degrees Fahrenheit.")
    # Now, can you convert back?


def convert_5_to_fahrenheit():
    # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    celsius_5 = 5
    fahrenheit_5 = (celsius_5 * 9/5) + 32
    print("5 degrees Celsius is equal to", fahrenheit_5, "degrees Fahrenheit.")
#convert_5_to_fahrenheit()

def hotter_temp():
    # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
    celsius_30_2 = 30.2
    fahrenheit_30_2 = (celsius_30_2 * 9/5) + 32

# Compare temperatures
    if fahrenheit_30_2 > 85.1:

        print("30.2 degrees Celsius is hotter than 85.1 degrees Fahrenheit.")
    else:
        print("85.1 degrees Fahrenheit is hotter than 30.2 degrees Celsius.")

    # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively

#hotter_temp()
