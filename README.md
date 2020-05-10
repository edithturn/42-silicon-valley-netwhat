# Netwhat
This project is an introduction to network problematics

Netwhat will allow you to discover the network and to learn about its inner workings.
This will allow you to understand how some things work that you already use in your
everyday life.


## Basic Concepts

### What is an IP address 
It is a network address for our computers and the internet knows where to send informations and data.
<network><host>

### What is a Netmask
A Netmask is a 32-bit "mask" used to divide an IP address into subnets and specify the network's available hosts.


### What is the subnet of an IP with Netmask
<network><subnet><host>


### What is the broadcast address of a subnet
Highest IP address in a subnet or network, used as the destination IP address for broadcast messages.

How to find broadcast address:

Class A

10.20.11.5
255.0.0.0
---------
10.255.255.255  <= Broadcast Address

**Class B**

172.16.20.20
255.255.255.0
--------------
172.16.20.255

**Class C**
 
192.168.2.33
255.255.255.246
---------------
192.168.2.**39**

Aditional steps:

* First step: subtrac octect from 256 (this is called our multiplier)
256-
246
----
  8

* Second step: How many multiples of this number do we need to come up with in order to get just greater than 33 but as close to it as possible:

8  + 8
16 + 8
24 + 8
32 + 8
40 - 1 = 39


Another example:

172.16.20.10
255.255.240.0
--------------
172.16.**31**.255

* First step: 
256 - 
240
-----
16

16 + 16
32 - 1

**remember 2 ruler**

- 255 in the subnet mast = write dorn IP address octet value
- 0 in the subnet mask = write down 255
- If the subnet mask has an octet whose value doesn't equal to 255 or 0:
use the formula: 256 - octet = multiplier.
  Find number greater than IP address octet  but close to it as possible, then subtract 1.



### What are the different ways to represent an ip address with the Netmask

**Netmask**
Is a 32-bit "mask" used to divide an IP address into subnets and specify the network's available hosts.

255.255.255.0 is applied to the 129.144.41.101 , the result is the IPv4 address of 129.144.41.0 .

129.144.41.101 & 255.255.255.0 = 129.144.41.0

In binary form, the operation is:

10000001.10010000.00101001.01100101 (IPv4 address)

AND

11111111.11111111.11111111.00000000 (netmask)



### What are the differences between public and private IPs

public Ip  can to be static or dynamic.
 - A static address is unchanged and is often for hosting websites, server.
 - A dynamic address are chasen from a "pool" of available addresses and will be changed each time user connects.



### What is a class of IP addresses 

IP address in class A, class B and class C.

Class	  Starting IP address	 Ending Ip Address   # of hots
A 	| 10.0.0.0		| 10.255.255.255   | 16,777,216
B 	| 172.16.0.0		| 172.31.255.255   | 1,048,576
C 	| 192.168.0.0		| 192.168.255.255  | 65,536

### What is TCP

TCP (Transmision Control Protocol)
Main protocols of the internet protol suite.

- Keeps track of lost packages, makes sure that lost packages are re-sent
- Addes sequesce numbers to packets and reorders any packets that arrive in thenworng order.
- Slower, because of all added additional functionality.
- Requieres more computer resources, because the OS needs to keep track of ongoing communication sessions and manage them on a much deeper level.

### What is UDP

- Doesn't keep track of lost packages
- Doesn't care about package arrival order.
- Faster, bacause it lacks any extra features.
- Requieres less computer resources.
- Examples of programs and services that use UPD:
	- DNS
	- IP telephony
	- DHCP
	- Many computer games

- Why we use UDP?

Many applications that requiere real-time communication prefer to use UDP, applications that requiere speed and that torerat partial data loss.

### What are the network layers

In the seven-layer OSI model of computer network, the network layer is layer 3. The network layer is responsible for packet forwarding including routing through intermediate routers.


### What is the OSI model

The Open System Interconnection (OSI). It has been developed by ISO - 'International Organization of Standardization'. It is a 7 layer architecture with each layer having specific functionality to perform. All tese 7 layers work collaboratively to transmit the data fr4om one person to another across the globe.

- Application Layer	| software layer
- Presentatation layer	| software layer
- Session Layer		| software layer
- Transport Layer	| Heart of OSI
- Network Layer		| hardware Layer
- Data Link Layer	| hardware Layer
- Physical layer	| hardware Layer


### What is a DHCP server and the DHCP protocol
 - DHCP server: DHCP (Dynamic Host Confivguration Protocol), is a protocol that provides quick, automatic, and central management for the distribution of IP addresses within a network. DHCP is also used to configure  the subnet mask, default gateway and DNS server information on the device.

### What is a DNS server and the DNS protocol

Domain Name System (DNS) is the phonebook of internet. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load internet resources.

The **Domain Network System (DNS) protocol** helps internet users and network devises discover websites using human-readable hostnames, instead of  numeric IP addresses.

### What are the rules to make 2 devices communicate using IP addresses



### How does routing work with IP?

- Routing is the process by which data packets move from one node (machine or device) to another on a computer network until the packets reach the final destination.

The header information includes:
- The IP addresses of the source and destination nodes.
- Packet numbers that help reassemble the packets in the correct order whe  the packets reach the destination. 
- other useful technical information.

** How routing works **


### What is a default gateway for routing
 It allows devices within one network to send information to devises within another network. If you are requestiong a certain web page, the trafic is first sent to your default gateay before leaving the local network to reach its indended destination.

### What is a port from an IP point of view and what is it used for when connecting
to another device




Resources:

How to find a Broadcast Address:
https://www.youtube.com/watch?v=1pZNjRZLNqI

https://www.youtube.com/watch?v=cNwEVYkx2Kk&list=PLDQaRcbiSnqF5U8ffMgZzS7fq1rHUI3Q8

http://jodies.de/ipcalc?host=148.12.181.53&mask1=20&mask2=


https://www.cloudflare.com/learning/dns/what-is-dns/


###  Technical Terms


|Technical Terms | Definition |
| ------------- | -------------------------- |
| subnet mask  	| A subnet mask is a number that defines a range of IP addresses available within a network. 			 |



