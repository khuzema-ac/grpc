import asyncio
import logging
import random
import time

import grpc
import profile_pb2
import profile_pb2_grpc
from faker import Faker


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = profile_pb2_grpc.ProfileServiceStub(channel)
        # Read from an async generator
        async for response in stub.saveProfiles(generate_profiles()):
            logging.info("Recieved Profile %s %s",
                         response.profile.name, response.status)


def generate_profiles():
    for i in range(0, 100):
        fake = Faker()
        profile = profile_pb2.Profile(name=fake.profile()['name'], company=fake.profile()['company'], ssn=fake.profile()[
            'ssn'], address=fake.profile()['address'], mail=fake.profile()['mail'])
        yield profile
        logging.info("Sent Profile %s", profile.name)
        time.sleep(random.uniform(0.1, .5))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(run())
