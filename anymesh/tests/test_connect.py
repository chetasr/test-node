import sys
import unittest
sys.path.append('../../')
from anymesh import AnyMesh, AnyMeshDelegateProtocol
from reactortester import ReactorTestCase

class TestAnyMeshBasic(ReactorTestCase, AnyMeshDelegateProtocol):
    connections = 0

    def connected_to(self, anymesh, device_info):
            print "connection detected!"
            self.connections += 1
            if self.connections == 2:
                self.reactorTestComplete()

    def disconnected_from(self, anymesh, name):
            self.reactorAssert(False, "disconnected from " + name + " no disconnecting in this test!")
    def received_msg(self, anymesh, message):
            pass


    def test_connect(self):
        self.leftMesh = AnyMesh('left', ['stuff', 'things'], self)
        self.rightMesh = AnyMesh('right', ['stuff', 'things'], self)
        AnyMesh.run()



if __name__ == '__main__':
    unittest.main()
