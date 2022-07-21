import grpc


from permission_pb2 import GetPoliciesByUserReply, GetPoliciesByUserRequest, CheckPolicyReply, CheckPolicyRequest, CreatePolicyReply, CreatePolicyRequest
from permission_pb2_grpc import PermissionStub


class PoliciesService:
    channel = grpc.insecure_channel("permissions-service:50051")
    stub = PermissionStub(channel)

    def get_policies_by_user_id(self, user_id: int) -> GetPoliciesByUserReply:
        policies = self.stub.GetPoliciesByUser(GetPoliciesByUserRequest(user_id=user_id))
        return policies

    def get_check_policy_by_user_id(self, user_id: int, object: str, action: str) -> CheckPolicyReply:
        check_policy = self.stub.CheckPolicy(CheckPolicyRequest(user_id=user_id, object=object, action=action))
        return check_policy

    def create_policy_by_user_id(self, user_id: int, object: str, action: str) -> CreatePolicyReply:
        policy = self.stub.CreatePolicy(CreatePolicyRequest(user_id=user_id, object=object, action=action))
        return policy