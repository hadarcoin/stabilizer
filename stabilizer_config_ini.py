import os
import subprocess
import shutil

print('-----------------------creating stabilizeConfig.ini files-------------------------------  ')
print('---------------------------Generate them, guess why?--------------------------------  ')
print('---------------------------------------------------------------------------------------  ')
print('---------------Right! we need the Matrix file (txt) per each camera--------------------  ')
print('---------------------------------------------------------------------------------------  ')
print('---------------------------------------------------------------------------------------  ')

number_of_cameras = raw_input("please enter number of cameras:")
#
# for i in range(int(number_of_cameras)):
#     u_cam_number = 1+int(i)
#     u_ref_image = '{value:0{pad}}.jpg'.format(value=u_cam_number, pad=4)
#     u_new_image = u_ref_image
#     u_txt_file = '{value:0{pad}}.txt'.format(value=u_cam_number, pad=4)
#     u_txt_new_file = u_txt_file
#     u_calibration_file = 'calibration_{iter}.ma'.format(iter=i+1)
#     with open(r'D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\StabilizerConfig.ini', "rt") as fin:
#       with open(r"D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\output\stabilize_new{iter}.ini".format(iter=i+1), "wt") as fout:
#         lines = fin.read()
#         checkWords = ("user_cameraNo", "user_refImage", "user_newImage", "user_TxtFile", "user_TxtnewFile", "user_calibration")
#         repWords = (u_cam_number, u_ref_image, u_new_image, u_txt_file, u_txt_new_file, u_calibration_file)
#         for check, rep in zip(checkWords, repWords):
#             lines = lines.replace(check, str(rep))
#         fout.write(lines)
#
#     cmd = r'D:\hadar\training\09-Stabilization\HandsOn\Application\Stabilizer.exe  D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\output\stabilize_new{iter}.ini'.format(iter=i+1)
#     subprocess.call(cmd, shell=True)

print('-------------------------------stabilizer finished -------------------------------------  ')
print('----------------------------now that you have txt files -------------------------------  ')
print('------------------------------Those files use for:-------------------------------------  ')
print('---------------------------------------------------------------------------------------  ')
print('--------------------------------- Stabilize vis----------------------------------------  ')
print('---------------------------------------------------------------------------------------  ')
print('------------------------PIP file if you dont remember----------------------------------  ')
print('---------------------------------------------------------------------------------------  ')

new_files=[]
ref_arr=[]
for i in range(int(number_of_cameras)):
    u_LoadImage = '{value:0{pad}}.jpg'.format(value=i+1, pad=4)
    u_ref_image = u_LoadImage
    u_groundMask = '{value:0{pad}}_result.tif'.format(value=i+1, pad=4)
    u_txt_file = '{value:0{pad}}.txt'.format(value=i+1, pad=4)
    u_save_matrix = '{value:0{pad}}.txt'.format(value=i+1, pad=4)
    u_save_new_vis = '{value:0{pad}}.jpg'.format(value=i+1, pad=4)
    new_files.append(u_save_new_vis)
    with open(r'D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\source_PrepCurrentFrame.xml', "rt") as fin:
      with open(r"D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\output_pip_wrap\stabilize_pip{iter}.xml".format(iter=i+1), "wt") as fout:
        lines = fin.read()
        checkWords = ("user_LoadImage", "user_refImage", "user_groundmask", "user_TxtFile", "user_saveMatrix", "user_saveVis")
        repWords = (u_LoadImage, u_ref_image, u_groundMask, u_txt_file, u_save_matrix, u_save_new_vis)
        for check, rep in zip(checkWords, repWords):
            lines = lines.replace(check, str(rep))
        fout.write(lines)


    cmd = r'D:\pip\bin\pip\x64\Release\Pip.exe  D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\output_pip_wrap\stabilize_pip{iter}.xml'.format(iter=i+1)
    subprocess.call(cmd, shell=True)

    print('you are the best --> now you have a stabilized image, compare it ref...')

#create compare folder
#create compare folder
#create compare folder
#create compare folder
#create compare folder
#create compare folder
newpath = r'D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\output_pip_wrap\compareRef2Stabilized'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#create seperated folders, and copy to each one of them the ref and the new stabilized-image
counter = 1
for i in new_files:
    new_sub_path = r'D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\output_pip_wrap\compareRef2Stabilized\compareImage_{iter}'.format(iter=counter)
    if not os.path.exists(new_sub_path):
        os.makedirs(new_sub_path)
    counter += 1
    path_to_new_vis = r'D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\output_pip_wrap\{file}'.format(file=i)
    shutil.copy(path_to_new_vis, new_sub_path)
    path_to_ref = r'D:\hadar\training\12-SemiHandsOn\03-StabilizeThis\inputs\Reference\{file}'.format(file=i)
    shutil.copy(path_to_ref, r'{path}\ref_{file}'.format(path=new_sub_path, file=i))

print('---------------------Go and check your stabilize quality-------------------------------  ')

print('---------------------------------------------------------------------------------------  ')
print('---------------------------------------------------------------------------------------  ')
print('---------------------------------------------------------------------------------------  ')
print('--------------------------------------Thanks-------------------------------------------  ')
print('---------------------------------------------------------------------------------------  ')
