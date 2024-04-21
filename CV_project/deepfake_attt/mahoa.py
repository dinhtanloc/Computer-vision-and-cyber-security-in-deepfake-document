from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Mã hóa hình ảnh
def encrypt_image(input_path, output_path, key):
    try:
        print('The path of file : ', input_path)
        print('Key for encryption : ', key)
        
        with open(input_path, 'rb') as fin:
            image_data = fin.read()
        
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_image_data = cipher.encrypt(pad(image_data, AES.block_size))
        
        with open(output_path, 'wb') as fout:
            fout.write(encrypted_image_data)
        
        print('Encryption Done...')
        return encrypted_image_data
    
    except Exception as e:
        print('Error caught : ', e)



# Giải mã hình ảnh
def decrypt_image(input_path, output_path, key):
    try:
        print('The path of file : ', input_path)
        print('Key for Decryption : ', key)
        
        with open(input_path, 'rb') as fin:
            encrypted_image_data = fin.read()
        
        cipher = AES.new(key, AES.MODE_CBC)
        decrypted_image_data = cipher.decrypt(encrypted_image_data)
        
        with open(output_path, 'wb') as fout:
            fout.write(decrypted_image_data)
        
        print('Decryption Done...')
        return decrypted_image_data
        
    except Exception as e:
        print('Error caught : ', e)

# Tạo khóa ngẫu nhiên
key = b"&\xd8\x92\xbb\xee`\x15\x1eeI\\\xbf\xbdB\xca\xc0\xd7\xf0z\xa9V\xe7\xc9u''H\x08\x95R\xa0*"

# Đường dẫn đến hình ảnh gốc
original_image_path = "image/vuong-quoc-anh.jpg"

# Đường dẫn đến hình ảnh sau khi mã hóa
encrypted_image_path = "image/vuong-quoc-anh_encrypted.jpg"

# Đường dẫn đến hình ảnh sau khi giải mã
decrypted_image_path = "image/vuong-quoc-anh_decrypted.jpg"

# Mã hóa hình ảnh
# encrypt_image(original_image_path, encrypted_image_path, key)

# Giải mã hình ảnh
# decrypt_image(encrypted_image_path, decrypted_image_path, key)

# Hàm để kiểm tra xem hai chuỗi byte có giống nhau không
def compare_bytes(byte_str1, byte_str2):
    if len(byte_str1) != len(byte_str2):
        return False
    
    for b1, b2 in zip(byte_str1, byte_str2):
        if b1 != b2:
            return False
    
    return True

# ... [Phần mã của bạn]

# Đọc dữ liệu hình ảnh gốc trước khi mã hóa
with open(original_image_path, 'rb') as fin:
    original_data = fin.read()

# Mã hóa hình ảnh
encrypt_image(original_image_path, encrypted_image_path, key)

# Giải mã hình ảnh
decrypt_image(encrypted_image_path, decrypted_image_path, key)

# Đọc dữ liệu sau khi giải mã
with open(decrypted_image_path, 'rb') as fin:
    decrypted_data = fin.read()

# So sánh dữ liệu trước và sau khi giải mã
if original_data == decrypted_data:
    print("Decryption successful! The decrypted data matches the original data.")
else:
    print("Decryption failed! The decrypted data does not match the original data.")


# print(f'so sanh {compare_bytes()}')
