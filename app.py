from multiprocessing import Process, Value
from capture import capture
from interface import control_panel

if __name__ == '__main__':

    save_frame_flag = Value('i', 0) # Value('type', value)
    captured_frame_num = Value('i', 0)
    
    capture_process = Process(target=capture, args=(save_frame_flag, captured_frame_num,))
    control_process = Process(target=control_panel, args=(save_frame_flag, captured_frame_num,))

    capture_process.start()
    control_process.start()

    capture_process.join()
    control_process.join()
