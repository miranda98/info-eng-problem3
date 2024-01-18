#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
=======
Created on Thu Feb  3 00:59:47 2022

@author: m.benammar
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
>>>>>>> 18ecf78e2bb2172fe877d4ca7bfd7fa17621cb43
Created on Tue Feb  1 11:09:50 2022

@author: m.benammar
"""
 

from matplotlib import pyplot   as plt
import numpy as np 
from PIL import Image as im   

<<<<<<< HEAD
def LFSR(N: int, c: np.array, seed: np.array):
    """
    LFSR is iteratively updated to generate a pseudo-random sequence of bits
    
    Args:
        N (int): length of the output sequence
        c (np.array): connections vector
        seed (np.array): initial state

    Returns:
        np.array: pseudo-random sequence of bits, used to encrypt the binary representation of the image 
    """
    LFSR_output: np.array = np.zeros(N)
=======
def LFSR(N,c,seed): 
    LFSR_output = np.zeros(N)
>>>>>>> 18ecf78e2bb2172fe877d4ca7bfd7fa17621cb43
    m = np.size(c)
    state = seed  
    for i in range(0,N): 
        next_bit = np.mod(np.sum(c*state),2)
        LFSR_output[i] = state[m-1]
        state = np.concatenate( (np.array([next_bit]) , state[0:m-1]))
    return LFSR_output  

<<<<<<< HEAD
c = np.array([1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1]) # connections vector - defines the feedback connections for the LFSR
seed = np.array([1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1]) # initial state   
=======
c = np.array([1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1]) # connections vector
seed = np.array([1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,1]) #initial state   
>>>>>>> 18ecf78e2bb2172fe877d4ca7bfd7fa17621cb43

# ***************************************************************************** 
#        Transmitter: Compression  + encryption  
# ***************************************************************************** 
  

# Open the image 
img = im.open("ISAE_Logo_SEIS_clr_new.png") 
img_eval= np.array(img) 
image_trunc = img_eval 
# pyplot.imshow(image_trunc) 

# Initializations 
image_rec_plane = np.zeros((200,200,3),dtype=np.uint8)
image_binary_plane = np.zeros((200*200*8,3))

#---------- Compression (trivial) --------------------
for i_plane in range(0,3): 
    
    # Select a plane  Y, Cb, or Cr 
    image_plane = image_trunc[:,:,i_plane]
   
    # Image to binary
    ctr = 0
    for i in range(0,np.size(image_plane,0)):
        for j in range(0, np.size(image_plane,1)):
            image_binary_plane[ctr:ctr+8,i_plane] =  np.unpackbits(image_plane[i,j]) 
            ctr += 8 
image_binary= np.reshape(image_binary_plane, (1,200*200*8*3))  
        
#------------- Encryption: stream cipher  --------------

# Create the stream cipher 
stream_cipher = LFSR(np.size(image_binary), c,seed) 
    
<<<<<<< HEAD
# Encrypt using the stream cipher using bitwise addition modulo 2
=======
# Encrypt using the stream cipher   
>>>>>>> 18ecf78e2bb2172fe877d4ca7bfd7fa17621cb43
image_binary_crypt = np.mod(image_binary+stream_cipher,2)

# ***************************************************************************** 
#            Receiver:  decryption + decompression
# *****************************************************************************  

# ---------------- Decryption: stream cipher -----------

# Recover the stream cipher 
stream_cipher_rec = stream_cipher

# Decrypt using the stream cipher 
image_binary_decrypt = np.mod(image_binary_crypt+0*stream_cipher_rec,2) 

# --------------- Decompression --------------------

# From binary to image
image_binary_decrypt_plane = np.reshape(image_binary_decrypt, (200*200*8,3)) 
for i_plane in range(0,3):     
    ctr = 0
    for i in range(0,np.size(image_plane,0)):
        for j in range(0, np.size(image_plane,1)):
            image_rec_plane[i,j,i_plane] = (np.sum(image_binary_decrypt_plane[ctr:ctr+8,i_plane]*np.array([128,64,32,16,8,4,2,1]))) 
            ctr += 8

# Recovering the image from the array of YCbCr
image_rec = im.fromarray(image_rec_plane) 
<<<<<<< HEAD

# Plot the image 
plt.imshow(image_rec) 
plt.show()
=======
# Plot the image 
plt.imshow(image_rec) 
 
>>>>>>> 18ecf78e2bb2172fe877d4ca7bfd7fa17621cb43
