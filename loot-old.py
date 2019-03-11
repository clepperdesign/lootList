# player characters
dicta= {'name': 'A','gold': 5}
dictb= {'name':'B','gold': 10}
dictc={'name':'C','gold': 6}
playerList = [dicta,dictb,dictc]
def getplayer():
        nameList = []
        goldList = []
        print('Your players are: ' )
        for item in playerList:
                for k,v in item.items():
                        if k == 'name':
                                nameList.append(v)
        for item in playerList:
                for k, v in item.items():
                        if k == 'gold':
                                goldList.append(v)
        print(nameList)        
        def playerselect():
                #define subprogram rerun functions
                def giveagain():
                        doAgain = input(str("Give more to this player?\n"))
                        if doAgain == 'yes' or doAgain == 'y':
                                giveplayer()
                        else:
                                print('Ending item giving program\n')
                def selectagain():
                        newname = input(str("Select another player?\n"))
                        if newname == 'yes' or newname =='y':
                                playerselect()
                        else:
                                print('Ending player selection program')
                #begin playerselect main program                
                askName= str(input('Select a player \n'))
                if askName in nameList:
                        print(askName + ' has ' + str(goldList[nameList.index(askName)]) + ' gold.')
                else:
                        print("Player not found.")
                        getplayer()
                def giveplayer():
                        togive = str(input('What do you want to give this player? \n'))
                        givequant = int(input('How many ' + togive + ' do you want to give ' + askName +'?\n'))
                        for item in playerList:
                                for k,v in item.items():
                                        if askName == v:
                                                item[togive] = givequant
                                                print(item)
                                                break
                        giveagain()
                giveplayer()
                selectagain()
        playerselect()       
getplayer()               
