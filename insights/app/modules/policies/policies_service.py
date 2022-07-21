import grpc


from permission_pb2 import GetPoliciesReply, GetPolicyRequest
from permission_pb2_grpc import PermissionStub


class PoliciesService:
    channel = grpc.insecure_channel("permissions:50051")
    stub = PermissionStub(channel)

    def get_policies_by_user_id(self, user_id: int) -> GetPoliciesReply:
        policies = self.stub.GetPolicies(GetPolicyRequest(user_id=user_id))
        return policies
