# open hdf file
from pyhdf.SD import *
import numpy as np
from scipy.interpolate import interp1d
import os

# 1 dimension size 
def spline_interp1(arr_origin, old_file):
    x = old_file.select("wave").get()
    x_new = [485.0, 569.0, 660.0, 840.0, 1676.0, 2223.0]
    arr1 = np.zeros((1,6))   
    y = arr_origin
    f = interp1d(x, y, kind="quadratic", fill_value = "extrapolate", axis = 0)
    y_new = f(x_new)
    arr1 =  y_new
    
    arr2 = arr1.astype("float32") 
    return arr2

# 2 dimension size
def spline_interp2(arr_origin, old_file):
    x = old_file.select("wave").get()
    x_new = [485.0, 569.0, 660.0, 840.0, 1676.0, 2223.0]
    arr1 = np.zeros((6, 14))
    y = arr_origin
    f = interp1d(x, y, kind="quadratic", fill_value = "extrapolate", axis = 0)
    y_new = f(x_new)
    arr1 = y_new
    
    arr2 = arr1.astype("float32") 
    return arr2

# 4 dimension size
def spline_interp4(arr_origin, old_file):
    x = old_file.select("wave").get()
    x_new = [485.0, 569.0, 660.0, 840.0, 1676.0, 2223.0]
    arr1 = np.zeros((6, 14, 16, 14))
    for i in range(arr_origin.shape[1]):
        for j in range(arr_origin.shape[2]):
            y = arr_origin[:, i, j, :]
            f = interp1d(x, y, kind="quadratic", fill_value = "extrapolate", axis = 0)
            y_new = f(x_new)
            arr1[:,i,j,:] = y_new
    
    arr2 = arr1.astype("float32") 
    return arr2

