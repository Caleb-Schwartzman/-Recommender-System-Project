import argparse
import csv
import sys

class Recommendation:
    """
    Class that stores the CSV data containing a users name, favorite song, and the genre
    of that song
    
    Attributes:
        genre - the favorite genre of the user to find matches
    """
    userPickedGenre = ""
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
        
        Returns:
            Genre - the user's favorite genre from the inputted answers
        """
        # f = open("Recommendation.csv", "a")
        
        # f.write(Name)
        # f.write(Genre)
        # f.write(Song)
        # f.write(Artist)

        with open('Recommendation.csv', 'a') as file_object:
            Name = input("What is your name: ")
            self.userPickedGenre = input("What is your favorite genre? ")
            Song = input("What is your favorite song within that genre? ")  
            Artist = input("Who is the song made by? ")
            List = [Name, self.userPickedGenre, Song, Artist]

            #Writes user answers to the csv
            writer_object = csv.writer(file_object)
            writer_object.writerow(List)
            file_object.close()
            
        # self.genre = Genre
    





    def match(self, genre):
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
                # print(row)
                if row[0] == genre:
                    songTitle = row[1]
                    artist = row[2]
                    matchingSongs.append(f"{songTitle} - {artist}")
            
        return matchingSongs
    
    #def friend(self):
    #    with open(self.path, 'r') as csvFile:
    #        data = csv.reader(csvFile)
    #        #skip header
    #        next(data)
    #        match_friend = []
    #        for row in data:
    #            if row[4] == self.name:
    #                friendName = row[4]
    #                song = row[2]
    #                match_friend.append(f"{match_friend}'s favorite song is {song}") 
    #    return match_friend
    
    
    # searches for song name from users imput of friend
    #need to make input function for this                
                    
def main(path):
    #creates Recommendation object
    data = Recommendation(path)
    #calls the user_input function to prompt the user with questions
    data.user_input()
    #calls match function to go through csv and find matching songs
    askUserSearch = input("Do you want to list songs that match your Genre?")
   
    if askUserSearch == "Yes":
        # print(data.userPickedGenre)
        matches = data.match(data.userPickedGenre)
        print(matches)




    

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
    
