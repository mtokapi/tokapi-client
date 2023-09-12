from client.api import TokApi
from client.proto import mssdk_pb2


def example(mssdk_request: str):
    client = TokApi('863efd5fc8184c34be21f95fa0b87e63', base_url='https://api.tokapi.online')

    req = mssdk_pb2.MssdkRequest()
    req.ParseFromString(bytes.fromhex(mssdk_request))

    decode_response = client.mssdk_decode(req.encrypted_payload.hex(), mode='full')

    print('To decode protobuf message you can use https://protobuf-decoder.netlify.app/')
    print(f'Decode result: {decode_response.json()}')


if __name__ == "__main__":
    example('08c4908082041002180422709e16d0f374e56b2a1c58c623e60698d0bd2789f75aea121c62500c9fd6053f99cf5d05e647037dc10c0f1cf4b198fe9846532be4716a5b3390963ba5ba521dd1a646b6ec6a7300d5e7897a8fe4c82c713204cfe8a461c80c868f1a3c198525a97b62f87768165236f8cba3a2f07ba8ec2892efb4f99762')
