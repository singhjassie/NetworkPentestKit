# networkspoofer
Spoof a device connected to your local network
This tool will help you to do a man-in-the-middle attack.

# Spoofing

Spoofing means to get into middle of a victim's device and access point.
This way all the traffic from and to the victim's device will flow through your device. Then you can [sniff](http://github.com:singhjassie/networksniffer) the traffic and do further attacks like [packet-injection]() and [dns-spoofing](http://github.com:singhjassie/dnsspoofer). This ways you can take full controll over victims device. 

# Installation
1. Clone the package using git. You can also download zip file from github repository and then extract it.
```sh
git clone http://github.com:singhjassie/networkspoofer
```
2. Nevigate into the directory
```
cd networkspoofer
```
3. Installing the requirements using pip
```
pip install -r requirements.txt
```
4. Make script executable to easily run script
```
chmod +x networkspoofer
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
```
./networkspoofer --help
```
```sh
Options:
  -h, --help            show this help message and exit
  -g GATEWAY_IP, --gateway_ip=GATEWAY_IP
                        add gateway ip
  -v VICTIM_IP, --victim_ip=VICTIM_IP
                        add victim ip
```


# Adding script to linux environment
Everytime you need to run the script you have to navigate to the networkspoofer directory and then type ./networkspoofer to run this command. This may be very overwhelming when you are in hurry. 
<br>
To avoid the problem, you may do so,
```
cp networkspoofer /usr/bin/networkspoofer
```
Now you can run the script from anywhere in terminal without "./" as below,
```
networkspoofer [options]
```
Now you can spoof any device on your network. To sniff their communication  you can use [this tool](http://github.com:singhjassie/networksniffer).
<br>To get more security tools click [here](https://github.com/singhjassie?tab=repositories)
