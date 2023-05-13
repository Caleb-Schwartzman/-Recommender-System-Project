import argparse
import csv
import sys

class Recommendation:
    """
    Class that stores the CSV data containing a users name, favorite song, and the genre
    of that song
    
    Attributes:
        genre - the favorite genre of the user to find matches
        path - dataset used by program to get favorite songs
    """
    def __init__(self, path):
        """
        Reads data from csv file 
        
        Args:
            path - csv file path passed in through terminal
        """
        self.path = path
            
        
    def user_input(self):
        """
        Ask for user input and then writes the user inputted data
        into CSV file to continue adding to the data
        
        Side Effects:
            Writes list to csv file
        """
        with open('Recommendation.csv', 'a', newline='') as file_object:
            Genre = input("What is your favorite genre? ")
            self.genre = Genre
            Song = input("What is your favorite song within that genre? ")  
            Artist = input("Who is the song made by? ")
            Name = input("What is your name: ")
            self.name = Name
            List = [Genre, Song, Artist, Name]

            #Writes user answers to the csv
            writer_object = csv.writer(file_object)
            writer_object.writerow(List)
            file_object.close()
            
    def match(self):
        """
        Searches for matches based on the user's favorite genre
        
        Returns:
            matchingSongs - list of strings containing matching songs
            that share the same genre as the user's favorite
        """
        with open(self.path, 'r') as csvFile:
            data = csv.reader(csvFile)
            #skip header
            next(data)
            matchingSongs = []
            #Find matching genres 
            for row in data:
                #disregards capitalization to get a match
                if row[0].lower() == self.genre.lower():
                    songTitle = row[1]
                    artist = row[2]
                    name = row[3]
                    if name != self.name:
                        matchingSongs.append(f"{songTitle} - {artist}")
                    else:
                        continue
            
        return matchingSongs
    
    def friend(self, nameFriend):
        """
        Searches for friend's name in the csv and returns the matching song
        
        Args:
            nameFriend - friends name that was user inputted
            
        Returns:
            match_friend - list with friend's favorite song
        """
        with open(self.path, 'r') as csvFile:
            data = csv.reader(csvFile)
            #skip header
            next(data)
            match_friend = []
            for row in data:
                if row[3].lower() == nameFriend.lower():
                    name = row[3]
                    songTitle = row[1]
                    artist = row[2]
                    
                    match_friend.append(f"{name}'s favorite song is {songTitle} by {artist}") 
        return match_friend               
                    
def main(path):
    """
    Main function that creates recommendation class object and calls the functions within it while also
    asking if user wants a recommendation of songs or/and their friends favorite song
    
    Args:
        path - path is the csv file being used as the dataset
        
    Side Effects:
        Prints a list of songs to the user to recommend if they request and also prints their friend's favorite
        song at their request as well    
    """
    
    data = Recommendation(path)
    #calls the user_input function to prompt the user with questions
    data.user_input()
    #calls match function to go through csv and find matching songs
    matches = data.match()
    askUserSearch = input("Do you want to list songs that match your Genre? ")
    askUserFriend = input("Do you want to see your friends favorite song? If so type their name: ")
   
    if askUserSearch == "Yes":
        print("Here are some songs you might like: ")
        for song in matches:
            print(song)

    friendSong = data.friend(askUserFriend)
    if not friendSong:
        print("Friend not found")
    else:
        print(friendSong[0])

def parse_args(args_list):
    """
    Takes a string from the command prompt and passes them as an argument. Allows program
    to be ran from the terminal
    
    Args:
        args_list (list) - the list of string(s) from the command prompt
        
    Returns:
        args (ArgumentParser)
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument('csv_file', type = str, help = 'The path to the dataset csv file')
    
    args = parser.parse_args(args_list)
    
    return args

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    #calls main function using the path passed in the terminal as argument
    main(args.csv_file)
