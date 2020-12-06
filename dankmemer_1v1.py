import random
GameEnd = "False"
searchstuff = ["Discord", "the airport", "your house", "this guy's pocket", "your poor dog"]
begpeople = ["Billie Eilish:", "Post Malone:", "Bob the Builder:", "MrBeast:", "That founder of 4chan you've always wanted to confront:"]
quotes = ["get off my lawn", "coins for you now go away my eyes are bleeding", ":P", "bruh stop asking for coins", "yip yap yip"]

player1money = 0
player2money = 0

id1 = input("DANK MEMER \ntype in player1's pseudo")
print ("Welcome to the parTAY,", id1)
id2 = input("type in player2's pseudo")
print ("Welcome,", id2, ".", "We hope you've brought pizza.")

print("At any time, type in 'pls help' for available commands and help.")

while GameEnd == "False":
    thing = input("Player 1's turn")
    if thing == "pls search":
        print("You searched", random.choice(searchstuff), "and you now have")
        player1money = player1money + random.randint(0, 500)
        print(player1money, "coins.")
    if thing == "pls beg":
        print(random.choice(begpeople), random.choice(quotes))
        player1money = player1money + random.randint(0, 450)
        print("you now have", player1money, "coins.")
    if thing == "pls rob" and player1money > 500:
        randomnumber = random.randint(1, 201)
        if randomnumber in range(1,101):
            print("You got caught TROLLOLOL \nyou pay", id2, "500 dollars.")
            player1money = player1money - 500
            player2money = player2money + 500
            print("you now have", player1money, "coins.")           
        elif randomnumber in range(101,201):
            print("NOICE you robbed some loot")
            rob = random.randint(1, player2money)
            player1money = player1money + rob
            player2money = player2money - rob
        else:
            print("Some weird bug happened, so now", id2, "must forfeit their next turn")
    if thing == "pls rob" and player1money < 500:
        print("Bro you need to have 500 dollars to rob, now", id2, "must forfeit their next turn")

    print("MONEY CHECK BRUHS!")
    print("Currently,", id1, "has", player1money, "dollars.")
    if player1money > 5000:
        print("So,", id1, "wins!")
        GameEnd == "True"
        
            
    


    thing = input("Player 2's turn")
    if thing == "pls search":
        print("You searched", random.choice(searchstuff), "and you now have")
        player2money = player2money + random.randint(0, 500)
        print(player2money, "coins.")
    if thing == "pls beg":
        print(random.choice(begpeople), random.choice(quotes))
        player2money = player2money + random.randint(0, 450)
        print("you now have", player2money, "coins.")
    if thing == "pls rob" and player2money > 500:
        randomnumber = random.randint(1, 201)
        if randomnumber in range(1,101):
            print("You got caught TROLLOLOL \nyou pay", id1, "500 dollars.")
            player1money = player1money + 500
            player2money = player2money - 500
            print("you now have", player2money, "coins.")           
        elif randomnumber in range(101,201):
            print("NOICE you robbed some loot")
            rob = random.randint(1, player1money)
            player1money = player1money - rob
            player2money = player2money + rob
        else:
            print("Some weird bug happened, so now", id1, "must forfeit their next turn")
    if thing == "pls rob" and player2money < 500:
        print("Bro you need to have 500 dollars to rob, now", id1, "must forfeit their next turn")

    print("MONEY CHECK BRUHS!")
    print("Currently,", id2, "has", player2money, "dollars.")
    if player2money > 5000:
        print("So,", id2, "wins!")
        GameEnd == "True"
        
        
        


