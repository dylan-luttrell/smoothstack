import unittest
import doc_parser
from datetime import datetime

class Test_Is_Valid_File_Name(unittest.TestCase):
    """ test if file name checker is working properly """
    def test_valid(self):
        """ check a number of possible file names """
        file_names = ["expedia_report_monthly_january_2018.xlsx",
                      "expedia_report_monthly_january_2012.xlsx",
                      "expedia_report_monthly_march_2018.xlsx",
                      "expedia_report_monthly_april_2018.xlsx",
                      "expedia_report_monthly_december_2018.xlsx",
                      "expedia_report_monthly_august_2018.xlsx"]
        
        for name in file_names:
            self.assertTrue(doc_parser.is_valid_filename(name))
    
    def test_invalid(self):
        """ check a number of invalid file names """
        file_names = ["expedia_report_monthly_january_201.xlsx", 
                      "expedia_report_monthly_januar_2012.xlsx",
                      "expedia_report_monthlymarch_2018.xlsx",
                      "expedia_report_monthly_april_2018.css",
                      "expedia_report_december_monthly_2018.xlsx",
                      "report_monthly_august_2018.xlsx"]
        
        for name in file_names:
            self.assertFalse(doc_parser.is_valid_filename(name))
            
class test_rank_score(unittest.TestCase):
    
    def test_good(self):
        cases = [(100, 50),
                   (200, 100),
                   (100, 100),
                   (100000000, 100000000)] # large number case
        
        for score, threshold in cases:
            self.assertEquals(doc_parser.rank_score(score, threshold), "good")
            
    def test_bad(self):
        cases = (
            (50, 100),
            (100, 200),
            (100, 101),
            (100000000, 1000000000) # large number case
        )
        
        for score, threshold in cases:
            self.assertEquals(doc_parser.rank_score(score, threshold), "bad")
            
class test_get_date_from_filename(unittest.TestCase):
    
    def test(self):
        cases = (
            (datetime(2018, 1, 1), "expedia_report_monthly_january_2018.xlsx"),
            (datetime(1990, 1, 1), "expedia_report_monthly_january_1990.xlsx"),
            (datetime(2020, 12, 1), "expedia_report_monthly_december_2020.xlsx"),
            (datetime(2018, 2, 1), "expedia_report_monthly_february_2018.xlsx"),
            (datetime(2018, 3, 1), "expedia_report_monthly_march_2018.xlsx")
        )
        
        for dt, filename in cases:
            self.assertEquals(dt, doc_parser.get_date_from_filename(filename))
    