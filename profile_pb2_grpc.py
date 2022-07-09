# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import profile_pb2 as profile__pb2


class ProfileServiceStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.saveProfiles = channel.stream_stream(
                '/profile.ProfileService/saveProfiles',
                request_serializer=profile__pb2.Profile.SerializeToString,
                response_deserializer=profile__pb2.Status.FromString,
                )


class ProfileServiceServicer(object):
    """The greeting service definition.
    """

    def saveProfiles(self, request_iterator, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'saveProfiles': grpc.stream_stream_rpc_method_handler(
                    servicer.saveProfiles,
                    request_deserializer=profile__pb2.Profile.FromString,
                    response_serializer=profile__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'profile.ProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProfileService(object):
    """The greeting service definition.
    """

    @staticmethod
    def saveProfiles(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/profile.ProfileService/saveProfiles',
            profile__pb2.Profile.SerializeToString,
            profile__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
