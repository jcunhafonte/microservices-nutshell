import grpc
from concurrent import futures


import permission_pb2
import permission_pb2_grpc


users = {
    1: {
        'name': 'John',
        'policies': [
            {
                'action': 'read',
                'object': 'stock_reports',
            },
            {
                'action': 'write',
                'object': 'custom_reports',
            }
        ]
    },
    2: {
        'name': 'Lucas',
        'policies': [
            {
                'action': 'read',
                'object': 'custom_reports',
            }
        ]
    },
}


class PermissionServicer(permission_pb2_grpc.PermissionServicer):
    def GetPolicies(self, request, context):
        print("GetPolicies Request Made:")
        print(request)

        user = users.get(request.user_id)

        if user is None:
            raise grpc.RpcError(grpc.StatusCode.NOT_FOUND, 'User not found')

        policies = [permission_pb2.PolicyReply(**policy) for policy in user['policies']]
        policies = permission_pb2.PoliciesReply(user_id=request.user_id, policies=policies)
        return policies


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    permission_pb2_grpc.add_PermissionServicer_to_server(PermissionServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print('Server started at localhost:50051')
    server.wait_for_termination()


if __name__ == "__main__":
    serve()