"""Init script for the algorithms submodule."""
from hbaselines.algorithms.off_policy import OffPolicyRLAlgorithm
from hbaselines.algorithms.off_policy_com import OffPolicyRLAlgorithm as OffPolicyRLAlgorithm_COM
__all__ = ["OffPolicyRLAlgorithm", "OffPolicyRLAlgorithm_COM"]
