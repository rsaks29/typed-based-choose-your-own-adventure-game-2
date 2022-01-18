import time,random
while True:
    a=input("welcome to the choose your own adventure type game #2 type 'ready' when you are ready: ")
    if a=='ready':
        print("the first thing before your epic journey begins you need to create your character.")
        break
while True:
    print("the first thing you need to when creating your character is choose your gender type M for male, F for female,")
    print("NB for non-binary, and O for other: ")
    time.sleep(1)
    a=input()
    if a=='M':
        print("you chose a male character")
        break
    elif a=='F':
        print("you chose a female character")
        break
    elif a=='NB':
        print("you chose a Non-Binary character")
        break
    elif a=='O':
        print("you chose a character with a unspecified gender")
        break
while True:
    time.sleep(1)
    print("after choosing your gender you should probably choose the character class but be careful")
    print("what you choose because you only have 50,000 points to spare")
    r=input("just type 'choose class' when you are ready: ")
    if r=='choose class':
        print("1. hacker 30,000")
        print("2. fighter 10,000")
        print("3. casual person 5,000")
        break
while True:
    points=50000
    # hacker=30,000
    # fighter=10,000
    # casual_person=5,000
    r1=input("type the name of the class or the number to choose the class you want to play as: ")
    if r1=='hacker'or r1=='1':
        print("you chose the hacker class")
        points=points-30000
        print(points)
        break
    elif r1=='fighter' or r1=='2':
        print("you chose the fighter class")
        points=points-10000
        print(points)
        break
    elif r1=='casual person' or r1=='3':
        print("you chose the casual person class")
        points=points-5000
        print(points)
        break
while True:
    print("now that you have chosen your class it is time to choose your abilities")
    print("type 'choose abilities' when you are ready: ")
    r=input()
    if r=='choose abilities':
        print("the abilities for your class are:")
        if r1=='hacker' or r1=='1':
            print("1. cheat sheet 50,000")
            print("2. glitch the servers 20,000")
            print("3. matrix dodge 10,000")
            break
        elif r1=='fighter' or r1=='2':
            print("1. street fighter hadouken 30,000")
            print("2. roundhouse kick 10,000")
            print("3. uppercut 5,000")
            break
        elif r1=='casual person' or r1=='3':
            print("1. Man's best friend 10,000")
            print("2. Fast car 5,000")
            print("3. punch 1,000")
            break
while True:
    print("type in the name of the ability to choose the ability: ")
    ability=input()
    if r1=='hacker' or r1=='1':
        if ability=='cheat sheet' or ability=='1':
            print("great choice")
            points=points-50000
            print(points)
            break
        elif ability=='glitch the servers' or ability=='2':
            print("great choice")
            points=points-20000
            print(points)
            break
        elif ability=='matrix dodge' or ability=='3':
            print("great choice")
            points=points-10000
            print(points)
            break
    elif r1=='fighter' or r1=='2':
        if ability=='roundhouse kick' or ability=='1':
            print("great choice")
            points=points-10000
            print(points)
            break
        elif ability=='street fighter hadouken' or ability=='2':
            print("great choice")
            points=points-30000
            print(points)
            break
        elif ability=='uppercut' or ability=='3':
            print("great choice")
            points=points-5000
            print(points)
            break
    elif r1=='casual person' or r1=='3':
        if ability=='punch' or ability=='1':
            print("great choice")
            points=points-1000
            print(points)
            break
        elif ability=="Man's best friend" or ability=='2':
            print("great choice")
            points=points-10000
            print(points)
            break
        elif ability=='Fast car' or ability=='3':
            print("great choice")
            points=points-5000
            print(points)
            break
while True:
    print("now that you have chosen your ability you can choose your username")
    player_name=str(input("enter your username: "))
    player_ID=random.randrange(1,1000000000000)
    print("welcome player "+str(player_name)+"#"+str(player_ID))
    break
while True:
    r=input("you are now done creating your character and can finally start your adventure press ENTER when ready: ")
    if r=='':
        print("Level 1")
        r=input("write 'start' when you are ready: ")
        if r=='start':
            print("you find yourself in a forest the wind blows through your hair and black belt")
            print("as you examine your surroundings a weird creature steps out of a bush")
            print("ATTACK MODE ENTERED")
            print("type 'fight' to start to fight")
            break
while True:
    r=input()
    if r=='fight':
        print("BATTLE TIME")
        print("Guide npc: Hello "+str(player_name)+"#"+str(player_ID)+" and welcome.")
        print("In this game you will have to choose what you do and you have just entered combat.")
        print("Looking at your character sheet I can see that you have chosen the ability "+str(ability)+" cool choice.")
        print("underneath you can see your menu where you will decide which ability you want to use to fight.")
        print("now type 'fight' and then select your ability")
        player_health=100
        player_health_full=100
        tutorial_enemy_health=100
        tutorial_enemy_health_full=100
        Player_menu = ("MENU: 1.fight 2.Items: 0 Player health:" + str(player_health) + "/" + str(player_health_full) + " 4.Points:" + str(points))
        print(Player_menu)
        print("5. Enemy health"+str(tutorial_enemy_health)+"/"+str(tutorial_enemy_health_full))
        r=str(input("SELECT: "))
        print("FIGHT Menu 1."+str(ability))
        r=str(input("SELECT ABILITY: "))
        if r==ability=='cheat sheet'or r==ability=='glitch the servers'or r==ability=='street fighter hadouken'or r==ability=='roundhouse kick'or r==ability=='uppercut'or r==ability=="Man's best friend"or r==ability=='punch' or ability=='1' or ability=='2' or ability=='3':
            print("you used the ability "+str(ability)+" it is quite effective")
            print("enemy health goes down 70/"+str(tutorial_enemy_health_full)+"enemies turn")
            print("the enemy attacks you with what seems like its claws and your health also goes down player health 70/"+str(player_health_full))
            print("to shorten down this tutorial you will be taken to the last part of the tutorial")
            break
        elif r==ability=='matrix dodge' or ability=='3':
            print("you have done a pointless dodge enemy health:"+str(tutorial_enemy_health)+"/"+str(tutorial_enemy_health_full))
            print("because your only ability is to dodge there is no point in continuing this fight and we will get to the last part of the tutorial")
            break
        elif r==ability=='Fast car' or ability=='3':
            print("you escaped the fight with your car and you suffocated your enemy with the smoke but because you")
            print("escaped you only get half the prize!")
            print("you are close to finishing the tutorial just one more step")
            break
while True:
    import random
    loot_drops=["sword","armor","potion"]
    a=random.choices(loot_drops)
    print("you have done good in your first ever battle but the tutorial is not over yet just type 'loot'")
    print("in the typing box to loot the enemy for items and get cool items that might help you later in the game")
    r=input()
    if r=='loot':
        print("you got "+str(a[0])+" level 1 item and plus 10 points")
        points=points+10
        loot=[]
        loot.append(a)
        Player_menu = ("MENU: 1.fight 2.Items: "+str(len(a))+" Player health:" + str(player_health) + "/" + str(player_health_full) + " 4.Points:" + str(points))
        print(Player_menu)
        r=str(input("enter 'items' into the type box to see which items you have: "))
        if r=='items':
            print(a[0]+" level 1 item")
            break
print("thank you for playing this demo I am working on getting you the rest of this game out as soon as possible and hope you enjoyed")
