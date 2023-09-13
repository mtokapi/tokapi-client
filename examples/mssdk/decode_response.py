from client.api import TokApi
from client.proto import mssdk_pb2
from examples.constants import API_KEY, BASE_URL


def example(mssdk_response: str):
    client = TokApi(API_KEY, base_url=BASE_URL)

    res = mssdk_pb2.MssdkResponse()
    res.ParseFromString(bytes.fromhex(mssdk_response))

    decode_response = client.mssdk_decode(res.body.hex(), mode='full')

    print('To decode protobuf message you can use https://protobuf-decoder.netlify.app/')
    print(f'Decode result: {decode_response.json()}')


if __name__ == "__main__":
    example('08a48c9081041002280232408fa0f8cd7812e2be6547aa8e3a22627d68c25f4890859ce7988145f4bd896d812cef7b24faf8ab224c7991bba07077a5310de071209f1999f585830fa952d598')
