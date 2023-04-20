import argparse
from csv import writer





class Reccomendation:
    """class for making reccomendation to user
    
    """

    def __init__(self):
        self

    def readData():
        """data from csv file 
    
    """



    def genreRec():
        """Function 
    
    
    """
    def match():
        """"""
    def input():
        """"""

    def songChoice():
        """"""
    
    def artistChoice():
        """"""

def user_input():
        """"""
        # f = open("Recommendation.csv", "a")
        
        # f.write(Name)
        # f.write(Genre)
        # f.write(Song)

        with open('Recommendation.csv', 'a') as file_object:
            Name = input("What is your name: ")
            Genre = input("What is your favorite genre? ")
            Song = input("What is your favorite song within that genre? ")  
            List = [Name, Genre, Song]


            writer_object = writer(file_object)

            writer_object.writerow(List)
    
            file_object.close()



if __name__ == "__main__":
    user_input()






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

