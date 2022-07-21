import grpc
from concurrent import futures


import permission_pb2_grpc
from permission_pb2 import GetPoliciesByUserReply, GetPolicyByUserReply, CreatePolicyReply, CheckPolicyReply
from users.validations import validate_user
from policies.service import PoliciesService


class PermissionServicer(permission_pb2_grpc.PermissionServicer):
    policies_service = PoliciesService()

    @validate_user
    def GetPoliciesByUser(self, request, context) -> GetPoliciesByUserReply:
        policies = self.policies_service.get_policies_by_user_id(request.user_id)
        policies = [GetPolicyByUserReply(object=policy[1], action=policy[2]) for policy in policies]
        policies = GetPoliciesByUserReply(user_id=request.user_id, policies=policies)
        return policies

    @validate_user
    def CreatePolicy(self, request, context):
        policy = self.policies_service.create_policy(request.user_id, request.object, request.action)
        policy = CreatePolicyReply(user_id=request.user_id, object=request.object, action=request.action)
        return policy

    @validate_user
    def CheckPolicy(self, request, context):
        check_policy = self.policies_service.has_policy(request.user_id, request.object, request.action)
        check_policy = CheckPolicyReply(access=check_policy["access"], message=check_policy["message"])
        return check_policy


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    permission_pb2_grpc.add_PermissionServicer_to_server(PermissionServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print('Server started at localhost:50051')
    server.wait_for_termination()


print('Starting server...')
if __name__ == "__main__":
    serve()
