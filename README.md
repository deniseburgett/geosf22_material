# Geo Data Science with Python, Fall 2022

## Cloning course material to your computer
The course material is available in a public repository (no setup or SSH connection necessary). It will be updated regularily.

#### Initial download
In a console/terminal, change directories to where you want the course material folder to live (below this is $home). The following command copies the entire course material repository to your computer to the folder './geosf22_material'.

```
cd $home
git clone https://github.com/GeoPythonVT/geosf21_material.git
```
You won't be able to push any content to this repository.

#### Update
Material will be added to the repository regularily. You can update the repository for new content (without repeatedly downloading the entire repository), whenever there is new material available. For that, enter the folder 'geosf22_material' on your computer and type in the terminal/console:
```
cd $home/geosf22_material
git pull
```
Alternatively, you can download the material directly from the repositories website:
https://github.com/GeoPythonVT/geosf22_material

## Submitting homework

To be able to submit homework, you have to first perform the "Setup at the beginning of the semester" provided below.

After that, whenever you want to submit homework, you need to use 4 commands (ok, really 3, but the first one is a good habit). Execute all of them, each time you make changes to your home work:
```
git pull
## assuming your homwork was saved as HW1_pid.ipynb
git add HW1_pid.ipynb
git commit -m "HW1 submitted!!"
git push
```

However, an even saver routine, while working is:

```
cd ~./geosf22_<pid>
git pull
<do work>
git pull
git add ./*ipynb
git add ./*pdf
git commit -m "homework submission"
git push
```

If you want to read more about this:

https://services.github.com/on-demand/downloads/github-git-cheat-sheet/


---
# Setup at the beginning of the semester

## A Create GitHub account and repository


## B GitHub setup on your computer

This instructions are for setting up your GitHub connection with your computer, after you have already created your GitHub account and repository.

- Install Bash and Git
- Configure Git locally to allow pushing to your personal repository (this is how you submit homework)

### Install Bash and Git on your computer
Follow instructions (depending on your operating system) for installing Bash, Git and Python/Anaconda on this website: https://annajiat.github.io/2021-07-19-colorado-online/

### Configure your ssh keys
1.) If you know your SSH key, skip to point 5.

2.) Open a Git Bash (Windows) or terminal (MacOS) on your computer, or in Anaconda/Jupyter Lab (click on + to the left and then on Terminal).

3.) In the terminal window, type:
```ssh-keygen```

4.) Ideally you will use a short passphrase different from your pid password, but can simply hit enter for most (or all prompts).

5.) Into the Git Bash or terminal, type:
```cat ~/.ssh/id_rsa.pub```
... and copy the entire output. (Note: this works also in a Windows command window. The Windows equivalent of the "cat" command is "type", and you will have to replace "/" with "\".)

6.) Now, you need to add this to your GitHub profile. In Github, click on the pulldown (top right) to view your profile and choose "Settings" then "SSH and GPG" keys.

7.) Click on New SSH key, paste your RSA public key there and save.

### Configure your local Git
To do this, type the following in your Terminal, or the Jupyter QTConsole:

git config --global user.email <you@example.com>  
git config --global user.name <GitHubUserName> 


### Clone the new repository to your local computer
In the terminal window, change directories to where you want your coursework to live, for instance cd ~/Documents/. Then pull your repository onto your computer:

```git clone git@github.com:<GitHubUserName>/geosf21_<pid>.git```
