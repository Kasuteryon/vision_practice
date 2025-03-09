import os
import numpy as np
import pydicom
import matplotlib.pyplot as plt

def load_dicom_series(folder_path):
    dicom_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.dcm', '.dicom'))]
    slices = []
    for f in sorted(dicom_files):
        path = os.path.join(folder_path, f)
        ds = pydicom.dcmread(path)
        slices.append(ds.pixel_array)
    volume = np.stack(slices, axis=0)
    return volume

def save_plane_slices(volume, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Axial
    axial_path = os.path.join(output_folder, 'axial')
    os.makedirs(axial_path, exist_ok=True)
    for i in range(volume.shape[0]):
        plt.imsave(os.path.join(axial_path, f"axial_{i:03d}.png"), volume[i, :, :], cmap='gray')

    # Coronal
    coronal_path = os.path.join(output_folder, 'coronal')
    os.makedirs(coronal_path, exist_ok=True)
    for i in range(volume.shape[1]):
        plt.imsave(os.path.join(coronal_path, f"coronal_{i:03d}.png"), volume[:, i, :], cmap='gray')

    # Sagittal
    sagittal_path = os.path.join(output_folder, 'sagittal')
    os.makedirs(sagittal_path, exist_ok=True)
    for i in range(volume.shape[2]):
        plt.imsave(os.path.join(sagittal_path, f"sagittal_{i:03d}.png"), volume[:, :, i], cmap='gray')

# Ruta a la carpeta con tus archivos .DICOM
dicom_folder = "/Users/macbookpro/Library/CloudStorage/OneDrive-InstitutoPolitecnicoNacional/MRI/1.2.840.113845.11.1000000002170592405.20250120122159.1055983/series19"
output_folder = "/Users/macbookpro/Library/CloudStorage/OneDrive-InstitutoPolitecnicoNacional/MRI/Output Png"

volume = load_dicom_series(dicom_folder)
save_plane_slices(volume, output_folder)

print("Listo: se guardaron los cortes axial, coronal y sagital en formato PNG.")