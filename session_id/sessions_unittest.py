import random
import unittest
import time
import pandas as pd
from create_df import create_random_df
from get_session_id import apply_session_id


class TestIDGeneration(unittest.TestCase):

    def test_single_customer_in_single_timeframe(self):
        df = create_random_df(1000, 1, 3)
        apply_session_id(df)
        unique_sessions = df['session_id'].nunique()

        self.assertEqual(unique_sessions, 1)

    def test_single_customer_in_multiple_timeframe(self):
        timeframes = 5
        df = pd.DataFrame(
            {'customer_id': [1 for _ in range(timeframes)],
             'product_id': [random.randint(1, 50) for _ in range(timeframes)],
             'timestamp': [time.time() + ses * 181 for ses in range(timeframes)]})

        apply_session_id(df)
        unique_sessions = df['session_id'].nunique()

        self.assertEqual(unique_sessions, timeframes)

    def test_multiple_customer_in_single_timeframe(self):
        customer_num = 10
        df = create_random_df(1000, customer_num, 3)
        apply_session_id(df)
        unique_sessions = df['session_id'].nunique()

        self.assertEqual(unique_sessions, customer_num)


if __name__ == '__main__':
    unittest.main()
