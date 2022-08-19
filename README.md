# Geo Data Science with Python, Fall 2022

## Cloning course material to your computer
The course material is available in a public repository (no SSH connection necessary). It will be updated regularily.

#### Initial download
In a console/terminal, change directories to where you want the course material folder to live (below this is $home). The following command copies the entire course material repository to your computer to the folder './geosf22_material'.

```
cd $home
git clone https://github.com/GeoPythonVT/geosf21_material.git
```
You won't be able to push any content to this repository.

#### Update
You can update the repository for new content (without repeatedly downloading the entire repository), whenever there is new material available. For that, enter the folder 'geosf22_material' on your computer and type in the terminal/console:
```
cd $home/geosf22_material
git pull
```
Alternatively, you can download the material directly from the repositories website:
https://github.com/GeoPythonVT/geosf22_material



## Submitting homework

To submit homework, you need to use 4 commands (ok, really 3, but the first one is a good habit). Execute all of them, each time you make changes to your home work:
```
git pull
## assuming your homwork was saved as HW1_pid.ipynb
git add HW1_pid.ipynb
git commit -m "HW1 submitted!!"
git push
```

