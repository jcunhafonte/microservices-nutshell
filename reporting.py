import permission_pb2_grpc as permission_pb2_grpc
import permission_pb2 as permission_pb2
import grpc


from utils.input import input_action, input_available_actions, input_object, input_user_id


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = permission_pb2_grpc.PermissionStub(channel)

        while True:
            actions = input_available_actions()

            if actions == 'G':
                try:
                    policy_request = permission_pb2.GetPolicyRequest(user_id=input_user_id())
                    policies_reply = stub.GetPolicies(policy_request)
                    print(f"GetPolicies Response Received: {policies_reply}")
                except grpc.RpcError as e:
                    print(e)
                    continue
            elif actions == 'C':
                try:
                    policy_request = permission_pb2.CreatePolicyRequest(user_id=input_user_id(), object=input_object(), action=input_action())
                    policies_reply = stub.CreatePolicy(policy_request)
                    print(f"CreatePolicy Response Received: {policies_reply}")
                except grpc.RpcError as e:
                    print(e)
                    continue
            else:
                print("Please select a valid option!")
                continue


if __name__ == "__main__":
    run()