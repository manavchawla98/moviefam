# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import recommendation_pb2 as recommendation__pb2


class get_moviesStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.get_movies = channel.unary_unary(
        '/recommendation.get_movies/get_movies',
        request_serializer=recommendation__pb2.movie_request.SerializeToString,
        response_deserializer=recommendation__pb2.movie_response.FromString,
        )


class get_moviesServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def get_movies(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_get_moviesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'get_movies': grpc.unary_unary_rpc_method_handler(
          servicer.get_movies,
          request_deserializer=recommendation__pb2.movie_request.FromString,
          response_serializer=recommendation__pb2.movie_response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'recommendation.get_movies', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))