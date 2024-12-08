def tempconverter(celsius):
    
    kelvin = celsius + 273.15 
    #converting celsius to kelvin
    
    fahrenheit = celsius * 1.80 + 32.00 
    #converting celcius to farenheit
    
    return [kelvin, fahrenheit] #returning the value of kelvin and farenheit in an array form
    
celcius_input = float(input("Enter a number in celsius: "))
result = tempconverter(celcius_input) 

print(f"Kelvin: {result[0]:.5f}, Fahrenheit: {result[1]:.5f}")                     
