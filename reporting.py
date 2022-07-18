import permission_pb2_grpc
import permission_pb2
import grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = permission_pb2_grpc.PermissionStub(channel)

        while True:
            user_id = input("Please enter a user_id (or nothing to stop chatting): ")

            if user_id == "":
                break

            user_id = int(user_id)
            policy_request = permission_pb2.PolicyRequest(user_id=user_id)

            try:
                policies_reply = stub.GetPolicies(policy_request)
                print("GetPolicies Response Received:")
                print(policies_reply)
            except grpc.RpcError as e:
                print(e)
                continue


if __name__ == "__main__":
    run()