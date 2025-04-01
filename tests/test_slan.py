import unittest
from src.slan import sLANConnection

class TestsLANConnection(unittest.TestCase):
    def setUp(self):
        self.node_a = sLANConnection()
        self.node_b = sLANConnection()
        self.node_a.handshake(self.node_b.session_key)
        self.node_b.handshake(self.node_a.session_key)
        self.node_a.set_segmentation("Test_Segment_A")
        self.node_b.set_segmentation("Test_Segment_B")

    def test_encryption_decryption(self):
        original_message = "Test LAN message"
        encrypted = self.node_a.encrypt_message(original_message)
        decrypted = self.node_a.decrypt_message(encrypted)
        self.assertEqual(original_message, decrypted)

    def test_message_transfer(self):
        message = "Hello from sLAN test"
        received = self.node_a.send_message(message, self.node_b)
        self.assertEqual(message, received)

if __name__ == '__main__':
    unittest.main()
