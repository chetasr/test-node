from anymesh import AnyMesh, AnyMeshDelegateProtocol, MeshMessage, MeshDeviceInfo
from crochet import setup
import json
setup()

class AmDelegate(AnyMeshDelegateProtocol):
    def connected_to(self, anymesh, device_info):
        pass

    def disconnected_from(self, anymesh, name):
        pass

    def received_msg(self, anymesh, message):
        print message.data.rstrip()


any_mesh = AnyMesh('server', [], AmDelegate())

while True:
    any_mesh.request('node', raw_input('> '))


