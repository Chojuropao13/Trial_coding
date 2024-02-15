import cv2
import numpy as np
from PIL import ImageGrab
import threading

class ScreenRecorder:
    def __init__(self, output_path="output.avi", fps=5.0, resolution=(1366, 768)):
        self.output_path = output_path
        self.fps = fps
        self.resolution = resolution
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(self.output_path, self.fourcc, self.fps, self.resolution)
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.record)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.thread.join()
            self.out.release()
            cv2.destroyAllWindows()

    def record(self):
        while self.running:
            img = ImageGrab.grab()
            img_np = np.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)
            self.out.write(frame)
            cv2.imshow("Screen Recorder", frame)
            if cv2.waitKey(1) == 27:
                break

if __name__ == "__main__":
    recorder = ScreenRecorder()
    recorder.start()
    input("Press Enter to stop recording...")
    recorder.stop()