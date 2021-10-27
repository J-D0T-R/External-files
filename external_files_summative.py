###   External Files Summative   ###
###   James Rutley   ###
###   Start Date: 10/26/2021   ###
###   End Date: 10/27/2021   ###
## Notes

## external files benefit this program tremendously.
## by creating a list from a txt file, the main file becomes significantly smaller
## This also allows the index items on the list to stored file the code isn't running.
## so the same list can be aceesed at different times without it having to manually be recreated\
## since each time the code is run arrays can use only their preset values
## using external files lets my bypass this and save information between uses.
## The file created can slo be shared independantly
## the data can be acessed without running the code
## this makes it significantly easier to work with and share.

## if I had more time to work or got to revisit this assignment
## I would replace the while loops in main() by finding a way to incoropate them in add_score()
## I would use path.os to sreach for files and acess different ones
## (removing the issue of writing over the txt file whenever a new scores list is made)
## without it, this code escapes the issue of filenotfound
## by creating a new file automatically with file.open if an existing one can't be found.
## searching for files would also be used to create a new file if one couldn't be found after
## they input (n) when asked if they want to make a new file
# this would remove the need for lines 95 - 99.

# Arrays
high_scores = {}

# Functions
def add_score():
    #opens a text file for apending
    file = open('my_highscores.txt', 'a')
    #gives visual confirmation that the code is working
    #print("File opened for writing.")
    user = input("Enter Username: ")
    file.write(f",{user},") # Adds their input to the file
    score = input("Enter score: ")
    file.write(f"{score}") # Adds their input to the file
    file.close()
    
    
def view_score():
    file = open('my_highscores.txt', 'r') # Opens the file for reading
    scores_list = file.read().split(',') #splits the file at each comma, and stores each item as a single index in a list
    #print(scores_list) # I used these lines to figure out why I kept getting index errors
    #print(scores_list[0]) # It turned out that putting a coma after a score
    # (which would always be the last character added to the list) caused a blank space to be added to the list uninteniontaly.
    # So I removed the comma from the scores and put in front of the username instead. This sloved the problem.
    item = 0
    while item < (len(scores_list)): #scrape the list and turn it into a dictionary where it goes odd-key:even-value
        high_scores[scores_list[item]] = scores_list[item + 1]
        item = item + 2
    print(high_scores) # Displays the list of highscores
    file.close() #closes the file
    return file #returns the filename so it can be used in other functions
    
def main():
    reset = input("Do you want to create a new score sheet? (y/n) ").lower() #Checking if they want to make a new list or add to an old one.
    
    if "y" in str(reset): # Warning the user that making a new list will overwrite the old one.
        print("If you do, the old list will be overwritten. You can avoid overwriting the previous list by renaming it.")
        check = input("Are you sure you want to proceed? (y/n) ").lower()
        
        if "y" in str(check): # they want a new list
            file = open('my_highscores.txt', 'w') # opens the file for writing
            file.write("Name, Score") # formatting that also serves to clear the existing
            file.close()
            add_score
            while True: # Allows multiple scores to be added recursively
                add_score()
                more_score = input("Do you want to enter another score?(y/n) ").lower()
                
                if "y" in str(more_score):
                    pass
                
                else:
                    view_score()
                    break
            pass
        
        else:
            while True: # Allows multiple scores to be added without constantly running the file
                add_score()
                more_score = input("Do you want to enter another score?(y/n) ").lower()
                
                if "y" in str(more_score):
                    pass
                
                else:
                    view_score()
                    break
        
    else:
        file = open('my_highscores.txt', 'a') # opens the file for writing
        file.write("filler, filler") # ensures that an index error won't occur due to the blank space issue
        # if it can't find an existing file and makes a new one.
        file.close()
        add_score
        while True: # Allows multiple scores to be added without constantly running the file
            add_score()
            more_score = input("Do you want to enter another score?(y/n) ").lower()
            
            if "y" in str(more_score):
                pass
            
            else:
                view_score()
                break
            
# Main Code   
main()
