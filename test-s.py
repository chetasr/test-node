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
        if msg[0] == 'stdout':
            print ' '.join(msg[1:])
        elif msg[0] == 'msg':
            print msg[1:]
        else:
            print 'unhandled: %s' % msg


any_mesh = AnyMesh(raw_input('server name: '), [], AmDelegate())

while True:
    r = raw_input('> ').split()
    print r[1:]
    any_mesh.request(r[0], r[1:])


