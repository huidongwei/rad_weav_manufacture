import os

convert     = "F:/Openradioss/OpenRadioss-main/exec/anim_to_vtk_win64.exe "
#print()
file_name   = str(input("Please input the file name (without A and number): "))
max_num     = int(input("Please input the maximum number of files: "))

for num in range(1,max_num+1):
    str_num     = str('{:03d}'.format(num))
    operation   = convert + file_name + "A" + str_num 
    operation   = operation + " > " + file_name + "A" + str_num + ".vtk"
    #print(operation)
    os.system(operation)
    #os.system("F:/Openradioss/OpenRadioss-main/exec/anim_to_vtk_win64.exe tensile_LAW36A001 > tensile_LAW36A001.vtk")