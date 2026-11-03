"""Bayesian reputation and trust scoring for autonomous multi-agent swarms."""
from typing import Dict, Any


class BayesianReputationScorer:
    def __init__(self, prior_alpha: float = 2.0, prior_beta: float = 2.0):
        self.prior_alpha = prior_alpha
        self.prior_beta = prior_beta
        self._scores: Dict[str, Dict[str, float]] = {}

    def _get_agent(self, agent_id: str) -> Dict[str, float]:
        if agent_id not in self._scores:
            self._scores[agent_id] = {
                "alpha": self.prior_alpha,
                "beta": self.prior_beta,
                "evaluations": 0
            }
        return self._scores[agent_id]

    def record_outcome(self, agent_id: str, success: bool, weight: float = 1.0) -> None:
        rec = self._get_agent(agent_id)
        rec["evaluations"] += 1
        if success:
            rec["alpha"] += weight
        else:
            rec["beta"] += weight

    def get_score(self, agent_id: str) -> float:
        """Returns expected mean reputation between 0.0 and 1.0."""
        rec = self._get_agent(agent_id)
        return round(rec["alpha"] / (rec["alpha"] + rec["beta"]), 4)

    def stats(self, agent_id: str) -> Dict[str, Any]:
        rec = self._get_agent(agent_id)
        return {
            "agent_id": agent_id,
            "reputation_score": self.get_score(agent_id),
            "alpha_successes": rec["alpha"],
            "beta_failures": rec["beta"],
            "total_tasks": rec["evaluations"]
        }
