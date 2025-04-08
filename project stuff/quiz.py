import hashlib

def hash_answer(answer: str) -> str:
    return hashlib.sha256(answer.strip().lower().encode()).hexdigest()

questions = [
    "When is the full release date of Drift? (format should be Month date, year e.g Jan 1, 2000)",
    "What is the name of the upcoming game (this is the game we are trying to steal)?",
    "What is the first name of the CEO of Rito Games?",
    "From the nmap scan what is the IP of the webserver hosting ritogames.com? (xxx.xxx.xxx.xxx)",
    "What is the version of the Apache Tomcat Server? (x.x.xxx)",
    "What HTTP Method was used to upload the script onto the server?",
    "What is the name of the exploit that was uploaded onto the webserver (include the extension)?",
    "What is the complete path of the file that includes communication details between two company employees?",
    "What is the IP address of the Design Server? (xxx.xxx.xxx.xxx)",
    "What is the hashing algorithm used in the /etc/shadow file?",
    "What is the account that you used to grant access to client 192.168.100.101? (Format:<Account_Name> <Password>)",
    "What is the full directory of where checkpoint2 is located?",
    "One of the car designs spells a 4 letter word. What does it say?",
    "What is the new IP address found from the arp -a command?",
    "From the Banner, what is the name of the server we just authenticated on?",
    "What is the new IP address found from the arp -a command?",
    "What is the color of the car in the game?"
]

answers = [
"01c57a255b0f41e81e890b63fc0793c8b478a06bb4927764c84e503024abad28",
"0b7a461fefbb68e518e51884369a4b88baffdb40b7e578921f3f88649ebc6494",
"64b4d0f47c93ce23d157e68a58767356283dc9b63c459d45d0e0e39b3a64b9b9",
"0ec0dc38ff3da5f4072580085056549bdcf7a777389c5beaed8aef2033f4c0ab",
"fae902be9ff932bdc39bce076f4d8d14c622173fdb848182b7903246fee74d73",
"373cb2c6d4fe2778441d4f0266505b699fa518d002e5793b87f9b48836de3f62",
"ed444abc2d8b6519af7a42e1b3d7b1a01eedb786a7032a449b65130fa377cad3",
"c2f24bf143beab2d463964bb848d626e1131d7606d6db2bb56c2e5da169d97fb",
"0ec0dc38ff3da5f4072580085056549bdcf7a777389c5beaed8aef2033f4c0ab",
"0400c7995fa7e98bf2edeba4c50692e1aa5d386f1dbb7874ec897142d49ce088",
"bbfca6ba8035540bb942342ccd379f2444c0580fc2153a23c6a65b0f50e34327",
"be5c762966811a9d54c0a78bc52ea4ad67eb814d1f254f9848663388817d8ca7",
"4e64ce3d8c7f9b04d738bf54f80b3e5cfac0bfe5e5befbad8d760af28310bff7",
"fea7d9339f28b709d37ebd376622fe942dbe4c2120d6ef8be60d41cae6255b87",
"8c85b6639e62e10b8330a8b883004b43c119053d7d62b512a98c77eb069627a7",
"9f10b28c378c663384a8a41fda096bbb0f50701b1d74ad006d9de43beee3b64f",
"16477688c0e00699c6cfa4497a3612d7e83c532062b64b250fed8908128ed548",
]

def check_quiz():
    for i in range(len(questions)):
        while True:
            print(f"Question {i + 1}: {questions[i]}")
            user_answer = input("Your answer: ")

            if hash_answer(user_answer) == answers[i]:
                print("Correct!\n")
                break
            else:
                print("Incorrect. Please try again.\n")

    print("Congratulations! You answered all questions correctly!")


check_quiz()

    #
    # print(hash_answer("/home/Jat/data_separation_request.txt"))