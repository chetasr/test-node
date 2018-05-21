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
        msg = message.data
        if msg.startswith('stdout'):
            print message.data[7:].rstrip()
        elif msg.startswith('msg'):
            print msg[4:]
        else:
            print 'unhandled: %s' % msg


any_mesh = AnyMesh(raw_input('server name: '), [], AmDelegate())

while True:
    r = raw_input('> ').split()
    any_mesh.request(r[0], r[1:])


