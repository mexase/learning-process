# What is Git?
Git is a open source Version Control System (VCS) originally developed in 2005 by Linus Torvalds.

## What it for?
Git works as a repository, recording a full history of changes made in files and coordinating work on those files among a team. Git is used for multiple
destinations but the most common is for software development.

# Basics of  Git

## Commands
* **git config** --global user.name "User" - Set your username
* **git config** --global user.email "user@user.com" - Set your email.
* **git config** --global core.editor vim - Set your editor in this example i used vim.
* **git init** - Start a repository (needs to be in a directory).
* **git add file.ext** - Adds a file to staging area
* **git add .** - Adds all files to staging.
* **git add .ext** - Adds all files with the same extension, in this example is *.ext.
* **git rm file.html** - Delete a file or directory, in this example file.html will be erased.
* **git reset HEAD file.ext** - Remove files from staging area.
* **git log** - Shows log with full information.It can be simplified using git log --oneline.
* **git checkout script** - Create a branch named script.
* **git commit -v** - Commit a file with a message and files diff. Can be used with -a parameter and commit multiple files.
* **git status** - Displays information about the repository.
* **git diff** - Compares a previously registered file and a new, displaying the changes made.
* **git tag -a v1.0 -m "Initial version"** - Create a tag with message.
* **git remote** - Show remote repository
* **git push [remote-name] [branch]** - Used to send files to server.
* **git pull** -
* **git branch name** - Create a branch. With parameter -d [name of branch] you can delete a branch.
* **git checkout [branchname]** - Change between branches.
* **git merge** - Incorporates file changes of a branch from commits into the current branch.




## Ignoring
You can ignore a extension, a directory or a single file. Create a file and name as .gitignore and add
***.ext** - Ignore all files with .ext extension.
** !file.ext** - Ignore all files but not file.ext.  
**texts/** - Ignore a entire directory including subdirectory and its files.   
