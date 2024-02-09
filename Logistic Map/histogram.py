import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def logistic_map(x, r):
    return r * x * (1 - x)

# function to perform chaotic encryption
def chaotic_encrypt(img_array, key):
    # set initial conditions
    x, y, z = key
    for i in range(100):
        x = logistic_map(x, 3.8)
        y = logistic_map(y, 3.9)
        z = logistic_map(z, 4.0)

    # perform encryption
    encrypted_img = np.zeros_like(img_array)
    rows, cols, channels = img_array.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                x = logistic_map(x, 3.8)
                y = logistic_map(y, 3.9)
                z = logistic_map(z, 4.0)
                r = int(round(logistic_map(x, 3.7) * 10000)) % 256
                encrypted_img[i, j, k] = img_array[i, j, k] ^ r
                key[k] = x

    return encrypted_img, key


# function to perform chaotic decryption
# function to perform chaotic decryption
def chaotic_decrypt(img_array, key):
    # set initial conditions
    x, y, z = key
    for i in range(100):
        x = logistic_map(x, 3.8)
        y = logistic_map(y, 3.9)
        z = logistic_map(z, 4.0)

    # perform decryption
    decrypted_img = np.zeros_like(img_array)
    rows, cols, channels = img_array.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(channels):
                x = logistic_map(x, 3.8)
                y = logistic_map(y, 3.9)
                z = logistic_map(z, 4.0)
                r = int(round(logistic_map(x, 3.7) * 1000)) % 256
                decrypted_img[i, j, k] = img_array[i, j, k] ^ r
                key[k] = x

    return decrypted_img


# read image
img = Image.open('Lenna.png')
img_array = np.array(img)
rows, cols, channels = img_array.shape
key = np.array([0.1, 0.2, 0.3])

# encrypt image
encrypted_img, key_enc = chaotic_encrypt(img_array, key.copy())

decrypted_img = chaotic_decrypt(encrypted_img, key.copy())


# calculate NPCR and UACI
N_diff = np.sum(encrypted_img != img_array)
N_rows, N_cols, N_channels = img_array.shape
NPCR = (N_diff / (N_rows * N_cols * N_channels)) * 100


# calculate correlation coefficient
mu_p = np.mean(img_array)
mu_d = np.mean(decrypted_img)
sigma_p = np.std(img_array)
sigma_d = np.std(decrypted_img)

CC = np.sum((img_array - mu_p) * (decrypted_img - mu_d)) / ((N_rows * N_cols * N_channels - 1) * sigma_p * sigma_d)

print("NPCR: {:.2f}%".format(NPCR))

print("Correlation coefficient: {:.4f}".format(CC))

flat_arr = encrypted_img.flatten()

# Compute the frequency of each pixel value
hist, bin_edges = np.histogram(flat_arr, bins=256)

# Normalize the histogram to prevent zero or negative values in probability array
hist = hist / np.sum(hist + 1e-10)

# Calculate the probability of each pixel value
prob = hist / np.sum(hist)

# Compute the entropy
entropy = -np.sum(prob * np.log2(prob + 1e-10))
print("Entropy of encrypted image:", entropy)

fig, axs = plt.subplots(3, 5, figsize=(15,7))
fig.subplots_adjust(hspace= 0.7 , wspace=0.5) 

axs[0,0].imshow(img_array)
axs[0,0].set_title('Plain Image',fontsize=10,loc='center', pad=10)

colors = ['Red', 'Green', 'Blue']

for i in range(channels):
    
    axs[0,i+2].hist(img_array[:,:,i].ravel(), 256, color=colors[i])
    axs[0,i+2].set_xlim([0,255])
    axs[0,i+2].set_title(f"{colors[i]} Histogram of Plain Image",fontsize=9,loc='center', pad=10)
    axs[0,i+2].spines['top'].set_visible(False)
    axs[0,i+2].spines['right'].set_visible(False)
    axs[0,i+2].set_xlabel('Pixel Values')
    axs[0,i+2].set_ylabel('Frequency')

    
    axs[1,i+2].hist(encrypted_img[:,:,i].ravel(), 256, color=colors[i])
    axs[1,i+2].set_xlim([0,255])
    axs[1,i+2].set_title(f"{colors[i]} Histogram of Encrypted Image",fontsize=9,loc='center', pad=10)
    axs[1,i+2].spines['top'].set_visible(False)
    axs[1,i+2].spines['right'].set_visible(False)
    axs[1,i+2].set_xlabel('Pixel Values')
    axs[1,i+2].set_ylabel('Frequency')

       
    axs[2,i+2].hist(decrypted_img[:,:,i].ravel(), 256, color=colors[i])
    axs[2,i+2].set_xlim([0,255])
    axs[2,i+2].set_title(f"{colors[i]} Histogram of Decrypted Image",fontsize=9,loc='center', pad=10)
    axs[2,i+2].spines['top'].set_visible(False)
    axs[2,i+2].spines['right'].set_visible(False)
    axs[2,i+2].set_xlabel('Pixel Values')
    axs[2,i+2].set_ylabel('Frequency')


histograms = []
for i in range(channels):
    histogram, _ = np.histogram(img_array[:,:,i], bins=256, range=(0,255))
    histograms.append(histogram)

encrypted_histograms = []
for i in range(channels):
    histogram, _ = np.histogram(encrypted_img[:,:,i], bins=256, range=(0,255))
    encrypted_histograms.append(histogram)

decrypted_histograms = []
for i in range(channels):
    histogram, _ = np.histogram(decrypted_img[:,:,i], bins=256, range=(0,255))
    decrypted_histograms.append(histogram)

axs[1,0].imshow(encrypted_img)
axs[1,0].set_title('Encrypted Image',fontsize=9, loc='center', pad=10)
axs[0,1].bar(range(256), histograms[0], color='red')
axs[0,1].bar(range(256), histograms[1], color='green')
axs[0,1].bar(range(256), histograms[2], color='blue')
axs[0,1].set_xlim([0, 255])
axs[0,1].set_title('Histogram of Plain Image',fontsize=9,loc='center', pad=10)
axs[0,1].spines['top'].set_visible(False)
axs[0,1].spines['right'].set_visible(False)
axs[0,1].spines['left'].set_position('zero')
axs[0,1].spines['bottom'].set_position('zero')

axs[1,1].bar(range(256), encrypted_histograms[0], color='red')
axs[1,1].bar(range(256), encrypted_histograms[1], color='green')
axs[1,1].bar(range(256), encrypted_histograms[2], color='blue')
axs[1,1].set_xlim([0, 255])
axs[1,1].set_title('Histogram of Encrypted Image',fontsize=9,loc='center', pad=10)
axs[1,1].spines['top'].set_visible(False)
axs[1,1].spines['right'].set_visible(False)
axs[1,1].spines['left'].set_position('zero')
axs[1,1].spines['bottom'].set_position('zero')

axs[2,0].imshow(decrypted_img)
axs[2,0].set_title('Decrypted Image',fontsize=9, loc='center', pad=10)

axs[2,1].bar(range(256), decrypted_histograms[0], color='red')
axs[2,1].bar(range(256), decrypted_histograms[1], color='green')
axs[2,1].bar(range(256), decrypted_histograms[2], color='blue')
axs[2,1].set_xlim([0, 255])
axs[2,1].set_title('Histogram of Decrypted Image',fontsize=9,loc='center', pad=10)
axs[2,1].spines['top'].set_visible(False)
axs[2,1].spines['right'].set_visible(False)
axs[2,1].spines['left'].set_position('zero')
axs[2,1].spines['bottom'].set_position('zero')


plt.show()
