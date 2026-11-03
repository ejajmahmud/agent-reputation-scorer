"""Command-line interface for Agent Reputation Scorer."""
import argparse
from .reputation import BayesianReputationScorer

def main():
    parser = argparse.ArgumentParser(description="Agent Reputation Scorer CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate Bayesian reputation tracking")
    args = parser.parse_args()

    scorer = BayesianReputationScorer()
    print("Initial neutral score:", scorer.get_score("agent_coder"))

    for _ in range(5):
        scorer.record_outcome("agent_coder", success=True)
    print("Score after 5 verified passes:", scorer.get_score("agent_coder"))

    for _ in range(3):
        scorer.record_outcome("agent_coder", success=False)
    print("Score after 3 failed builds:", scorer.get_score("agent_coder"))
    print("Detailed stats:", scorer.stats("agent_coder"))

if __name__ == "__main__":
    main()
