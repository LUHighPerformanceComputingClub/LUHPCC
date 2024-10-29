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
  3. Power on each of the Raspberry Pi's

## Getting Started
Ok now you have one of the pis on, what now? Now you need to update your systems using these basic commands:
<pre>
<code>sudo apt update</code>
<code>sudo apt upgrade</code>
</pre>
Next, you will want to intall MPICH, which allows the Pis to split tasks among multiple pis
<pre>
<code>sudo apt install mpich python3-mpi4py</code>
</pre>
Here are a couple more installs, and what they do
<pre><code>sudo apt install python3-pip python-dev libopenmpi-dev</code></pre>
> Installs python and other resources needed to run tasks in parrellel
<pre><code>sudo apt install dnsmasq</pre></code>
>Installs lightweight version of DNS and DHCP, which allows you to assign IP addresses to each node







## Getting IP addresses
Alright, the modules have been downloaded, and now we need to setup and work with MPI. 
First, pick a pi to be the master pi. Then, get the IP of each of the raspberry pi's. You can do so using <code>ifconfig</code>
<pre>
<code>ifconfig</code>
</pre>
Here is an example of what it should look like, the IP address is on line 2 after the "inet" keyword:
<img>https://raspberrytips.com/wp-content/uploads/2018/08/ifconfig.png</img>

Now, write down/remeber the IP of each of the Pi's, you will need them for later.
You may want to save the IP's into a file, here is what that would like
<pre>
<code>nano ip_addrs</code>
</pre>
In the file, write down the IP's on a seperate line
Example:
<pre>
192.168.1.01
192.168.1.02
192.168.1.03
192.168.1.04
etc...
</pre>


## Setting Up DHCP
To set up a DHCP server, make sure you are on the <b>master node</b>
First, you need to edit your dhcp.conf file using this command:
<pre><code>sudo nano /etc/dhcpcd.conf</code></pre>

At the bottom of the file, enter this to add your dhcp server
<pre>
<code>
interface eth0
static ip_addresses=192.168.3.2/24
static routers=192.168.3.1
static domain_name_servers = 192.168.3.2
</code>
</pre>

<!--
Next, change your directory to your home folder, then create and edit a file
<pre>
<code>cd /home/pi</code>
</pre>
<pre>
<code>nano ip_addrs</code>
</pre>
In this file, you will want to add the IP of each node on a seperate line
Example:
<pre>
192.168.1.01
192.168.1.02
192.168.1.03
192.168.1.04
etc...
</pre>
-->
## Fun with SSH
From your master node you will want to create and copy your SSH key to each node
<pre><code>ssh-keygen</code>
</pre>
For each of the pi's
<pre>
<code>ssh-copy-id -i .ssh/id_rsa.pub pi@PI_IP</code>
<code>ssh pi@<b>NODE_IP</b></code>
</pre>
>The pi# stands for the host name of the pi

<!--
<pre><code>sudo raspi-config</code>
Go in system options -> Host name
Set a new hostname for this node
Then, exit the node using <code>exit</code>
</pre>
-->
<!--
<pre><code>sudo raspi-config</code>
Go in system options -> Host name
Set a new hostname for this node -> Node1
Then, exit the node using <code>exit</code>
</pre>
-->


On the master node, you will want to create a SSH key using this command
<pre><code>ssh-keygen</code></pre>
Using this command, you will transfer the public key to each of the nodes.
<pre><code>ssh-copy-id -i .ssh/id_rsa.pub pi#@PI_IP</code></pre>

Now, try to ssh without a password to each node!
<pre><code>ssh pi@<b>NODE_IP</b></code></pre>
</pre>



## Running MPI and specefics with it
Alright, to test that MPI is working, lets run a simple command on the master node
<pre><code> nano Hello.py</code></pre>
In the file, enter:
<pre><code>print("Hello World!")</code></pre>
Ctrl + x, then y, then copy the file to each node

<pre><code>scp Hello.py pi@NODE_IP </pre></code>
>**^COPY TO EACH PI IP ADDRESS**

Now, all you need to do is enter this command:
<pre><code>mpirun python3 Hello.py</code></pre>
 
 Thats it! Mpi is now working, we will dive further into Mpi a little later
  
