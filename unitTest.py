import unittest
import tempfile
import RecommenderSystem

class RecommendationTest(unittest.TestCase):
    """
    Test for our RecommenderSystem file and Recommendation class
    """
    def setUp(self):
        """
        Setups a temp csv file to use as our testing file when performing functions upon it
        
        Side Effects:
            Uses self.csv_file as the pathway and includes it as an attribute for current test case
        """
        with tempfile.NamedTemporaryFile(delete=False) as csv_file:
            csv_file.write(b"Genre,Song,Artist,Name\n")
            csv_file.write(b"Pop,Red,Taylor Swift,Mary\n")
            csv_file.write(b"Rock,Purple Haze,Jimi Hendrix,Michael\n")
            csv_file.write(b"Rap,Jumpman,Drake,Dominic\n")
            
        self.csv_file = csv_file.name
        
        self.recommendation = RecommenderSystem.Recommendation(self.csv_file)
                 
    def test_match(self):
        """
        Test match function within the class by setting genre to Rap and name to Mark to get a sample
        return
        """
        self.recommendation.genre = "Rap"
        self.recommendation.name = "Mark"
        self.assertEqual(self.recommendation.match(), ["Jumpman - Drake"])
        
    def test_friend(self):
        """
        Test friend function within the class by setting friend's name to Mary to see if function can find her
        name within csv file and return her song
        """
        self.assertEqual(self.recommendation.friend("Mary"), ["Mary's favorite song is Red by Taylor Swift"])

    def askFavoriteSong(self):
        """
        To test this function, you can type what your favorite genre is and see if it matches up with the next question.
        Enter your favorite genre and then you will be asked to input your favorite song within that genre. If the 
        genre you entered matches the genre mentioned in the first question then the function is working correctly.
        
        """    
            
        self.assertEqual(self.recommendation.askFavoriteSong("Rock"), "What is your favorite song within Rock?" )
        self.assertEqual(self.recommendation.askFavoriteSong("."), "What is your favorite song within .?" )
        self.assertEqual(self.recommendation.askFavoriteSong("dsfdfdsfsd"), "What is your favorite song within dsfdfdsfsd?" )


    #def test_user_input():
        """
        To test user_input, the user must input their own items when prompted and running the main RecommenderSystem.py file
        and ensure that based on what they input, it is clearly inputted into the csv file in the same format as every other song.
        """

    #def test_recommendation_init(self):
        """
        To test the __init__ function, pass in an invalid path in the terminal. For example, if you were to type in 
        "python recommend.py Recommendation" in order to run the code on the terminal, an error will show up. You need to 
        be specific with the file path as that determines where the output is being written
        """
    
if __name__ == '__main__':
    unittest.main()
