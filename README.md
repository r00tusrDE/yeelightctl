# yeelightctl

Python script to control your Xiaomi Yeelight bulbs.

### Built With
* [Python](https://www.python.org)
* [python-yeelight](https://github.com/skorokithakis/python-yeelight)

## Prerequisites
* Install Python 3 and Pip
```sh
# Ubuntu / Debian
$ sudo apt install python3 python3-pip

# CentOS / Fedora
$ sudo yum install python36 python3-pip

# Arch
$ sudo pacman -S python python-pip

# openSUSE
$ sudo zypper install python3 python3-pip
```

## Getting started
1. Clone this repo
```sh
$ git clone https://github.com/r00tusrDE/yeelightctl.git
```
2. Install Dependencies
```sh
$ pip install -Ur requirements.txt
```
3. You can set names for your bulbs so you don't need to always type out the ip of the bulb that you want to control. To set names open the bulbs.csv file (contained in this repo) and use one line per bulb. Use the following syntax in the CSV file:
```csv
<bulb_name>,<bulb_ip>
```
Here is a example for a bulb in the living room and one in the bedroom:
```csv
name,ip
lr,192.168.178.10
br,192.168.178.11
```
See `Usage` to know how to use these names.

## Usage
### Basic usage
You can either use the ip or the name of your bulb (See `Getting started` for more information on how to set up names for your bulbs)
```sh
$ python yeelightctl.py <bulb_ip|bulb_name> <function>
```
1. Turn on the bulb
```sh
# using IP
$ python yeelightctl.py 192.168.178.10 on

# using name
$ python yeelightctl.py lr on
```
2. Turn off the bulb
```sh
# using IP
$ python yeelightctl.py 192.168.178.10 off

# using name
$ python yeelightctl.py lr off
```

## License
Distributed under the GPLv3 License. See `LICENSE` for more information.
