from Question import Question

question_prompt= [
"If an Ethernet port on a router were assigned an IP address of 21.121.54.71/15, which host address would be able to communicate with it? \n (a) 166.121.177.233 \n (b) 95.199.103.46 \n (c) 21.121.241.69 \n (d) 244.28.220.100 \n (e) 198.58.153.142 \n (f) 79.46.141.190 \n (g) 167.232.175.162\n\n",
"Which of the following services use UDP? 1. DHCP  2. SMTP  3. FTP  4. HTTP \n (a) 3 \n (b) 1 \n (c) All of the above \n (d) 2 \n\n"
]

questions = [
	Question(question_prompt[0], "c"),
	Question(question_prompt[1], "b")
]

def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question.prompt)
		if answer == question.answer:
			score += 1
	print ("You got " + str(score) + "/" + str(len(questions)) + "Correct")

run_test(questions)

