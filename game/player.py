from Client0 import Client

IP = "127.0.0.1"
PORT = 12345

c = Client(IP, PORT)
print(c)


guessing = True
while guessing:
    guess = input("Enter your guess (between 1 and 100)")
    response = c.talk(gu41ess)
    print(response)

    if ("You won") in response:
        guessing = False