¿Which of the following is the valid host range for the subnet on which the IP address 120.2.67.128/15 resides?


## what you should know before:
Find the number of subnets and the number of valid host per Subnet

- Subnet
	2 ^ # of subnets bits

- Valid Host
	(2 ^ # of hosts bits) - 2 
	
* (-2) at the end is because we have the network number we don't assign and we have the broadcast address which does not get assigned to one single host.

* The valid host do mean the IP addresses in a subnet that we can actually allocate to endpoints like a computer or a router.


* **Example:**
```bash
19.168.1.0
255.255.255.240(/28)

11111111.11111111.11111111.11110000

is this Class A, B, or C network?

- The firts octect 192 falls within the Class C Network range.
- Network has a default subnet mask of 255.255.255.0 which means the first three octects are dedicated to the network portion, this never  changes.

# The remaining ones in the subnet mask have to be our subnet bits.
Subnet = 2^4 = 16 # by using this subnet mask we can create 16 subnets.

# Lets touch the number of host bits
Hosts = (2^4 ) - 2 = 14
```
**Interpretation
We can create 16 different subnets and each subnet is going to have 14 valid hosts

**Subnet Mask Formats**

```bash
Cider			/10
Decimal		255.192.0.0
Binary		1     1       1       1      1     1    1     1   .   1        1     0    0    0    0    0    0 ...
			(128)  (64)  (32)  (16)  (8)  (4)  (2)  (1)    (128)   (64)
```

## answering the question
**¿Which of the following is the valid host range for the subnet on which the IP address 120.2.67.128/15 resides?**


![alt text](first_valid_host.png)

![alt text](last_valid_host.png)


### The answerd is :  [ 120.2.0.1 - 120.3.255.254 ]



Reference: https://www.youtube.com/watch?v=uyRtYUg6bnw

calculator: http://www.aboutmyip.com/AboutMyXApp/SubnetCalculator.jsp?ipAddress=120.2.67.128&cidr=15