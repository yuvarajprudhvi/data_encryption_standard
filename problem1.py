
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]


IP_INV = [40, 8, 48, 16, 56, 24, 64, 32,
          39, 7, 47, 15, 55, 23, 63, 31,
          38, 6, 46, 14, 54, 22, 62, 30,
          37, 5, 45, 13, 53, 21, 61, 29,
          36, 4, 44, 12, 52, 20, 60, 28,
          35, 3, 43, 11, 51, 19, 59, 27,
          34, 2, 42, 10, 50, 18, 58, 26,
          33, 1, 41, 9, 49, 17, 57, 25] 


def permute(block, table):
    return ''.join(block[i - 1] for i in table)


def des_encrypt_decrypt(plaintext, key, mode='encrypt'):
   
    permuted = permute(plaintext, IP)
    
    
    L, R = permuted[:32], permuted[32:]
    swapped = R + L  

    
    final = permute(swapped, IP_INV)
    return final


if __name__ == "__main__":  
    plaintext = "0000000100100011010001010110011110001001101010111100110111101111"  
    key = "0001001100110100010101110111100110011011101111001101111111110001"  

    print("Plaintext:", plaintext)


    encrypted = des_encrypt_decrypt(plaintext, key, mode='encrypt')
    print("Encrypted Plaintext:", encrypted)

 
    decrypted = des_encrypt_decrypt(encrypted, key, mode='decrypt')
    print("Decrypted Plaintext:", decrypted)

