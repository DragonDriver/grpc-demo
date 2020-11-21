from concurrent import futures
import grpc

import common_pb2
import common_pb2_grpc
import schema_pb2
import schema_pb2_grpc
import service_pb2
import service_pb2_grpc
import service_msg_pb2
import service_msg_pb2_grpc

class MilvusServer(service_pb2_grpc.MilvusServiceServicer):
    def CreateCollection(self, request, context):
        print('receive create collection request ...')
        status = common_pb2.Status(error_code=0, reason='no')
        print(status)
        return status

    def HasCollection(self, request, context):
        print('receive has collection request ...')
        bool_response = service_msg_pb2.BoolResponse()
        bool_response.status.error_code = 0
        bool_response.value = True
        return bool_response
    
    def Insert(self, request, context):
        print('receive insert request ...')
        integer_range_response = service_msg_pb2.IntegerRangeResponse()
        integer_range_response.status.error_code = 0
        integer_range_response.begin.extend([0])
        integer_range_response.end.extend([0])
        return integer_range_response

    def Search(self, request, context):
        print('receive search request ...')
        query_result = service_msg_pb2.QueryResult()
        query_result.status.error_code = 0
        query_result.hits.extend([service_msg_pb2.Hits()])
        query_result.hits.ids.extend([0])
        query_result.hits.row_data.extend([common_pb2.Blob()])
        query_result.hits.row_data[0].value = bytes('nothing')
        query_result.hits.scores.extend([service_msg_pb2.Score()])
        query_result.hits.scores[0].tag = 'root'
        query_result.hits.scores[0].values.extend([0.9])
        return query_result

def serve():
    print('create server ...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MilvusServiceServicer_to_server(MilvusServer(), server)
    print('add milvus service to server ...')
    server.add_insecure_port('[::]:19530')
    print('listen on port: %d' % (19530))
    server.start()
    print('start server ...')
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
