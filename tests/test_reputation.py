"""Unit tests for BayesianReputationScorer."""
import unittest
from agent_reputation_scorer.reputation import BayesianReputationScorer

class TestReputationScorer(unittest.TestCase):
    def test_score_progression(self):
        scorer = BayesianReputationScorer(prior_alpha=1.0, prior_beta=1.0)
        self.assertEqual(scorer.get_score("a1"), 0.5)

        scorer.record_outcome("a1", True)
        self.assertGreater(scorer.get_score("a1"), 0.5)

        scorer.record_outcome("a1", False)
        self.assertEqual(scorer.get_score("a1"), 0.5)

if __name__ == "__main__":
    unittest.main()
