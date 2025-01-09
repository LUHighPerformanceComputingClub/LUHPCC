# Pi clusters
#### Written By Ben Peterson
This guide will go over how to cluster multiple raspberry pi's together, and how to run python scripts off the pi cluster


 ## Prerequisites
   - More than one raspberry pi
   - Each raspberry pi must be plugged into an ethernet switch
   - Power/ethernet cables for each pi
   - Internet access to download updates and module
   - A micro SD card with Raspbian for each pi
## Raspbian Installation
  1. Plug each micro SD card into your pc, then <a href="https://www.raspberrypi.com/software/"> Download Raspian</a>
  2. Plug in the micro SD card, ethernet, and power to each pi
  3. Power on each of the Raspberry Pis
  4. Enable ssh on each of the pis

## Getting Started
Before we get started, we will need to connect the pis to the internet. Using the wireless connectivity options of the pis or an ethernet hub, connect the pis to the internet at this time. This can be done by simply plugging in the ethernet, or selecting an available Wi-Fi network. Note that Pis like to be finiky when there is no display output for the pi when it is turned on, so it is reccomended that each pi temporarily gets plugged in to a display when it gets powered on. 


Ok now you have all of the pis on and connected to the internet, what now? Now you need to update your systems using these basic commands. Run this on **EACH** of the pis in the cluster:
<pre>
<code>sudo apt update</code>
<code>sudo apt upgrade</code>
</pre>
Next, you will want to intall MPICH, which allows the Pis to split tasks among multiple pis. Run this on **EACH** of the pis
<pre>
<code>sudo apt install mpich python3-mpi4py</code>
</pre>
Finally install another python library for mpi. Run this on **EACH** of the pis.
<pre><code>sudo apt install python3-pip python-dev libopenmpi-dev</code></pre>
> Installs python and other resources needed to run tasks in parrellel



## Setting IP addresses
Now that everything is installed, lets get working on setting IP addresses manually.

Using the command <code>nmtui</code>, click edit a connection, then select the wired ethernet connection. 

Next, go down to the IPv4 Configuration section, and change the IP to a manual address by selecting automatic, then manual. 

Finally, in the IPv4 Configuration section down to where it says addresses, and type in the desired address. Go to the bottom and select ok.

**After exiting nmtui, run the commands <code> sudo ifconfig eth0 down</code>, then <code>sudo ifconfig eth0 up</code>**


## Getting IP addresses and usernames
For each pi, an IP address will need to be configured using the above method. Because of network segments, the IP addresses will need to be on the same network segments in order for this guide to work (If you dont know what that means look at the example file below).
You can use the <code>ifconfig</code> command to get the IP address of the device.

Here is an example of what it should look like, the IP address is on line 2 after the "inet" keyword:
<img>https://raspberrytips.com/wp-content/uploads/2018/08/ifconfig.png</img>



Now, write down/remeber the IP of each of the Pi's, you will need them for later.
Save this to a file called **ip_addrs** on the master node.
<pre>
<code>touch ip_addrs</code>
</pre>
In the file, write down the IP's on a **separate** line

Additionally, you will want to write down the users for which MPI will be used for. This is **very** important. Use the <code>whoami</code> command to get the username of the user. **DO NOT USE ROOT, MPI WILL NOT WORK AS ROOT**
<br>This is the syntax for which you will write down the usernames and IP addresses:
<pre><code>user@IPAddress</code></pre>
Here is an example of what the file should look like in its final form:
<pre>
pi@192.168.1.1
pi2@192.168.1.2
mpiGuy@192.168.1.3
timmy@192.168.1.4
etc...
</pre>
> Note, by default, MPI will attempt to use the same user across all nodes by default. Adding the user is optional, but allows for different users to be utilized for MPI. 




## Fun with SSH
From your master node you will want to create and copy your SSH key to each node. Follow this process. First, create a ssh key.
<pre><code>ssh-keygen</code>
</pre>
Do this from the master node, and copy the id to each of the pis. User stands for the user that you want to have mpi on. Do this on the master node for **EACH PI**
<pre>
<code>ssh-copy-id user@PI_IP</code>
</pre>
Next, back on the master node, run this command. USER is the user of the master node, and USER2 is the user of the slave node, and IPAddress is the IP address of the slave node:
<pre><code>scp /home/USER/.ssh/id_rsa.pub USER2@IPAddress:/home/USER2/master.pub</code></pre>

Finally, ssh into the user
<pre><code>ssh user@<b>NODE_IP</b></code></pre>
and run these commands:
<pre>
<code>cat master.pub >> .ssh/authorized_keys</code>
<code>rm master.pub</code>
</pre>



## Testing MPI
Alright, to test that MPI is working, lets run a simple command on the master node
<pre><code> nano Hello.py</code></pre>
In the file, enter:
<pre><code>print("Hello World!")</code></pre>
Ctrl + x, then y, then copy the file to **EACH OF THE SLAVE NODES**:

<pre><code>scp Hello.py pi@NODE_IP </pre></code>
>**^COPY TO EACH PI IP ADDRESS**

Now, all you need to do is enter this command:
<pre><code>mpirun --hostfile ip_addrs python3 Hello.py</code></pre>


 Thats it! Mpi is now working, we will dive further into MPI in a later guide.