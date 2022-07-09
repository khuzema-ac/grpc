import asyncio
import logging
import random
import time

import grpc
from profile_pb2 import Status
from profile_pb2 import Profile
from profile_pb2_grpc import ProfileService
from profile_pb2_grpc import add_ProfileServiceServicer_to_server


class ProfileServer(ProfileService):

    async def saveProfiles(self, request_iterator,
                           context: grpc.aio.ServicerContext) -> Status:
        async for profile in request_iterator:
            logging.info("Saving Profile %s", profile.name)
            yield Status(profile=profile, status='Saved!')
            time.sleep(random.uniform(0.5, 1.0))


async def serve() -> None:
    server = grpc.aio.server()
    add_ProfileServiceServicer_to_server(ProfileServer(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
