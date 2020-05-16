**Which of the following services use UDP?**

1. DHCP  
2. SMTP
3. FTP
4. HTTP
5. All of the above

|||
|--------------|----------------|
| **UDP:** | (User Datagram Protocol) is a communication protocol that is primarily used for establishing low-latency and loss-tolerating connections between application on the internet. |
| **DHCP:** |  The DHCP (Dynamc Host  Confguration Protocol) is a network management protocol used to automate the process of configuring devices on IP network. Employs a connectionless services model, using the User Datagram Protocol  (UDP). it is implemented with two UDP port numbers for its operations which are the same as the BOOTP protocol. UDP port number 67 is the destination port of a server, and UDP port number 68 is used by the client. | 
|  **SMTP:** |  (Simple Mail Transfer Protocol), is a mail transport protocol, and in mail every single packagt is important. If you lose some package in the transmision of the message the recipient might not even receive the message and they might be missing key information. TCP is more appropieate in this case because ensures that every package is delivered. | 
|  **FTP:** |  (File Transfer Protocol)  Is a way to transfer file online (between a client and server on a computer network), uses the TCP protocol because the file transfer has to be correct. | 
|  **HTTP:** |  (Hipertext Transfer Protocol) is a protocol used by the World Wide Web, and this protocol defines how messages are formated and transmitted, and what actions Web servers and browsers should take in response to several commands. Uses TCP instead of UDP because it guarantees delivery via a three-way handshake and re-transmission of lost packets. | 


:pencil2: **Answer:**
**DHCP use UDP**