# Basic-Port-Scanner
Simple port scanner made in python

How to use: 

```
python3 scanner.py <ip>
```
The code checks for invalid IPs (less than 4 octets, wrong range in octets).

Also it has implemented exceptions such as a keyboard interrupt (e.g. ^C is pressed), gai error(host couldn't be resolved) or socket error (couldn't connect to the server).

There are still improvements to add, such as the time flag (-Tx, x being how fast I want the port scanner to be)
