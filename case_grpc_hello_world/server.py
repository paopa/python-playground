from concurrent import futures
import grpc
import greeter_pb2
import greeter_pb2_grpc


# Define the server class inheriting from the generated GreeterServicer
class GreeterServicer(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        name = request.name
        message = f"Hello, {name}!"
        return greeter_pb2.HelloReply(message=message)


def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)

    # Listen on port 50051
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051.")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Server stopped.")


if __name__ == "__main__":
    serve()