def interp_aerosol(file_name):
    
    folder_path = "G:\\Users\\Lenovo\\Desktop\\zd22\\zd22\\"
    file_path = folder_path + file_name
    output_path = "G:\\Users\\Lenovo\\Desktop\\zd22\\zd22_l5tm\\"
    output_name = file_name.replace("modisa","l5tm")
    output_file_path = output_path + output_name
    
    file = SD(file_path, SDC.READ)
    new_file = SD(output_file_path, SDC.WRITE | SDC.CREATE)
    attributes = file. attributes()
    print(attributes)

    # dataset
    old_phi = file.select("phi")
    old_senz = file.select("senz")
    old_solz = file.select("solz")
    old_scatt = file.select("scatt")
    old_dtran_theta = file.select("dtran_theta")
    old_acost = file.select("acost") # 4 dimension
    old_bcost = file.select("bcost") # 4 dimension
    old_ccost = file.select("ccost") # 4 dimension
    old_albedo = file.select("albedo")
    old_extc = file.select("extc")
    old_angstrom = file.select("angstrom")
    old_phase = file.select("phase") # 2 dimension
    old_dtran_a = file.select("dtran_a") # 2 dimension
    old_dtran_b = file.select("dtran_b") # 2 dimension 
    old_dtran_a0 = file.select("dtran_a0") # 2 dimension
    old_dtran_b0= file.select("dtran_b0") # 2 dimension


    attrs = {
        'Title': 'Aerosol Model Data for l5tm',
        'Model Name': 'm4.0',
        'Version': '01',
        'Number of Wavelengths': 6,
        'SizeDistribution': 24,
        'Number of Scattering Angles': 75,
        'Number of Solar Zenith Angles': 14,
        'Number of View Zenith Angles': 14,
        'Number of Relative Azimuth Angles': 16,
        'Number of Diffuse Transmittance Wavelengths': 6,
        'Number of Diffuse Transmittance Zenith Angles': 14,
        'Creation Date': "Thu Mar 02 16:14:00 2023",
        'Created By': "lvjn using Zhao Dan's model interpolation to get"
    }

    for attr_name, attr_value in attrs.items():
        setattr(new_file, attr_name, attr_value)

    # get new dataset
    phi = new_file.create('phi', SDC.FLOAT32, 16)
    senz = new_file.create('senz', SDC.FLOAT32, 14)
    solz = new_file.create('solz', SDC.FLOAT32, 14)
    scatt = new_file.create('scatt', SDC.FLOAT32, 75)
    dtran_theta = new_file.create('dtran_theta', SDC.FLOAT32, 14)
    dtran_wave = new_file.create('dtran_wave', SDC.FLOAT32, 6)
    wave = new_file.create('wave', SDC.FLOAT32, 6)
    acost = new_file.create('acost', SDC.FLOAT32, (6, 14, 16, 14))
    bcost = new_file.create('bcost', SDC.FLOAT32, (6, 14, 16, 14))
    ccost = new_file.create('ccost', SDC.FLOAT32, (6, 14, 16, 14))
    albedo = new_file.create('albedo', SDC.FLOAT32, 6)
    extc = new_file.create('extc', SDC.FLOAT32, 6)
    angstrom = new_file.create('angstrom', SDC.FLOAT32, 6)
    phase = new_file.create('phase', SDC.FLOAT32, (6, 75))
    dtran_a = new_file.create('dtran_a', SDC.FLOAT32, (6, 14))
    dtran_b = new_file.create('dtran_b', SDC.FLOAT32, (6, 14))
    dtran_a0 = new_file.create('dtran_a0', SDC.FLOAT32, (6, 14))
    dtran_b0 = new_file.create('dtran_b0', SDC.FLOAT32, (6, 14))

    phi[:] = old_phi.get()
    senz[:] = old_senz.get()
    solz[:] = old_solz.get()
    scatt[:] = old_scatt.get()
    dtran_theta[:] = old_dtran_theta.get()
    dtran_wave[:] = [485.0, 569.0, 660.0, 840.0, 1676.0, 2223.0]
    wave[:] = [485.0, 569.0, 660.0, 840.0, 1676.0, 2223.0]
    arr = np.array(old_acost.get())
    acost[:,:,:,:] = spline_interp4(arr, file)
    arr = np.array(old_bcost.get())
    bcost[:,:,:,:] = spline_interp4(arr, file)
    arr = np.array(old_ccost.get())
    ccost[:,:,:,:] = spline_interp4(arr, file)
    arr = np.array(old_albedo.get())
    albedo[:] = spline_interp1(arr, file)
    arr = np.array(old_extc.get())
    extc[:] = spline_interp1(arr, file)
    arr = np.array(old_angstrom.get())
    angstrom[:] = spline_interp1(arr, file)
    arr = np.array(old_phase.get())
    phase[:,:] = spline_interp2(arr, file)
    arr = np.array(old_dtran_a.get())
    dtran_a[:,:] = spline_interp2(arr, file)
    arr = np.array(old_dtran_b.get())
    dtran_b[:,:] = spline_interp2(arr, file)
    arr = np.array(old_dtran_a0.get())
    dtran_a0[:,:] = spline_interp2(arr, file)
    arr = np.array(old_dtran_b0.get())
    dtran_b0[:,:] = spline_interp2(arr, file)

    # set dataset attributes
    phi.long_name = "relative azimuth angles"
    phi.units = "degress"
    senz.long_name = "sensor view zenith angles"
    senz.units = "degress"
    solz.long_name = "solar zenith angles"
    solz.units = "degress"
    scatt.long_name = "scattering angles"
    scatt.units = "degress"
    dtran_theta.long_name = "zenith angles of diffuse transmittance coeffs"
    dtran_theta.unit = "degress"
    dtran_wave.long_name = "wavelengths of diffuse transmittance coeffs"
    dtran_wave.unit = "degress"
    wave.long_name = "wavelengths"
    wave.unit = "degress"
    acost.long_name = "1st quadratic coefficient of SS to MS function"
    acost.unit = "dimensionless"
    bcost.long_name = "2nd quadratic coefficient of SS to MS function"
    bcost.unit = "dimensionless"
    ccost.long_name = "3rd quadratic coefficient of SS to MS function"
    ccost.unit = "dimensionless"
    albedo.long_name = "single scattering albedo"
    albedo.units = "dimensionless"
    extc.long_name = "extinction coefficient"
    extc.units = "dimensionless"
    angstrom.long_name = "angstrom coefficient"
    angstrom.units = "dimensionless"
    phase.long_name = "volume scattering function"
    phase.units = "dimensionless"
    dtran_a.long_name = "a coefficient of diffuse sensor transmittance"
    dtran_a.units = "dimensionless"
    dtran_b.long_name = "b coefficient of diffuse sensor transmittance"
    dtran_b.units = "dimensionless"
    dtran_a0.long_name = "a coefficient of diffuse solar transmittance"
    dtran_a0.units = "dimensionless"
    dtran_b0.long_name = "b coefficient of diffuse solar transmittance"
    dtran_b0.units = "dimensionless"

    # set dimension attributes
    dim1 = phi.dim(0)
    dim1.setname("nphi")
    dim1 = senz.dim(0)
    dim1.setname("nsenz")
    dim1 = solz.dim(0)
    dim1.setname("nsolz")
    dim1 = scatt.dim(0)
    dim1.setname("nscatt")
    dim1 = dtran_theta.dim(0)
    dim1.setname("dtran_ntheta")
    dim1 = dtran_wave.dim(0)
    dim1.setname("dtran_nwave")
    dim1 = wave.dim(0)
    dim1.setname("nwave")

    dim1 = acost.dim(0)
    dim2 = acost.dim(1)
    dim3 = acost.dim(2)
    dim4 = acost.dim(3)
    dim1.setname("nwave")
    dim2.setname("nsolz")
    dim3.setname("nphi")
    dim4.setname("nsenz")
    dim1 = bcost.dim(0)
    dim2 = bcost.dim(1)
    dim3 = bcost.dim(2)
    dim4 = bcost.dim(3)
    dim1.setname("nwave")
    dim2.setname("nsolz")
    dim3.setname("nphi")
    dim4.setname("nsenz")
    dim1 = ccost.dim(0)
    dim2 = ccost.dim(1)
    dim3 = ccost.dim(2)
    dim4 = ccost.dim(3)
    dim1.setname("nwave")
    dim2.setname("nsolz")
    dim3.setname("nphi")
    dim4.setname("nsenz")

    dim1 = albedo.dim(0)
    dim1.setname("nwave")
    dim1 = extc.dim(0)
    dim1.setname("nwave")
    dim1 = angstrom.dim(0)
    dim1.setname("nwave")
    dim1 = phase.dim(0)
    dim2 = phase.dim(1)
    dim1.setname("nwave")
    dim2.setname("nscatt")
    dim1 = dtran_a.dim(0)
    dim2 = dtran_a.dim(1)
    dim1.setname("dtran_nwave")
    dim2.setname("dtran_ntheta")
    dim1 = dtran_b.dim(0)
    dim2 = dtran_b.dim(1)
    dim1.setname("dtran_nwave")
    dim2.setname("dtran_ntheta")
    dim1 = dtran_a0.dim(0)
    dim2 = dtran_a0.dim(1)
    dim1.setname("dtran_nwave")
    dim2.setname("dtran_ntheta")
    dim1 = dtran_b0.dim(0)
    dim2 = dtran_b0.dim(1)
    dim1.setname("dtran_nwave")
    dim2.setname("dtran_ntheta")

    # close file
    new_file.end()
    file.end()
    
    
file_names = os.listdir("G:\\Users\\Lenovo\\Desktop\\zd22\\zd22\\")
for file_name in file_names:
    interp_aerosol(file_name)
    print("{} is done!".format(file_name))
