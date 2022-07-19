import grpc
import permission_pb2
import permission_pb2_grpc


from concurrent import futures
from ac.user import User, validate_user


class PermissionServicer(permission_pb2_grpc.PermissionServicer):
    def GetPolicies(self, request, context):
        policies = User(request.user_id).get_policies()
        policies = [permission_pb2.GetPolicyReply(object=policy[1], action=policy[2]) for policy in policies]
        policies = permission_pb2.GetPoliciesReply(user_id=request.user_id, policies=policies)
        return policies

#     @validate_user
#     def CreatePolicy(self, request, context):
#         User(request.user_id).add_policy(request.object, request.action)
#         policy = permission_pb2.CreatePolicyReply(user_id=request.user_id, object=request.object, action=request.action)
#         return policy

#     @validate_user
#     def CheckPolicy(self, request, context):
#         check_policy = User(request.user_id).has_policy(request.object, request.action)
#         policy = permission_pb2.CheckPolicyReply(access=check_policy["access"], message=check_policy["message"])
#         return policy


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
