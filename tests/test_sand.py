import unittest
from src.sand import SANdConnection

class TestSANdConnection(unittest.TestCase):
    def setUp(self):
        self.conn_a = SANdConnection()
        self.conn_b = SANdConnection()
        self.conn_a.handshake(self.conn_b.session_key)
        self.conn_b.handshake(self.conn_a.session_key)
        self.conn_a.set_segmentation("Test_Segment_A")
        self.conn_b.set_segmentation("Test_Segment_B")

    def test_encryption_decryption(self):
        original_message = "Test message"
        encrypted_message = self.conn_a.encrypt_message(original_message)
        decrypted_message = self.conn_a.decrypt_message(encrypted_message)
        self.assertEqual(original_message, decrypted_message)

    def test_message_send_receive(self):
        message = "Hello from test"
        received_message = self.conn_a.send_message(message, self.conn_b)
        self.assertEqual(message, received_message)

if __name__ == '__main__':
    unittest.main()
