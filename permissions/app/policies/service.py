from typing import List


from policies.deps import enforcer as enforcer_v2


class PoliciesService:
    def get_policies_by_user_id(self, user_id: int) -> List[tuple]:
        # from casbin.enforcer import Enforcer
        # from policies.my_mom import Adapter

        # adapter = Adapter("postgresql://permissions:permissions@permissions-database:5432/permissions")
        # enforcer_v2 = Enforcer("policies/ac_model.conf", adapter)

       # print(enforcer_v2.get_policy())
        print('FIRST ---->', enforcer_v2.get_filtered_policy(0, str(user_id)))

      #  enforcer_v2.add_policy("2", "reports", "write")
       # enforcer.add_policy("2", "payments", "read")

        print('SECOND ---->', enforcer_v2.get_filtered_policy(0, str(user_id)))

        return enforcer_v2.get_filtered_policy(0, str(user_id))

    def create_policy(self, user_id: int, object: str, action: str) -> dict:
        enforcer_v2.add_named_policy("p", str(user_id), object, action)
        enforcer_v2.save_policy()
        return dict(user_id=str(user_id), object=object, action=action)

    def has_policy(self, user_id: int, object: str, action: str) -> dict:
        return dict()
        # if enforcer.enforce(str(user_id), object, action):
        #     return dict(access=True, message=f"User {user_id} has access!")

        # return dict(access=False, message=f"User {user_id} is forbidden!")
