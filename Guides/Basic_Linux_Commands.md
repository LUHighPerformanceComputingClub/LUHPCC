# Welcome to the HPCC Guide of Basic Linux Commands (for total newbies)

## Intro (read intro before starting)

First, I would highly recommend to install some sort of Linux based Operating System (OS) on your computer. These commands should work for the most part on any Linux OS so do not be worried. I recommend installing Linux in a Virtual Machine (VM) as a start before you decide on leaving your current OS (presumably Windows 🤮).

### Recommended Linux OSes:

Yes there are many Linux OSes (aka distros) so it may not be easy to choose the one that is perfect for you but here is a list of popular choices:

1. Ubuntu (extremely popular)
2. Zorin (if you love the windows feel)
3. Fedora (well rounded)
4. Pop_OS (good for gaming out of the box)
5. Arch (if you love doing everything manually and spending countless hours making your system run)

You can also install any other Linux distro and compare them on <https://distrowatch.com/>

Use either VMWare Player or VirtualBox to set up your Linux distro (unless you really know what you are doing in which case I would not expect you to be reading this guide)

## Start With the Basics

### File Navigation

#### Present Working Directory

Open a terminal in whichever Linux distro you like and type:

```plaintext
pwd
```

The "pwd" command shows the Present Working Directory aka the folder you are currently in. Normally, by default it will output /home/\[your username\]. This command is not used very often, but it is useful to know if you ever forget which directory you are in.

#### List Folder Contents

Now that you know how to find which directory you are in, lets list the the files in the directory with:

```plaintext
ls
```

This command will LiSt all the subdirectories and files in your current directory. Typically, in the home directory it will show your Documents, Downloads, etc. If you would like to see hidden files or more information about the files in your directory, you may use:

```plaintext
ls -al
```

#### Create New Directory

The next command will let you make a new directory:

```plaintext
mkdir test-directory
```

The "mkdir" command creates a new directory on your computer and gives is the name "test-directory" which we specified. You can change "test-directory" to anything you want the name of the directory to be. If you want to use any name with a space in it, use double quote around the name. For example, "Directory with spaces"

#### Change Directories

Now that you have created a directory, it is time to change your working to directory. To choose to go into "test-directory":

```plaintext
cd test-directory
```

"cd" stands for Change Directory. To see that we have successfully change directories use the "pwd" command to see that we are now in /home/\[your username\]/test-directory. To change directly to the home directory you may also use:

```plaintext
cd ~
```

If you would like to move up one directory use:

```plaintext
cd ..
```

#### Create Files

Let's learn how to create a file now:

```plaintext
touch test-file
```

This command creates and empty file named test-file. To edit it you may use any text editor. Some common terminal text editors are "nano" and "vim". For beginners I strongly recommend on starting out with "nano". To see your new "test-file" you may use the "ls" command.

#### Move Files and Folders

If you would like to rename or move your file use the move command:

```plaintext
mv /path/to/source /path/to/destination
```

For example, to rename our "test-file" you may use:

```plaintext
mv test-file test-file-2
```

Use the "ls" command to see those you have made.

#### Copy Files and Folders

The copy command works in the same way as the move command:

```plaintext
cp /path/to/source /path/to/destination
```

So if we wanted to make a copy of "test-file-2", we would do:

```plaintext
cp test-file-2 test-file-2-backup
```

Using "ls" we can see that both files are now in our test-directory.

#### Removing Files and Folders

To remove a file use the "rm" command:

```plaintext
rm test-file-2-backup
```

Using "ls" again we can see that "test-file-2-backup" is deleted permanently.

Removing folders requires another flag "-r" which stands for recursively. For example of we wanted to delete the "test-directory" with "test-file-2" within it we would:

```plaintext
cd ..
rm -r test-directory
```

This first goes up a directory by using the change directory command, and then removes "test-directory" and all of the files and directories within.

#### Viewing the Contents of a File

To print the contents of a file to the terminal you can use the "cat" command:

```plaintext
cat /path/to/file
```

All of the contents of the file will be output on the terminal.

### Commands as Root User

BE VERY CAREFUL WHENEVER RUNNING COMMANDS AS ROOT!

