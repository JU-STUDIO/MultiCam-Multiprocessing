from vidgear.gears import CamGear
from config import Config
import cv2

def capture(save_frame_flag, captured_frame_num):
    
    frame_count = 0

    for cam_id in range(0,Config.camera_quantity):
        globals()['stream_'+str(cam_id)] = CamGear(source=cam_id, logging=True, **Config.camera_params).start()

    while True:

        try:

            for cam_id in range(0,Config.camera_quantity):

                globals()['cam_'+str(cam_id)+'_frame'] = globals()['stream_'+str(cam_id)].read()

                if globals()['cam_'+str(cam_id)+'_frame'] is None:
                    break
                
                if save_frame_flag.value == int(1):
                    frame_num = captured_frame_num.value
                    cv2.imwrite(fr'videos/{cam_id}/{frame_num}.png', globals()['cam_'+str(cam_id)+'_frame'])
                    captured_frame_num.value += 1

                frame_count += 1
                cv2.putText(globals()['cam_'+str(cam_id)+'_frame'], str(frame_count), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
                cv2.imshow(f"CAM_{cam_id}", globals()['cam_'+str(cam_id)+'_frame'])

            key = cv2.waitKey(1)
            if key == 27 : # ESC
                break

        except AttributeError:
            pass

    cv2.destroyAllWindows()