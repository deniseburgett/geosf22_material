# Code snippets for Lesson 7 on Statements

# Selection 1
# -----------

yesterday = 14
today = 13
tomorrow = 13

if yesterday < today:
    print('A: yesterday was colder than today')
elif today != tomorrow:
    print('B: yesterday was not the same temperature as today')
elif yesterday > tomorrow:
    print('C: yesterday was warmer than today')
elif today == today:
    print('D: yesterday and today had equal temperatures')

    
    
# Selection 2
# -----------
weather = 'Rain' # 'Sun', 'Clouds'
wind = 'Windy'   # 'notWindy'

# 1) Write a selection that tells you to just stay home, if it is `Rain` and `Windy` => multiple conditions
# 2) Add `elif` option for only `Rain`: wearing a raincoat, otherwise no raincoat needed. => multiple selections

#if (weather == 'Rain') and (wind == 'Windy'):
# continue the selection!




# Selection 3
# -----------
# Rewrite the temperature selection into a ternary if statement. Set temperature to any value.
temperature = 17

if temperature > 25:   
    print('it is hot')
    
    
    
# Iteration 1
# -----------
# Calculate the sample mean in a for loop
X = [123, 87, 96, 24, 104, 16]



# Iteration 2
# -----------
# Write a while loop that checks a password!
# Reading user input:
yourText = input()
# The notebook cell will prompt you to enter any string and it would display the same string on the screen. Enter your text and hit a plain <Enter>. Then print the variable to screen to see your result!



# Iteration 3
# -----------
# Use else for While and compound statements for the password check!


