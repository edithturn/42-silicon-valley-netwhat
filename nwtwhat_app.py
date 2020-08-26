from Question import Question
import time
from colorama import init
from timeit import default_timer as timer
init()

question_prompt= [
"01. If an Ethernet port on a router were assigned an IP address of 21.121.54.71/15, which host address would be able to communicate with it? \n\n (a) 166.121.177.233 \n (b) 95.199.103.46 \n (c) 21.121.241.69 \n (d) 244.28.220.100 \n (e) 198.58.153.142 \n (f) 79.46.141.190 \n (g) 167.232.175.162\n\n",
"02. Which of the following services use UDP? 1. DHCP  2. SMTP  3. FTP  4. HTTP \n\n (a) 3 \n (b) 1 \n (c) All of the above \n (d) 2 \n\n",
"03. Which of the following is the valid host range for the subnet on which the IP address 120.2.67.128/15 resides \n\n (a) 120.2.0.1-120.3.255.251 \n (b) 120.2.0.1-120.3.255.254 \n (c) 120.2.0.1-120.3.255.253 \n (d) 120.2.0.1-120.4.0.3\n\n",
"04. DHCP is used for \n\n (a) Both IPV6 and IPV4 \n (b) None of the mentioned \n (c) IPv4 \n (d) IPv6 \n\n",
"05. How long is an IPv4 address?  \n\n (a) 64 bits \n (b) 128 bits \n (c) 128 bytes \n (d) 32 bits \n\n",
"06. What is the Network address of a host with an IP address of 250.160.111.191/18?  \n\n (a) 250.160.64.0 \n (b) 250.160.0.0 \n (c) 250.160.111.176 \n (d) 224.0.0.0 \n (e) 250.160.108.0 \n (f) 250.160.111.128 \n\n",
"07. What is the maximun number of IP addresses that can be assigned to host on a local subnet that uses the 255.240.0.0 subnet mask? \n\n (a) 1048576  \n (b) 524284  \n (c) 2097154 \n (d) 1048574 \n (e) 2097150 \n (f) 52488 \n\n",
"08. Which of this is not true? \n\n (a) UDP supports Broadcasting \n (b) There is no sequencing of data in UDP. If ordering is requiered, it has to be managed by the application layer \n (c) UDP is a datagram-oriented protocol \n (d) The delivery of data to the destination cannot be guaranteed in UDP\n (e) UDP has only the basic error checking mechanism using checksums \n (f) UDP is comparatively slower than TCP \n\n",
"09. Which protocol does  DHCP use at the Transport layer? \n\n (a) IP \n (b) ARP \n (c) UDP \n (d) TCP \n\n" ,
"10. You have an interface on a router with the IP address of 248.137.150.138/25. Including the router interface, how many hosts can have IP addresses on the LAN attached to the router interface? \n\n (a) 64 \n (b) 126 \n (c) 250 \n (d) 62 \n (e) 256 \n (f) 252 \n (g) 254 \n\n",
"11. What are the different layers of the OSI model? \n\n (a) Application -> Presentation -> Session -> Transport -> Network -> Data Link -> Physical \n (b) Application -> Mediation -> Session -> Transport -> Network -> Data Link -> Physical \n (c) Presentation -> Session -> Transport -> Network -> Data Link -> Application -> Real \n (d) Relation -> Transport -> Session -> Data Link -> Mediation -> Presentation -> Application \n\n",
"12. What is the maximun number of IP addresses that can be assigned to host on a local subnet that uses the 255.255.255.248 subnet mask? \n\n (a) 0 \n (b) -2 \n (c) 10 \n (d) 2 \n (e) 6 \n (f) 4 \n\n",
"13. Which of this is not a class of IP address?  \n\n (a) Class D \n (b) Class C  \n (c) Class E  \n (d) Class F \n\n" ,
"14. Which of the following is private IP address? \n\n (a) 18.187.149.135 \n (b) 192.168.108.121 \n (c) 81.0.182.194 \n (d) 130.41.89.219 \n\n",
"15. Which class of IP address has the most host addresses available by default? \n\n (a) B  \n (b) C \n (c) A and B \n (d) A \n\n",
"16. The_____________translates internet domain and host names to IP adddress.  \n\n (a) Internet Relay Chat \n (b) Network Time Protocol \n (c) Routing Information Protocol \n (d) Domain Name System \n\n",
"17. Which of this is not true? \n\n (a) TC is reliable as it guarantees delivery of data to the destination router. \n\n (b) TCP provides extensive error checking mechanisms. It is because it provides flow control and acknowledgment of data.\n (c) TCP is comparatively slower than UDP\n (d) TCP doesn't supports Broadcasting  \n (e) There is not sequencing of data in TCP. If ordering is requiered, it has to be managed by the application layer. \n (f) TCP is a connection-oriented protocol.\n\n",
"18. You want to implement a mechanism that automates the IP configuration, including IP address, subnet mask, default gateway, and DNS information. Which protocol will you see to accomplish this? \n\n (a) DHCP  \n (b) ARP \n (c) SNMP \n (d) SMTP \n\n",
"19. Which protocol does Ping use? \n\n (a) TCP \n (b) BootP \n (c) ARP \n (d) ICMP \n\n",
"20. How long is an IPv6 address? \n\n (a) 64 bits \n (b) 128 bytes \n (c) 32 bits \n (d) 128 bits \n\n"
]

questions = [
	Question(question_prompt[0], "c"),
	Question(question_prompt[1], "b"),
	Question(question_prompt[2], "b"),
	Question(question_prompt[3], "a"),
	Question(question_prompt[4], "d"),
	Question(question_prompt[5], "a"),
	Question(question_prompt[6], "d"),
	Question(question_prompt[7], "f"),
	Question(question_prompt[8], "c"),
	Question(question_prompt[9], "b"),
	Question(question_prompt[10], "a"),
	Question(question_prompt[11], "e"),
	Question(question_prompt[12], "d"),
	Question(question_prompt[13], "b"),
	Question(question_prompt[14], "d"),
	Question(question_prompt[15], "d"),
	Question(question_prompt[16], "e"),
	Question(question_prompt[17], "a"),
	Question(question_prompt[18], "d"),
	Question(question_prompt[19], "d")
]

def run_test(questions):
	score = 0
	from colorama import Fore, Back, Style
	start_time = time.time()
	print (Fore.GREEN  + "\n********************************************* Netwhat - 42 Silicon Valley *********************************************\n")
	for question in questions:
		print(Style.RESET_ALL)
		print (question.prompt)
		answer = input("Your Answer: ")
		if answer == question.answer:
			print (Fore.GREEN + " [ OK ] \n")
			score += 1
		else:
			print (Fore.RED + "[ KO ] \n")
	print (Fore.GREEN + "You got " + str(score) + "/" + str(len(questions)) + " Correct")
	e = int(time.time() - start_time)
	print(Fore.GREEN  + 'Time taken: {:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))
	print ("\n")
run_test(questions)

