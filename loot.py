def getplayer():
        #puts content from txt file in list as dictionaries
        playerList = []
        with open('players.txt','r') as inf:
            for line in inf:
                        playerList.append(eval(line))  
        #makes a list of just player's names
        nameList = []
        for item in playerList:
                for k,v in item.items():
                        if k == 'name':
                                nameList.append(v)
        print('Your players are: ' )
        print(nameList)
        #interactive function that allows player selection and inventory updating
        def playerselect():    
                #defines subprogram rerun functions
                def giveagain():
                        doAgain = str.lower(input("Give anything else to this player?\n"))
                        if doAgain == 'yes' or doAgain == 'y':
                                giveplayer()
                        else:
                                print('Ending item giving program\n')
                def selectagain():
                        newname = str.lower(input("Select another player?\n"))
                        if newname == 'yes' or newname =='y':
                                playerselect()
                        else:
                                print('Ending player selection program\n')
                def takeagain():
                        takemore = str.lower(input("Remove any other items from this player?\n"))
                        if takemore == 'yes' or takemore == 'y':
                                takethaway()
                        else:
                                print('Ending item removal program\n')
                #begin playerselect main program                
                askName= str.lower(input('Select a player \n'))
                if askName in nameList:
                        print('You have selected player ' + askName + '.')
                else:
                        print("Player not found.\n")
                        getplayer()
                #begin item distribution program
                giveany = str.lower(input('Give items to ' + askName + '?\n'))
                def giveplayer():
                                if giveany == 'y' or giveany == 'yes': 
                                        togive = str.lower(input('What do you want to give this player? \n'))
                                        try:
                                                #select player's inventory dictionary
                                                for item in playerList:
                                                        for k,v in item.items():
                                                                if askName == v:
                                                                        #check if item is already in inventory
                                                                        if togive in item:
                                                                                if togive == 'name':
                                                                                        print('Player already has a name!')
                                                                                        break
                                                                                else:
                                                                                        givequant = int(input('How many ' + togive + ' do you want to give ' + askName +'?\n'))
                                                                                        tgvalue = int(item.get(togive))
                                                                                        print(tgvalue)
                                                                                        item[togive] = givequant + tgvalue
                                                                                        print(item)
                                                                                        break
                                                                        else:
                                                                                givequant = int(input('How many ' + togive + ' do you want to give ' + askName +'?\n'))
                                                                                item[togive] = givequant
                                                                                print(item)
                                                                                break
                                
                                        except:
                                                print('invalid quantity\n')
                                                giveplayer()
                                        giveagain()
                                else:
                                        print('ending item giving program\n')
                #begin item removal program
                def takethaway():
                        if toremove == 'y' or toremove == 'yes':
                                removeit = str.lower(input('Which item to remove?\n'))
                                for item in playerList:
                                        for k,v in item.items():
                                                if askName == v: #remove items only from chosen player's inventory
                                                        if removeit in item:
                                                                item.pop(removeit)
                                                                print(item)
                                                                break
                                takeagain()
                        else:
                                print('Exiting item removal program\n')

                        
                                                               
                giveplayer()
                toremove = str.lower(input('Remove items from inventory?\n'))
                takethaway()
                selectagain()
        playerselect()
        #updates player inventor file, saving changes
        def updatelist():
                f = open('players.txt', 'w')
                for item in playerList:
                        f.write(str(item)+'\n') #allows dictionaries to be written to file properly
                f.close()
        updatelist()
getplayer()
