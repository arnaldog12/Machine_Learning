import unittest

import numpy as np
from boruta import BorutaPy
from sklearn.ensemble import RandomForestClassifier


class BorutaTestCases(unittest.TestCase):
    def test_get_tree_num(self):
        rfc = RandomForestClassifier(max_depth=10)
        bt = BorutaPy(rfc)
        self.assertEqual(bt._get_tree_num(10), 44, "Tree Est. Math Fail")
        self.assertEqual(bt._get_tree_num(100), 141, "Tree Est. Math Fail")

    def test_if_boruta_extracts_relevant_features(self):
        np.random.seed(42)
        y = np.random.binomial(1, 0.5, 1000)
        x = np.zeros((1000, 10))

        z = y - np.random.binomial(1, 0.1, 1000) + np.random.binomial(1, 0.1, 1000)
        z[z == -1] = 0
        z[z == 2] = 1

        # 5 relevant features
        x[:, 0] = z
        x[:, 1] = y * np.abs(np.random.normal(0, 1, 1000)) + np.random.normal(0, 0.1, 1000)
        x[:, 2] = y + np.random.normal(0, 1, 1000)
        x[:, 3] = y**2 + np.random.normal(0, 1, 1000)
        x[:, 4] = np.sqrt(y) + np.random.binomial(2, 0.1, 1000)

        # 5 irrelevant features
        x[:, 5] = np.random.normal(0, 1, 1000)
        x[:, 6] = np.random.poisson(1, 1000)
        x[:, 7] = np.random.binomial(1, 0.3, 1000)
        x[:, 8] = np.random.normal(0, 1, 1000)
        x[:, 9] = np.random.poisson(1, 1000)

        rfc = RandomForestClassifier()
        bt = BorutaPy(rfc)
        bt.fit(x, y)

        # make sure that only all the relevant features are returned
        self.assertItemsEqual(range(5), list(np.where(bt.support_)[0]))


if __name__ == "__main__":
    unittest.main()
