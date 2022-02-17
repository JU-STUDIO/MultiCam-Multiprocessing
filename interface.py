from config import Config
import tkinter as tk
import cv2

def control_panel(save_frame_flag, last_captured_frame_num):

    replay_frame_num = 0

    def start_save():
        save_frame_flag.value = int(1)

    def end_save():
        save_frame_flag.value = int(0)

    def show_frame(frame_num):
        for cam_id in range(0,Config.camera_quantity):
            frame_Path = fr'videos/{cam_id}/{frame_num}.png'
            print(frame_Path)
            image = cv2.imread(frame_Path)
            cv2.imshow(f'CAM_{cam_id}', image)

    def show_replay_frame(frame_num):
        for cam_id in range(0,Config.camera_quantity):
            frame_Path = fr'videos/{cam_id}/{frame_num}.png'
            print(frame_Path)
            replay_frame = cv2.imread(frame_Path)
            cv2.waitKey(200) # 0.2sec
            cv2.imshow('Replay', replay_frame)

    def next_frame():
        if last_captured_frame_num.value > replay_frame_num:
            last_captured_frame_num.value += 1
            show_frame(last_captured_frame_num.value)
        else:
            show_frame(int(0))

    def prev_frame():
        if last_captured_frame_num.value > replay_frame_num:
            last_captured_frame_num.value -= 1
            show_frame(last_captured_frame_num.value)
        else:
            show_frame(int(0))

    def replay_frame():
        show_replay_frame(last_captured_frame_num.value)


    window = tk.Tk()
    window.title('window')
    window.title("控制面板")
    window.geometry('380x100') # 寬*高

    start_save_btn = tk.Button(window, text='開始儲存', width=10, command=start_save).place(x=10, y=10)
    end_save_btn = tk.Button(window, text='結束儲存', width=10, command=end_save).place(x=240, y=10)

    replay_frame_btn = tk.Button(window, text='Replay', width=7, height=4, command=replay_frame).place(x=140, y=10)

    prev_frame_btn = tk.Button(window, text='<F', width=10, command=prev_frame).place(x=10, y=55)
    next_frame_btn = tk.Button(window, text='F>', width=10, command=next_frame).place(x=240, y=55)

    window.mainloop()