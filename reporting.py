# import permissions.permission_pb2_grpc as permission_pb2_grpc
# import permissions.permission_pb2 as permission_pb2
import grpc


import permission_pb2_grpc
import permission_pb2


from utils.input import input_action, input_available_actions, input_object, input_user_id
from enums.actions import Actions


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = permission_pb2_grpc.PermissionStub(channel)

        while True:
            actions = input_available_actions()

            try:
                if actions == Actions.G.name:
                    policy_request = permission_pb2.GetPolicyRequest(user_id=input_user_id())
                    policies_reply = stub.GetPolicies(policy_request)
                    print(f"GetPolicies Response Received: {policies_reply}")
                elif actions == Actions.C.name:
                    policy_request = permission_pb2.CreatePolicyRequest(user_id=input_user_id(), object=input_object(), action=input_action())
                    policies_reply = stub.CreatePolicy(policy_request)
                    print(f"CreatePolicy Response Received: {policies_reply}")
                elif actions == Actions.V.name:
                    check_policy_request = permission_pb2.CheckPolicyRequest(user_id=input_user_id(), object=input_object(), action=input_action())
                    check_policy_reply = stub.CheckPolicy(check_policy_request)
                    print(f"CheckPolicy Response Received: {check_policy_reply}")
                else:
                    print("Please select a valid option!")
                    continue
            except grpc.RpcError as e:
                print(e)
                continue

if __name__ == "__main__":
    run()