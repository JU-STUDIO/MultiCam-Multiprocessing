from config import Config
import tkinter as tk
import cv2

def control_panel(save_frame_flag, last_captured_frame_num):

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

        frame_1 = frame_num - 15
        frame_14 = frame_num
        for cam_id in range(frame_1, frame_14):
            frame_Path = fr'videos/0/{cam_id}.png'
            print(frame_Path)
            replay_frame = cv2.imread(frame_Path)
            cv2.waitKey(100) # 0.1sec
            cv2.imshow('Replay', replay_frame)

        for cam_id in range(0,Config.camera_quantity):
            frame_Path = fr'videos/{cam_id}/{frame_num}.png'
            print(frame_Path)
            replay_frame = cv2.imread(frame_Path)
            cv2.waitKey(200) # 0.2sec
            cv2.imshow('Replay', replay_frame)
        
        frame_16 = frame_num
        frame_30 = frame_num + 15
        for cam_id in range(frame_16, frame_30):
            frame_Path = fr'videos/7/{cam_id}.png'
            print(frame_Path)
            replay_frame = cv2.imread(frame_Path)
            cv2.waitKey(100) # 0.1sec
            cv2.imshow('Replay', replay_frame)

        # ------------------ video_writer ------------------
        img_array = []

        frame_1 = frame_num - 15
        frame_14 = frame_num
        for cam_id in range(frame_1, frame_14):
            frame_Path = fr'videos/0/{cam_id}.png'
            replay_frame = cv2.imread(frame_Path)
            height, width, layers = replay_frame.shape
            size = (width,height)
            img_array.append(replay_frame)

        for cam_id in range(0,Config.camera_quantity):
            frame_Path = fr'videos/{cam_id}/{frame_num}.png'
            replay_frame = cv2.imread(frame_Path)
            height, width, layers = replay_frame.shape
            size = (width,height)
            img_array.append(replay_frame)
        
        frame_16 = frame_num
        frame_30 = frame_num + 15
        for cam_id in range(frame_16, frame_30):
            frame_Path = fr'videos/7/{cam_id}.png'
            replay_frame = cv2.imread(frame_Path)
            height, width, layers = replay_frame.shape
            size = (width,height)
            img_array.append(replay_frame)
        
        out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

    # def video_writer(frame_num):

    #     img_array = []
    #     for filename in glob.glob('C:/New folder/Images/*.jpg'):
    #         img = cv2.imread(filename)
    #         height, width, layers = img.shape
    #         size = (width,height)
    #         img_array.append(img)


    #     out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
        
    #     for i in range(len(img_array)):
    #         out.write(img_array[i])
    #     out.release()

    def next_frame():
        if last_captured_frame_num.value != Config.last_replay_frame_num:
            Config.last_replay_frame_num += 1
            show_frame(Config.last_replay_frame_num)

    def prev_frame():
        if Config.last_replay_frame_num != int(0):
            Config.last_replay_frame_num -= 1
            show_frame(Config.last_replay_frame_num)

    def replay_frame():
        show_replay_frame(Config.last_replay_frame_num)


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