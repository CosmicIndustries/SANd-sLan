import os
import sys
from cryptography.fernet import Fernet

class sLANConnection:
    """
    A simplified implementation of a secure LAN connection.
    Designed for high-speed, low-latency LAN environments with:
    - Secure handshake (zero trust)
    - End-to-end encryption using Fernet
    - Dynamic segmentation for local security policies
    """
    def __init__(self):
        try:
            self.session_key = Fernet.generate_key()
            self.cipher = Fernet(self.session_key)
            self.authenticated = False
            self.segmentation_tag = None
            self.busybox_interface = self.init_busybox_interface()
        except Exception as e:
            print("Initialization Error:", e)
            sys.exit(1)

    def init_busybox_interface(self):
        """
        Initialize an interface to support BusyBox integration.
        """
        return {"integration": True}

    def handshake(self, peer_key: bytes):
        """
        Perform a secure handshake. For simplicity, authentication
        is simulated by ensuring a valid key is provided.
        """
        try:
            if not peer_key:
                raise ValueError("Missing peer key")
            if isinstance(peer_key, bytes):
                self.authenticated = True
                print("sLAN Handshake successful. Peer authenticated.")
            else:
                raise TypeError("Invalid peer key type")
        except Exception as e:
            self.authenticated = False
            print("Handshake failed:", e)
        return self.authenticated

    def encrypt_message(self, message: str) -> bytes:
        """
        Encrypt a message if the connection is authenticated.
        """
        if not self.authenticated:
            raise Exception("Connection not authenticated. Cannot encrypt.")
        if not message:
            raise ValueError("Cannot encrypt an empty message.")
        try:
            return self.cipher.encrypt(message.encode())
        except Exception as e:
            print("Encryption error:", e)
            raise

    def decrypt_message(self, token: bytes) -> str:
        """
        Decrypt a message if the connection is authenticated.
        """
        if not self.authenticated:
            raise Exception("Connection not authenticated. Cannot decrypt.")
        if not token:
            raise ValueError("Empty token provided.")
        try:
            return self.cipher.decrypt(token).decode()
        except Exception as e:
            print("Decryption error:", e)
            raise

    def set_segmentation(self, segment: str):
        """
        Set a segmentation tag to isolate LAN segments.
        """
        if not self.authenticated:
            raise Exception("Connection not authenticated. Cannot set segmentation.")
        if not segment:
            raise ValueError("Segmentation tag cannot be empty.")
        self.segmentation_tag = segment
        print(f"Segmentation set to: {self.segmentation_tag}")

    def send_message(self, message: str, peer_connection):
        """
        Simulate sending an encrypted message to a peer LAN node.
        """
        try:
            encrypted = self.encrypt_message(message)
            print("Sending encrypted message over LAN...")
            return peer_connection.receive_message(encrypted)
        except Exception as e:
            print("Send message failed:", e)
            raise

    def receive_message(self, encrypted_message: bytes) -> str:
        """
        Receive and decrypt an encrypted LAN message.
        """
        try:
            decrypted = self.decrypt_message(encrypted_message)
            print("Message received and decrypted.")
            return decrypted
        except Exception as e:
            print("Receive message failed:", e)
            raise

    def integrate_with_busybox(self):
        """
        Simulate BusyBox integration.
        """
        try:
            result = os.system("echo 'sLAN integrating with BusyBox...'")
            if result != 0:
                raise Exception("BusyBox integration error")
            print("BusyBox integration successful.")
        except Exception as e:
            print("BusyBox integration failed:", e)

if __name__ == "__main__":
    try:
        # Create two sLAN connections to simulate LAN communication.
        lan_node_a = sLANConnection()
        lan_node_b = sLANConnection()
        
        # Simulate key exchange for handshake.
        peer_key_for_b = lan_node_a.session_key
        peer_key_for_a = lan_node_b.session_key
        
        # Perform handshake.
        if not lan_node_a.handshake(peer_key_for_a):
            raise Exception("Node A handshake failed")
        if not lan_node_b.handshake(peer_key_for_b):
            raise Exception("Node B handshake failed")
        
        # Set segmentation tags.
        lan_node_a.set_segmentation("Office_A")
        lan_node_b.set_segmentation("Office_B")
        
        # Demonstrate BusyBox integration.
        lan_node_a.integrate_with_busybox()
        
        # Simulate sending a LAN message.
        received = lan_node_a.send_message("Hello from LAN Node A", lan_node_b)
        print("LAN Node B received:", received)
    
    except Exception as main_e:
        print("Error in sLAN simulation:", main_e)
