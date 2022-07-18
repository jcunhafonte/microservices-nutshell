import grpc
import permission_pb2 as permission_pb2
import permission_pb2_grpc as permission_pb2_grpc


from concurrent import futures
from authorization.casbin import Casbin


class PermissionServicer(permission_pb2_grpc.PermissionServicer):
    def GetPolicies(self, request, context):
        if request.user_id not in Casbin.get_users():
            raise grpc.RpcError(grpc.StatusCode.NOT_FOUND, 'User not found')

        policies = Casbin().enforcer.get_filtered_policy(0, str(request.user_id))
        policies = [permission_pb2.GetPolicyReply(object=policy[1], action=policy[2]) for policy in policies]
        policies = permission_pb2.GetPoliciesReply(user_id=request.user_id, policies=policies)
        return policies

    def CreatePolicy(self, request, context):
        if request.user_id not in Casbin.get_users():
            raise grpc.RpcError(grpc.StatusCode.NOT_FOUND, 'User not found')

        enforcer = Casbin().enforcer
        enforcer.add_named_policy("p", str(request.user_id), request.object, request.action)
        enforcer.save_policy()

        policy = permission_pb2.CreatePolicyReply(user_id=request.user_id, object=request.object, action=request.action)

        return policy


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    permission_pb2_grpc.add_PermissionServicer_to_server(PermissionServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print('Server started at localhost:50051')
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
