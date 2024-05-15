# networkscanner
Scan a local network to know the IP Address and MAC Address of in the network

# Installation
1. Clone the package using git. You can also download zip file from github repository and then extract it.
```sh
git clone http://github.com:singhjassie/networkscanner
```
2. Nevigate into the directory
```
cd networkscanner
```
3. Installing the requirements using pip
```
pip install -r requirements.txt
```
4. Make script executable to easily run script
```
chmod +x networkscanner
```
> **Note**
>
>You first have to switch to super user before running the script.
# Usage
Enter the following command to see usage help
```
./networkscanner --help
```
```sh
Usage: networkscanner.py [options]

Options:
  -h, --help            show this help message and exit
  -r IPRANGE, --iprange=IPRANGE
                        add ip addresses range you want to scan
```
You have pass iprange of your network. To know your IP Address type the following command,
```
ifconfig
```
Check inet (Local IP Address) and subnet. According to your subnet pass your IP Address range of your network. To know more about IP Address range of network or CIDR notation [click here](https://community.spiceworks.com/networking/articles/2495-what-is-cidr-notation).
<br>For example, In my case my local IP Address is 192.168.16.12 and subnet mask 255.255.255.0. I will pass iprange as below,
```
./networkscanner -r 192.168.16.12/24
```

# Adding script to linux environment
Everytime you need to run the script you have to navigate to the networkscanner directory and then type ./networkscanner to run this command. This may be very overwhelming when you are in hurry. 
<br>
To avoid the problem, you may do so,
```
cp networkscanner /usr/bin/networkscanner
```
Now you can run the script from anywhere in terminal without "./" as below,
```
networkscanner [options]
```
Now you have IP Addresses and MAC Address of all the devices connected to your local network. This information can be used to spoof any device on your network. To spoof someone on your wireless network you can use [this tool](http://github.com:singhjassie/networkspoofer).
<br>To get more security tools click [here](https://github.com/singhjassie?tab=repositories)