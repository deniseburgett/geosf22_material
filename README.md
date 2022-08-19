# Geo Data Science with Python, Fall 2022

---
# Cloning course material to your computer
The course material is available in a public repository (no setup or SSH connection necessary). It will be updated regularily.

#### Initial download
In a console/terminal, change directories to where you want the course material folder to live (below this is $home). The following command copies the entire course material repository to your computer to the folder './geosf22_material'.

```
cd $home
git clone https://github.com/GeoPythonVT/geosf22_material.git
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

---
# Submitting homework

To be able to submit homework, you have to first perform the "Setup at the beginning of the semester" provided below.

After that, whenever you want to submit homework, you need to use 4 commands (ok, really 3, but the first one is a good habit). Execute all of them, each time you make changes to your home work:
```
git pull
## assuming your homwork was saved as HW1_pid.ipynb
git add HW1_pid.ipynb
git commit -m "HW1 submitted!!"
git push
```


## Submitting homework explained

Homework submissions will be accomplished through GitHub. At this point, I am assuming you have worked through the Git Configuration document and successfully added the README file via the command line.

Submitting homework will involve adding your homework to the tracked files, committing changes, and finally pushing your changes to your remote repo.

After you have completed your assignment and saved your final knitted document, in the terminal, do the following:

### Make sure your local copy is synced with your remote copy
```git pull```

### Add your homework files to the list of tracked files
```git add <your homework file>```

### Commit changes you care about
```git commit -m "final version of homework"```

### Push your homework to your remote repo
```git push```


### Basic workflow in summary:

As you work on your homework, you can and should add/commit/push often to save your work! So, save routine, while working on your homework is:

```
cd ~./geosf22_<pid>
git pull
<do work>
git pull
git add ./*ipynb
git add ./*pdf
git commit -m "final version of homework"
git push
```
  
Once you know how to use the Jupyter Notebooks, uyou can also copy the following code cell into a Jupyter Notebook file in your homework repository, and use it to submit homework from that Notebook. The Exclamation Mark allows you to execute shell commands from within a Jupyter Notebook.

```
! git pull
! git add <filename>.ipynb
! git commit -m "final version of homework"
! git push
```

And if you want to learn more about git, check out the docs and the cheatsheet:

https://services.github.com/on-demand/downloads/github-git-cheat-sheet/


---
# Setup at the beginning of the semester

Basically, we need to:

- Configure GitHub and invite me as collaborator to your homework repository (so your homework can be graded).
- Configure Git on the computer to allow pushing to your personal repository (this is how you submit homework)


## A: Setting up GitHub
Part A instructions include creating your GitHub account and homework repository.

#### 1. GitHub account
Sign up for a GitHub account and remember your password.

#### 2. Create your homework repository

On GitHub, create a new, empty repository (Repositories > New) named:

```geosf22_<pid>```

(pid should be your VT PID). For that, click on the 'New' button.

Don’t add a readme file at this time.

Make your repository private.

#### 3. Add me as collaborator to your repository

On GitHub, add me as a collaborator under 'Settings' > 'Manage access' of your repository. Please use my GitHub account name 'GeoPythonVT' or my e-mail address 'swerth@vt.edu'.
  

## B: Setting up your Computer 
Part B instructions will set up your GitHub connection with your computer, after you have already created your GitHub account and repository. These include:

- Install Bash and Git
- Configure Git locally to allow pushing to your personal repository (this is how you submit homework)

#### 1. Install Bash and Git on your computer (skip this step on the lab computers)
Follow instructions (depending on your operating system) for installing Bash, Git and Python/Anaconda on this website: https://annajiat.github.io/2021-07-19-colorado-online/

#### 2. Configure your ssh keys
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

#### 3. Configure your local Git
To do this, type the following in your Terminal, or the Jupyter QTConsole:

```
git config --global user.email <you@example.com>  
git config --global user.name <GitHubUserName> 
```

#### 4. Clone the new repository to your local computer
In the terminal window, change directories to where you want your coursework to live, for instance cd ~/Documents/. Then pull your repository onto your computer:

```git clone git@github.com:<GitHubUserName>/geosf22_<pid>.git```

Enter into your repository, which is currently empty:

```cd geosf22_<pid>```

#### 5. Push your first work to your repository
In the terminal, enter the following commands to create new content for your repository and send it to GitHub:

```
echo "# My Homework for Geos Python Fall 2022" >> README.md
git add README.md
git commit -m "first commit"
git branch -M main
git push -u origin main
```

If this set of commands is successful you are all setup and have made your first commit. If you refresh the Github page, you should see your README.

Note: You will need to repeat only some of these commands, when you submit your homework. These are listed at the top of this README page.
