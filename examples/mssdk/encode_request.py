import time

from client.api import TokApi
from client.proto import mssdk_pb2


def example(mssdk_request_payload: str, payload_type: str):
    client = TokApi('863efd5fc8184c34be21f95fa0b87e63', base_url='https://api.tokapi.online')

    req = mssdk_pb2.MssdkRequest()
    req.u1 = 1077938244
    req.u2 = 2
    req.u3 = 2
    req.encrypted_payload = bytes.fromhex(client.mssdk_encode(mssdk_request_payload, payload_type).json())
    req.current_time_in_ms = int(time.time() * 1000)

    print('To decode protobuf message you can use https://protobuf-decoder.netlify.app/')
    print(f'Full mssdk request: {req.SerializeToString().hex()}')


if __name__ == "__main__":
    example('0a96050a08216e6f74736574211205594159474f1a074154562d3130312208216e6f74736574212a07416e64726f6964320231313a083736382a313138344080054a22414c353138362d73656c656e652d6275696c642d3230323230383135313535363431508ef4cfaf0c5a05656e5f4742620f4575726f70652f4c6f6e646f6e2c316846704478fef7e3e23f800180c0c4b7a8078801c0fbfbecf6019001a6b786dbdf029a0108216e6f7473657421a20108216e6f7473657421aa011034376265653437333133633635613966b20108216e6f7473657421ba0108216e6f7473657421c2012c51784f62686e74734d62387a53546e4d57414e4d4d4d326545436879635a6b35597955644f306768752f673dc80186f8c1cf0cd2012430316632353666652d633962662d346134342d626464612d623139663835646666346536d8018080f8dbed16e20108216e6f7473657421e801fd887af001fd887afa0108216e6f747365742182020a313639343531313036318a020d3139322e3136382e312e313936920208216e6f74736574219a0208216e6f7473657421a002d403a80232b20208216e6f7473657421ba0208216e6f7473657421c202155b22382e382e382e38222c22312e312e312e31225dc802fd887ad002fd887ae20208216e6f7473657421e8029eb5f6cf0cf00286becccf0cfa025f2f646174612f6170702f7e7e383668683943554d5353317a7441356f6266684a74773d3d2f636f6d2e7a68696c69616f6170702e6d75736963616c6c792d74535334364277546a5659376c6d52507258776f5a673d3d2f626173652e61706b80033c8803fd887a920308216e6f74736574219803fd887aa003fd887aaa0308216e6f7473657421b20308216e6f7473657421ba0308216e6f7473657421c003fd887a1a07616e64726f6964221c7630342e30342e30302d616c7068612e322d6f762d616e64726f696428c080a0403204313233333a0632362e342e354213373237373438353131393236363134353832344a103030303030303030303030303030303058fd887a622438353262643562382d383732612d346338642d396531392d6663376133646262373530618001fd887a',
            'sdi/get_token')