#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'ExodusIIReader'
whipple_Shieldexo300 = ExodusIIReader(FileName=['/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.000', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.001', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.002', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.003', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.004', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.005', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.006', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.007', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.008', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.009', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.010', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.011', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.012', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.013', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.014', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.015', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.016', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.017', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.018', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.019', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.020', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.021', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.022', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.023', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.024', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.025', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.026', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.027', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.028', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.029', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.030', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.031', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.032', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.033', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.034', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.035', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.036', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.037', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.038', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.039', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.040', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.041', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.042', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.043', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.044', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.045', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.046', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.047', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.048', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.049', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.050', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.051', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.052', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.053', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.054', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.055', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.056', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.057', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.058', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.059', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.060', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.061', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.062', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.063', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.064', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.065', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.066', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.067', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.068', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.069', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.070', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.071', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.072', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.073', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.074', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.075', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.076', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.077', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.078', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.079', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.080', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.081', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.082', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.083', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.084', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.085', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.086', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.087', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.088', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.089', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.090', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.091', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.092', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.093', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.094', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.095', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.096', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.097', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.098', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.099', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.100', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.101', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.102', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.103', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.104', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.105', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.106', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.107', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.108', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.109', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.110', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.111', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.112', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.113', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.114', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.115', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.116', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.117', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.118', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.119', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.120', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.121', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.122', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.123', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.124', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.125', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.126', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.127', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.128', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.129', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.130', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.131', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.132', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.133', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.134', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.135', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.136', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.137', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.138', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.139', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.140', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.141', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.142', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.143', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.144', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.145', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.146', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.147', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.148', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.149', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.150', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.151', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.152', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.153', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.154', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.155', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.156', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.157', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.158', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.159', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.160', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.161', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.162', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.163', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.164', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.165', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.166', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.167', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.168', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.169', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.170', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.171', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.172', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.173', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.174', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.175', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.176', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.177', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.178', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.179', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.180', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.181', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.182', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.183', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.184', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.185', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.186', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.187', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.188', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.189', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.190', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.191', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.192', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.193', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.194', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.195', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.196', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.197', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.198', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.199', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.200', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.201', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.202', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.203', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.204', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.205', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.206', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.207', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.208', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.209', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.210', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.211', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.212', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.213', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.214', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.215', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.216', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.217', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.218', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.219', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.220', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.221', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.222', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.223', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.224', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.225', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.226', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.227', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.228', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.229', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.230', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.231', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.232', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.233', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.234', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.235', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.236', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.237', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.238', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.239', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.240', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.241', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.242', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.243', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.244', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.245', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.246', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.247', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.248', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.249', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.250', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.251', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.252', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.253', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.254', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.255', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.256', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.257', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.258', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.259', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.260', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.261', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.262', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.263', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.264', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.265', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.266', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.267', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.268', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.269', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.270', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.271', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.272', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.273', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.274', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.275', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.276', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.277', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.278', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.279', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.280', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.281', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.282', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.283', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.284', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.285', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.286', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.287', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.288', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.289', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.290', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.291', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.292', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.293', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.294', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.295', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.296', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.297', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.298', '/work/01336/carson/intelTACC/data/Whipple300/Whipple_Shield.exo.300.299'])
whipple_Shieldexo300.ElementVariables = []
whipple_Shieldexo300.NodeSetArrayStatus = []
whipple_Shieldexo300.ModeShape = 21

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on whipple_Shieldexo300
whipple_Shieldexo300.ElementVariables = ['VOID_FRC', 'VOLFRC1', 'VOLFRC2', 'DENSITY', 'TEMPERATURE', 'PRESSURE']
whipple_Shieldexo300.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1005, 566]

# show data in view
whipple_Shieldexo300Display = Show(whipple_Shieldexo300, renderView1)
# trace defaults for the display properties.
whipple_Shieldexo300Display.ColorArrayName = [None, '']
#whipple_Shieldexo300Display.ScalarOpacityUnitDistance = 0.00028215277189116723

# reset view to fit data
renderView1.ResetCamera()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=whipple_Shieldexo300)

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)
# trace defaults for the display properties.
cellDatatoPointData1Display.ColorArrayName = [None, '']
#cellDatatoPointData1Display.ScalarOpacityUnitDistance = 0.00028215277189116723

# hide data in view
Hide(whipple_Shieldexo300, renderView1)

# create a new 'Clip'
clip1 = Clip(Input=cellDatatoPointData1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'DENSITY']
clip1.Value = 3936.18994140625

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, 0.0, 0.018435800448060036]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1)

# Properties modified on clip1
clip1.ClipType = 'Scalar'
clip1.Scalars = ['POINTS', 'VOLFRC2']
clip1.Value = 0.5

# show data in view
clip1Display = Show(clip1, renderView1)
# trace defaults for the display properties.
clip1Display.ColorArrayName = [None, '']
#clip1Display.ScalarOpacityUnitDistance = 0.00049793065251967561

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['POINTS', 'DENSITY']
clip2.Value = 3317.7668240797921

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-0.0012411912903189659, 0.0, 0.0071280160918831825]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2)

# Properties modified on clip2.ClipType
clip2.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip2Display = Show(clip2, renderView1)
# trace defaults for the display properties.
clip2Display.ColorArrayName = [None, '']
#clip2Display.ScalarOpacityUnitDistance = 0.00050864790828488793

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(cellDatatoPointData1)

# create a new 'Contour'
contour1 = Contour(Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'DENSITY']
contour1.Isosurfaces = [3936.18994140625]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'VOLFRC1']
contour1.Isosurfaces = [0.5]

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.ColorArrayName = [None, '']

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# set scalar coloring
ColorBy(contour1Display, ('POINTS', 'PRESSURE'))

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'PRESSURE'
pRESSURELUT = GetColorTransferFunction('PRESSURE')

# get opacity transfer function/opacity map for 'PRESSURE'
pRESSUREPWF = GetOpacityTransferFunction('PRESSURE')

animationScene1.Play()

# set active source
SetActiveSource(clip2)

# Properties modified on clip2
clip2.InsideOut = 1

# Rescale transfer function
pRESSURELUT.RescaleTransferFunction(-510438080.257, 780985983.58)


for i in range(0, 10):
	Render()
