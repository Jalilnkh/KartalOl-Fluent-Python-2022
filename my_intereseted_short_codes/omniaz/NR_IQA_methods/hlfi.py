import cv2
import numpy as np

def hlfi(image_path):
    # Read the image and convert to grayscale
    img = cv2.imread(image_path, 0)
    # Compute the 2D Fourier Transform of the image
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = np.abs(fshift)

    # Get image dimensions
    N, M = magnitude_spectrum.shape

    # Define lower and upper frequency thresholds
    i_l = i_h = int(0.15 * N)
    j_l = j_h = int(0.15 * M)

    # Compute sums of the magnitudes for lower, upper, and total frequencies
    lower_freq_sum = np.sum(magnitude_spectrum[:i_l, :j_l])
    upper_freq_sum = np.sum(magnitude_spectrum[i_h:, j_h:])
    total_freq_sum = np.sum(magnitude_spectrum)

    # Compute the High-Low Frequency Index (HLFI)
    HLFI = (lower_freq_sum - upper_freq_sum) / total_freq_sum

    return HLFI


if __name__ == "__main__":
    # Usage example:
    hlfi_value = hlfi('img2.jpeg')
    print('HLFI value:', hlfi_value)