Your system has a very good chance at breaking if you do not know what you are doing with root commands! Now that you ahve been warned, let me explain what the idea of root is. If you are familiar with Microsoft Windows root is like the administrator, but even more powerful. Running commands as a root user is a great tool, but you must be very careful to know exactly what you are doing before running a command as root.

Root commands are used to make changes to the operating system that would not normally be made on a day to day basis. Some examples of commans you would typically run as root would be: installing software, changing disk partitions, and modifying system configuration files.

Now that you have been warned, here is the key to running any command as root:

```plaintext
sudo [command]
```

All you have to do to run a command as root is put "sudo" right before the command. Sometimes it will also ask you to put in your password just to make sure you would like to make this change.

### Installing Software

To install any software, the first step is knowing the distribution you are using. If you do not know which Linux Distribution you are using, you can use the following command:

```plaintext
cat /etc/os-release
```

Now that you know your Linux Distibution, let's install some programs. Installation of programs happens through a package manager. Package managers keep track of which software is installed on your system and if it needs to be updated. There are three major package managers used on Linux each used on different distributions:

1. apt - used on Debian based systems like Ubuntu, Zorin, and Pop_OS
2. dnf - used by Fedora based systems
3. pacman - used by Arch based systems like EndeavourOS and Manjaro

#### apt Package Management

Before doing most things with apt it is best to update the list of packages available from apt with:

```plaintext
sudo apt update
```

This command finds out the newest version of each package available to install.

To upgrade the system and upgrade every package to the newest available version on your system use:

```plaintext
sudo apt upgrade
```

To search for the name of a specific package use:

```plaintext
sudo apt search [package]
```

 Use the list of results to help determine the exact name of the package you woud like to install.

Installing the selected package is as easy as running:

```plaintext
sudo apt install [package]
```

Uninstalling packages is also very easy:

```plaintext
sudo apt remove [package]
```

If you would like to rid your system of any packages that are unecessary, which may happen from time to time, run these commands to clean up the system:

```plaintext
sudo apt autoremove
sudo apt purge
```

#### dnf Package Management

Package management with dnf is also fairly simple.

Updating the list of packages to the newest versions and upgrading your system to the latest available version can be done with one command:

```plaintext
sudo dnf upgrade
```

To find the exact name of the package you would like to install:

```plaintext
sudo dnf search [package]
```

Installation of packages is also as simple as:

```plaintext
sudo dnf install [package]
```

And removal/uninstallation is just as easy:

```plaintext
sudo dnf remove [package]
```

If you would like to remove unused and/or unecessary packages on your system:

```plaintext
sudo dnf autoremove
```

This will automatically remove anything that the system does not need to run.

#### pacman Package Management

Management of packages with pacman is slightly more difficult than other package managers, but it is definitely doable. 

If you would like to update all of your packages on your system use:

```plaintext
sudo pacman -Syu
```

This command makes use of flags which are the letters after the dash. Each of these letters tells pacman what you would like to do. It is sort of like a special shorthand for commands. In the case of this command, "S" stands for syncronize which gets the latest packages, "y" stands for refresh the local cached packages, and "u' stands for update.

Searching for packages is done with the flags:

```plaintext
sudo pacman -Ss [package]
```

In this command the "s" stands for search.

Installing new packages is done with:

```plaintext
sudo pacman -S [package]
```

Uninstalling packages requires a couple more letters:

```plaintext
sudo pacman -Rns [package]
```

This will remove the package and all of the packages it depended on to run (dependencies) which are not dependent of any other package.

To get rid of uneeded packages on your system you may use:

```plaintext
sudo pacman -Qdtq | pacman -Rs -
```

This is useful to help free up space from unrequired packages.

## Final Notes

I encourage you to explore all of these Linux commands yourself and force yourself to try to use Linux often. It may be a struggle to learn something new and it may seem like a hassle at first but once you get past the barriers, it is something many people fall inlove with.

### Other Resources

Bandit by OverTheWire is a great game to learn how to use these commands and learn more about SSH: <https://overthewire.org/wargames/bandit/>

TLDR Pages - A great readable alternative to man community developed <https://github.com/tldr-pages/tldr>
