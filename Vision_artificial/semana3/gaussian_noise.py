import numpy as np

def add_gaussian_noise(image, mean=0, sigma=25):

    row, col, ch = image.shape
    # Al estar normalizados van de -1 a +1
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    # np.clip hace que todos los valores negativos los pone en 0 y si hay valores arriba de 255 los va a dejar en 255
    noisy_image = np.clip(image + gauss, 0, 255).astype(np.uint8)
    return noisy_image

def add_salt_and_pepper_noise(image, salt_prob=1, pepper_prob=1):

    row, col, ch = image.shape
    noisy_image = image.copy()

    # Salt (valor máximo)
    num_salt = int(salt_prob * row * col)
    salt_coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1], :] = 255

    # Pepper (valor mínimo)
    num_pepper = int(pepper_prob * row * col)
    pepper_coords = [np.random.randint(0, i-1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1], :] = 0

    return noisy_image