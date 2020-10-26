#!/bin/bash

# python -m grpc_tools.protoc -I . --python_out=../fake-server --grpc_python_out=../fake-server status.proto
# python -m grpc_tools.protoc -I . --python_out=../fake-server --grpc_python_out=../fake-server milvus.proto
python -m grpc_tools.protoc -I . --python_out=../fake-server --grpc_python_out=../fake-server common.proto
python -m grpc_tools.protoc -I . --python_out=../fake-server --grpc_python_out=../fake-server schema.proto
python -m grpc_tools.protoc -I . --python_out=../fake-server --grpc_python_out=../fake-server service.proto
python -m grpc_tools.protoc -I . --python_out=../fake-server --grpc_python_out=../fake-server service_msg.proto
