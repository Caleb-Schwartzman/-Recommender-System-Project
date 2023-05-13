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
        
    #def test_user_input():
        """
        To test user_input, the user must input their own items when prompted and running the main RecommenderSystem.py file
        and ensure that based on what they input, it is clearly inputted into the csv file in the same format as every other song.
        """
        
if __name__ == '__main__':
    unittest.main()