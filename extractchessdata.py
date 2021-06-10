import os

path = "standard/"
linecount = 0
gamecount = 0
oldgamecount = 0

def savegame(event, site, date, round, whiteelo, blackelo, whiteratingdiff, blackratingdiff, eco, opening,termination,  game, winner):
    print("site: "+site)
    print("date: "+date)
    print("game: "+game)
    print("winner: "+str(winner))

Event = ""
Site = ""
Date = ""
Round = "??"
Whiteelo = 0
Blackelo = 0
Whiteratingdiff = 0
Blackratingdiff = 0
Eco = ""
Opening = ""
Termination = ""
Game = ""
#if winner = 1 white wins, if winner = -1 black wins, 0 means a tie
Winner = 0


for root, dirs, files in os.walk(path, topdown=False):
    for filename in files:
        if(filename[-13:] == ".decompressed"):
            with open(path + filename) as file:
                for fullline in file:
                    linecount +=1
                    line = fullline.strip()

                    if(line[:8] == "[Event \""):
                        #if new game
                        gamecount += 1

                    if(oldgamecount != gamecount and gamecount != 1):
                        #new game, save old game and reset vars
                        oldgamecount = gamecount
                        savegame(Event, Site, Date, Round, Whiteelo, Blackelo, Whiteratingdiff, Blackratingdiff, Eco, Opening, Termination, Game, Winner)

                    if(line[:8] == "[Event \""):
                        Event = line[8:].replace("\"]","")
                    elif(line[:7] == "[Site \""):
                        Site = line[7:].replace("\"]","")
                    elif(line[:10] == "[UTCDate \""):
                        Date = line[10:].replace("\"]","")
                    elif(line[:11] == "[WhiteElo \""):
                        try:
                            Whiteelo = int(line[11:].replace("\"]",""))
                        except:
                            Whiteelo = -1
                    elif(line[:11] == "[BlackElo \""):
                        try:
                            Blackelo = int(line[11:].replace("\"]",""))
                        except:
                            Blackelo = -1
                    elif(line[:18] == "[WhiteRatingDiff \""):
                        Whiteratingdiff = int(line[18:].replace("\"]",""))
                    elif(line[:18] == "[BlackRatingDiff \""):
                        Blackratingdiff = int(line[18:].replace("\"]",""))
                    elif(line[:6] == "[ECO \""):
                        Eco = line[6:].replace("\"]","")
                    elif(line[:10] == "[Opening \""):
                        Opening = line[10:].replace("\"]","")
                    elif(line[:14] == "[Termination \""):
                        Termination = line[14:].replace("\"]","")
                    
                    if(line[:2] == "1."):
                        if(line[-3:] == "1-0"):
                            Winner = 1
                            line = line[:-4]
                        elif(line[-3:] == "0-1"):
                            Winner = -1
                            line = line[:-4]
                        elif(line[-7:] == "0.5-0.5"):
                            Winner = 0
                            line = line[:-7]
                        Game = line

