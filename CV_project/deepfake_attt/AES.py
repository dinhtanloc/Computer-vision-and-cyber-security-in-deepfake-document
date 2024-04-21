from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt_text(text, key):
    # Chuyển chuỗi key thành bytes
    key = bytes(key, 'utf-8')
    
    # Khởi tạo AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Mã hóa chuỗi văn bản
    encrypted_bytes = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    
    # Chuyển dữ liệu mã hóa sang dạng Base64 để lưu trữ hoặc truyền đi
    encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    return encrypted_text

def decrypt_text(encrypted_text, key):
    # Chuyển chuỗi key thành bytes
    key = bytes(key, 'utf-8')
    
    # Khởi tạo AES cipher
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Giải mã dữ liệu từ dạng Base64
    encrypted_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
    
    # Giải mã dữ liệu
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    
    # Chuyển bytes giải mã thành chuỗi văn bản
    decrypted_text = decrypted_bytes.decode('utf-8')
    
    return decrypted_text

# Chuỗi văn bản cần mã hóa
text = "Hello, AES!"

# Tạo một khóa ngẫu nhiên (độ dài 16 ký tự để phù hợp với AES-128)
key = get_random_bytes(16)

# Mã hóa chuỗi văn bản
encrypted_text = encrypt_text(text, key)
print(f"Encrypted text: {encrypted_text}")

# Giải mã chuỗi văn bản
decrypted_text = decrypt_text(encrypted_text, key)
print(f"Decrypted text: {decrypted_text}")
