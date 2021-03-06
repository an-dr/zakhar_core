from .common import *
from zakhar_core import __version__
# from .common.devices import *

class DeviceUnitTests(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.1.0'

    def setUp(self):
        zk_programs.zk_start()

    def tearDown(self):
        zk_programs.zk_stop()

    def test_motors_commands(self):
        cmds = get_commands(devices.motors)
        for c in cmds:
            name = c[0]
            val = c[1]
            LOGD("CMD: %s - %d" % (name,val))
            devices.motors.dev.cmd(val)
            m = devices.motors.dev.mode()
            LOGD("MODE: %d" % m)
            assert(val == m)

    def test_motors_commands_stress(self):
        for i in range(STRESSTEST_CYCLES):
            self.test_motors_commands()

    def test_face_faces(self):
        cmds = get_commands(devices.face)
        for c in cmds:
            name = c[0]
            val = c[1]
            LOGD("CMD: %s - %d" % (name,val))
            devices.face.dev.cmd(val)
            now = time()
            while 1:
                if (time() > now + 3):
                    assert(False)
                else:
                    m = devices.face.dev.mode()
                    LOGD("MODE: %d" % m)
                    if val == m:
                        break
                    LOGW("MODE: %s (expected: %s)" % (hex(m),hex(val)))
                    sleep(.1) # need time to execute the command

    def test_face_faces_stress(self):
        for i in range(STRESSTEST_CYCLES):
            self.test_face_faces()

    def test_eye_value(self):
        v = devices.eye.dev.get_light()
        print(str(v)+'|', end = '', flush=True)
        assert(v < 0xffff)

    def test_eye_stress(self):
        for i in range(STRESSTEST_CYCLES*10):
            self.test_eye_value()

    def test_test(self):
        LOGD("hello")


    def test_reset(self):
        devices.motors.dev.cmd(devices.CMD_STOP)

if __name__ == "__main__":
    unittest.main()