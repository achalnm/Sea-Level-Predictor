import unittest
import pandas as pd

class TestSeaLevelPredictor(unittest.TestCase):
    def test_data_import(self):
        df = pd.read_csv('epa-sea-level.csv')
        self.assertTrue('Year' in df.columns)
        self.assertTrue('CSIRO Adjusted Sea Level' in df.columns)
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
