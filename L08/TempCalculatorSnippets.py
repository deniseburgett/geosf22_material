# Code snippets to write a function converting temperature units
#   to convert temperature values from Kelvin to either Celcius or Fahrenheit


# 1 to convert temperature values from Kelvin to Celcius and 
def kelvinsToCelsius(tempKelvins):
    return tempKelvins - 273.15

# 2 to convert temperature values from Celcius to Fahrenheit.
def celsiusToFahr(tempCelsius):
    return 9/5 * tempCelsius + 32

# 3 to convert temperature values from Kelvin to Fahrenheit
def kelvinsToFahrenheit(tempKelvins):
    tempCelsius = kelvinsToCelsius(tempKelvins)
    tempFahr = celsiusToFahr(tempCelsius)
    return tempFahr


 


# Embed the docstring:
    """
    Function for converting temperature in Kelvins to Celsius or Fahrenheit.

    Parameters
    ----------
    tempK: <numerical>
        Temperature in Kelvins
    convertTo: <str>
        Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Supported values: 'C' | 'F'

    Returns
    -------
    <float>
        Converted temperature.
    """

    
    
    
# Add your code for a function tempCalculator(t,convertTo)
# to convert temperature values from Kelvin to either Celcius or Fahrenheit,
# which works as of the descriptions in the docstring above.
# Make use of the functions provided above!
# Enter the docstring at the top of the function!
