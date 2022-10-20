# James Bebarski
# CS 5003: Recitation for CS 5001
# October 12, 2022
# Project 05: Spaceman Game

import random

# Basic greeting with some rules for the player. 
def getGreetingAndRules():
   print(
     """
          __________________________________________________________________________________________________
         |                                                                                                  |
         |------------------------------------ WELCOME TO SPACEMAN -----------------------------------------|
         |                                                                                                  |
         |                                    ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒                                        |
         |                                    ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒                                        |
         |                                    ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒                                        |
         |                                    ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒                                        |
         |                                    ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒                                        |
         |                                                                                                  |
         |      The object of the game is to try and guess a mystery word by guessing it's characters.      |
         |       Each character in the mystery word is initially represented with a underscore ( _ ).       |
         |                Correct character guesses will be reflected on the game board.                    |
         |                               You only get 6 incorrect attempts.                                 |
         |               For each incorrect attempt the spaceman adds a part to their ship!                 |
         |                 When the spaceman adds his sixth part and takes off YOU LOSE.                    |
         |                                                                                                  |
          --------------------------------------------------------------------------------------------------
   """
   )
   return

# Randomly selects a game word from a list of words. 
def getGameWord():
    word_list = ["conservation", "manage", "captain", "empirical", "implication",
                 "algorithm", "freighter", "wilderness", "aviation", "depart", 
                 "calculate", "program", "education", "agriculture", "machinery",
                 "steed", "platypus", "recluse", "consensus", "beach"]
    
    word_selection = random.choice(word_list)
    return word_selection

# Converts the randomly selected game_word into a list. 
def getGameWordAsList(game_word):
  game_word_list = list(game_word)
  return game_word_list

# Creates a blank game list, that the user will use as a template and working game board.
def getWorkingGameList(game_word_list):
  length_of_game_word_list = len(game_word_list)
  working_game_list = []
  counter = 0
  while counter != length_of_game_word_list:   
    counter += 1
    working_game_list.append(" _ ")    
  return working_game_list

# Provides images of the Spaceman's ship building stages. Each element in the list represents each incorrect guess. 
# On the sixth incorrect guess, it prints YOU LOSE as text art. 
# If our boolean, win, becomes True, the function prints YOU WIN as text art. 
def getGameInformation(incorrect_counter, win, game_word):
  art_list = [

  """
_____________
  """,
  """
  |         |
_/___________\_      
  """,
  """
   _________
  |         |
_/___________\_        
  """,
  """
   _________
  |  O O O  |
_/___________\_         
  """,
  """
      o   o
    __|___|__
   |  O O O  |
 _/___________\_
  """,
  """
       o   o
     __|___|__
    |  O O O  |
  _/___________\_
   V     V     V
  """]
  
  if (incorrect_counter == 1) and (win == False):
    print("You have 5 more attempts.\n")
    print(art_list[0])
    
  elif (incorrect_counter == 2) and (win == False):
    print("You have 4 more attempts.\n")
    print(art_list[1])
    
  elif (incorrect_counter == 3) and (win == False): 
    print("You have 3 more attempts.\n")
    print(art_list[2])
  
  elif (incorrect_counter == 4) and (win == False):
    print("You have 2 more attempts.\n")
    print(art_list[3])
    
  elif (incorrect_counter == 5) and (win == False):
    print("You have 1 more attempts.\n")
    print(art_list[4])
    
  elif (incorrect_counter == 6) and (win == False):
    print(art_list[5])
    print("The spaceman finished building his ship...")
    print("The word was - " + str(game_word) + " -")
    print("""                       
    
█▄█ █▀█ █ █   █   █▀█ █▀ █▀▀
 █  █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄        
  
  """)
  
  if win == True:
   print("""

█▄█ █▀█ █ █   █ █ █ █ █▄ █
 █  █▄█ █▄█   ▀▄▀▄▀ █ █ ▀█

""")
  
  return

# Displays user guess attempts, sorted alphabetically.
def getPastAttempts(user_guess, past_attempts_list):
  join_assist = " "
  past_attempts_list.append(user_guess)
  past_attempts_list = list(set(past_attempts_list))
  past_attempts_list.sort()
  past_attempts_as_string = str(join_assist.join(past_attempts_list))
  print("All Attempts ----> " + past_attempts_as_string)
  return past_attempts_as_string

def main():     
  '''  
  First main calls getGameWord so we can get a random game word for the user, game_word is assigned to the result.
  
  Next, getGreetingAndRules is called and displays a short greeting and some basic game rules. 
  
  After that, we call getGameWordAsList with game_word as a parameter. This converts the random 
  game word into a list, with each character as separate elements of the list. We assign the 
  result to game_word_list. 
  
  Finally, we call getWorkingGameList with game_word_list as a parameter. The function makes a copy of 
  equal length to the game_word_list, but replaces the characters with blanks. This list will be our game board,
  it will change if the user guesses the character of the game word correctly. 
  '''  
  game_word = getGameWord() 
  getGreetingAndRules()
  game_word_list = getGameWordAsList(game_word)
  working_game_list = getWorkingGameList(game_word_list)
  
  # Adds space in between blank spots ( _ ) when we join our lists, strictly for aesthetic purposes.
  join_assist = " "
   # Variable that keeps track of incorrect inputs.
  incorrect_counter = 0
  # List of past characters that the user inputs. Empty at start. 
  past_attempts_list = []
  
  
  # Announces the length of the mystery word the player needs to guess and displays their starting game board. 
  print("The game word contains " + str(len(game_word)) +" characters:\n" + str(join_assist.join(working_game_list)))   
 
  # Checks to see if a user would like play again or quit if the game is over. 
  game_over = False
  while game_over == False: 
    user_guess = ""
    if (incorrect_counter == 6) or (game_word_list == working_game_list):
      print("\nWould you like to play again?\nEnter y to continue, or n to quit.")
      answer = str(input(">>> "))
      if answer.lower() == "n":
        quit()
      elif answer.lower() == "y":
        main()
      else:
        print("Please enter either y to continue, or n to quit.")
        answer = str(input(">>> \n"))
    
    print("\nInput guess below:")    
    user_guess = str(input(">>> ")).lower()
   
    # Conditional that checks to see if input is not inside the random game word list.
    if user_guess not in game_word_list:
      incorrect_counter += 1
      print("=====================================================")
      print("Sorry, that character was not in the game word.")
      getGameInformation(incorrect_counter, win=False, game_word=game_word)
      getPastAttempts(user_guess, past_attempts_list)
      print("\nFound Characters: " + str(join_assist.join(working_game_list)))
    
    # Conditional that checks to see if user input is inside the game_word_list. 
    if user_guess in game_word_list:
      game_word_list_temp = game_word_list.copy()
      while user_guess in game_word_list_temp:
        character_location = game_word_list_temp.index(user_guess)
        game_word_list_temp.remove(user_guess) in game_word_list
        game_word_list_temp.insert(character_location, "-") in game_word_list
        working_game_list[character_location] = user_guess
        print("=====================================================")
        print("Nice guess! That character was in the game word.\n")
        getPastAttempts(user_guess, past_attempts_list)
        print("\nFound Characters: " + str(join_assist.join(working_game_list)))
       
        # If game_word_list is the same as the working_game_list then the player has won.
        if game_word_list == working_game_list:
          getGameInformation(incorrect_counter, win=True, game_word=game_word)
          print("The word was - " + game_word + " -")  

if __name__ == "__main__":    
  main()
    
  