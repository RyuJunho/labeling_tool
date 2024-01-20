import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2 as cv


global min_index 
global max_index 
global dir_path
global file_list


def open_image_folder() :
    global min_index 
    global max_index 
    global dir_path
    global file_list

    print('open_image_foler()')
    dir_path = filedialog.askdirectory(initialdir='/',\
                                          title = '폴더를 선택해 주세요')
    if dir_path == '' :
        messagebox.showwarning('경고','폴더를 선택 하세요')
    else : 
        file_list = os.listdir(dir_path) # 선택한 폴더의 파일을 리스트로 저장
        
        if len(file_list) == 0 :
            messagebox.showwarning('경고','폴더내 파일이 없습니다.')
        else : 
            min_index = 0
            max_index = len(file_list) - 1 
            current_index = min_index

            print(*file_list)
            # print(dir_path + '/' + file)
            while True :
                image = cv.imread(dir_path + '/' + file_list[current_index]
                                    ,cv.IMREAD_UNCHANGED)
                resized_image = cv.resize(image, dsize=(600,300)
                                            ,interpolation=cv.INTER_LINEAR)
                print(f'current : {current_index}')
                cv.imshow('image',resized_image)
            
                key = cv.waitKeyEx(0)

                if key == ord('a') or key == 0x250000:  # Left arrow key
                    print('<-')
                    if current_index == min_index :
                        continue
                    else :
                        current_index = current_index - 1
                elif key == ord('d') or key == 0x270000:  # Right arrow key
                    print('->')
                    if current_index == max_index :
                        continue
                    else :
                        current_index = current_index + 1
                elif key == 27 :
                    break
                    


window = tk.Tk()
window.title("labeling tool")
window.geometry("200x300+500+150")
window.resizable(False, False)

open_image_flag = False 

open_image_button = tk.Button(window, text = 'open image folder'
                              ,pady = 20
                              ,command = open_image_folder)
open_image_button.pack()


window . mainloop()