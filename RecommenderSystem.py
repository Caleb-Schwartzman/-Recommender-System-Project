import argparse





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

    def input():
        """"""

class Genre_Choice:



    def user_input():







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

