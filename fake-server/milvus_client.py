# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc

import service_pb2_grpc
import service_msg_pb2
import schema_pb2


def run():
    with grpc.insecure_channel('localhost:19530') as channel:
        # stub = helloworld_pb2_grpc.GreeterStub(channel)
        # response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        stub = service_pb2_grpc.MilvusServiceStub(channel)
        resp = stub.HasCollection(service_msg_pb2.CollectionName(collection_name="test"))
        print(resp)
        if resp.value:
            resp = stub.DropCollection(service_msg_pb2.CollectionName(collection_name="test"))
            print(resp)
        resp = stub.CreateCollection(schema_pb2.CollectionSchema(name="test"))
        print(resp)


if __name__ == '__main__':
    run()
