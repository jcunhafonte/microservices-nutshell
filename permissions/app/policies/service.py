from typing import List


from policies.deps import enforcer


class PoliciesService:
    def get_policies(self) -> List[dict]:
        return enforcer.get_policy()

    def get_policies_by_user_id(self, user_id: int) -> List[tuple]:
        return enforcer.get_filtered_policy(0, str(user_id))

    def create_policy(self, user_id: int, object: str, action: str) -> dict:
        enforcer.add_named_policy("p", str(user_id), object, action)
        enforcer.save_policy()
        return dict(user_id=str(user_id), object=object, action=action)

    def has_policy(self, user_id: int, object: str, action: str) -> dict:
        if enforcer.enforce(str(user_id), object, action):
            return dict(access=True, message=f"User {user_id} has access!")

        return dict(access=False, message=f"User {user_id} is forbidden!")
