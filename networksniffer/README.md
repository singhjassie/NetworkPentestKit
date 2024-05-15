# Networksniffer

Sniff HTTP traffic of spoofed device to get links of visited websites and extract username and passwords.

You have to first spoof the victim's device before using this tool. To do so you can use [this tool](http://github.com:singhjassie/networkspoofer).

# Installation
1. Clone the package using git. You can also download zip file from github repository and then extract it.
```sh
git clone http://github.com:singhjassie/networksniffer

```
2. Nevigate into the directory
```
cd networksniffer

```
3. Installing the requirements using pip
```
pip install -r requirements.txt
```
4. Make script executable to easily run script
```
chmod +x networksniffer

```
> **Note**
>
>You first have to switch to super user before running the script.


# Usage
To forward the incoming traffic from victim's device you need to run this command.

```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Enter the following command to see usage help

```sh
./networksniffer --help
```
```
Usage: networksniffer
.py [options]

Options:
  -h, --help            show this help message and exit
  -r IPRANGE, --iprange=IPRANGE
                        add ip addresses range you want to scan
```

# Adding script to linux environment
Everytime you need to run the script you have to navigate to the networksniffer
 directory and then type ./networksniffer
 to run this command. This may be very overwhelming when you are in hurry. 
<br>
To avoid the problem, you may do so,
```
cp networksniffer
 /usr/bin/networksniffer

```
Now you can run the script from anywhere in terminal without "./" as below,
```
networksniffer
 [options]
```



Now you can sniff the traffic of victim's device and extract the useful information for further attacks like [dns-spoofing](http://github.com:singhjassie/dnsspoofer) and [packet-injection]().
<br>To get more security tools click [here](https://github.com/singhjassie?tab=repositories)