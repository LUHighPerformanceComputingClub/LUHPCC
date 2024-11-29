# Raid configuration
### Written by Connor Anderson
This guide will go over how to set up RAID on a Linux system.


## Prerequisites
- You will need at least two hard drives to set up RAID properly. If you wish to set up RAID 6 you will need at least four.

## Let's started
First we have to partition the disks, but remember to update your system and back-up any important data before you start this.
<pre>
  <code>sudo apt update</code>
  <code>sudo apt upgrade</code>
  <code>cat /proc/partitions</code>
</pre>




## Partition the Disks
We will now use fdisk to partition. (Replace /dev/sda with whatever name your hard drives have.)
<pre>
  <code>sudo fdisk /dev/sda</code>
</pre>
 >Now press "n" to create a new partition and "w" to write out the changes.


## Creating the Raid array
We are using mdadm tool to create the array.
<pre>
  <code>sudo mdadm --create /dev/md0 -a yes -l 5 -n 4 /dev/sda1 /dev/sda2 /dev/sda3 /dev/sda4</code>
</pre>
>"/dev/md0" is the new name of the raid array, "-a yes" auttomatically starts the array after creation. "-l 5" is the raid configuriation. "-n 4" is the number of drives in the array, followed by the partition location.


## Creating the filesystem and mounting
Next we have to create a filesystem to use the raid array, we will be using the ext4 filesystem.
<pre>
  <code>sudo mkfs.ext4 /dev/md0</code>
</pre>
Finally we have to mount the raid array.
<pre>
  <code>mount /dev/md0 /mnt</code>
</pre>


And that's it, you now should have a working raid configuration running raid 5.
