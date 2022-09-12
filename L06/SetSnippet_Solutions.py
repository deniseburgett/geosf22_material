##############################
# load code into a jupyter notebook with the magic command %load:
# %load ../geosf22_material/L06/SetSnippet.py 

# or without file path:
# %load SetSnippet.py 
##############################

restaurantsInOurTown = [
    'La Madeleine',
    'Our Daily Bread',
    'Olive Garden',
    'Pommes de Terre',
    'Jean"s',
    'LaBoca', 
    'Pont Blanc', 
    'Berliner Kueche', 
    'Olive Garden']

setFrench = set(['La Madeleine','Our Daily Bread','Pommes de Terre','Pont Blanc'])
setPark = set(['LaBoca', 'La Madeleine', 'Berliner Kueche', 'Olive Garden'])


# Is the restaurant 'Madeleine' located near a park?
'La Madeleine' in setPark    # Membership

# Are all french restaurants also park restaurants?
setFrench < setPark    # Subset

# Are all park restaurants also french restaurants?
setFrench > setPark    # Superset

# We are just hungry, any restaurant that is either french or at a park is fine!
setFrench | setPark    # Union

# Find a french restaurant near a park!
setFrench & setPark    # Intersection

# Find a restaurant that is near a park but not french style!
setPark - setFrench    # Difference

# My friend does not like french and near a park is not fancy enough. Which place can we go?
set(restaurantsInOurTown) - setFrench - setPark 
