from pytube import YouTube
import os
import cv2

class Video_fetch:
    def __init__(self, url, dir, frames_dir):
        self.url = url
        self.dir = dir
        self.frames_dir = frames_dir
        self.count = 1
        self.fetch_video()
        self.frames()
    
    def fetch_video(self):
        yt = YouTube(self.url)
        video_title = yt.title
        self.downloaded_video_path = os.path.join(self.dir, f"{video_title}.mp4")
        all_streams = yt.streams.filter(progressive=True, file_extension="mp4")
        selected_quality_stream = all_streams.filter(res="720p").first()
        selected_quality_stream.download(output_path=self.dir)

    def frames(self):
        cap = cv2.VideoCapture(self.downloaded_video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)                 
        interval_seconds = 42
        interval_frames = int(fps * interval_seconds)
        print(interval_frames)
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count % interval_frames == 0:
                if frame_count > 0 and frame_count < (cap.get(cv2.CAP_PROP_FRAME_COUNT) - interval_frames):
                    frame_filename = os.path.join(self.frames_dir, f"frame_{self.count}.jpg")
                    cv2.imwrite(frame_filename, frame)
                    self.count +=1
            frame_count += 1
