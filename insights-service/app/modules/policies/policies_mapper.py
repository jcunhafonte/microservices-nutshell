from typing import List


from modules.policies.policies_dtos import Policy, Policies
from modules.policies.policies_models import PolicyModel


class PoliciesMapper:
    def to_policy(self, policy: PolicyModel) -> Policy:
        return Policy(object=policy.object, action=policy.action)

    def to_policies(self, policies: List[PolicyModel]) -> Policies:
        return Policies(policies=[self.to_policy(policy) for policy in policies])
