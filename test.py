from anymesh import AnyMesh, AnyMeshDelegateProtocol, MeshMessage, MeshDeviceInfo
import json
import subprocess

class AmDelegate(AnyMeshDelegateProtocol):
    def connected_to(self, anymesh, device_info):
        pass

    def disconnected_from(self, anymesh, name):
        pass

    def received_msg(self, anymesh, message):
        msg = message.data
        if msg[0] == 'cmd':
            any_mesh.request(message.sender, 'stdout '+subprocess.check_output(msg[4:].split()))

        elif msg[0] == 'msg':
            print msg[4:]
            

any_mesh = AnyMesh(raw_input('node name: '), [], AmDelegate())
any_mesh.run()
