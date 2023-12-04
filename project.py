from Video_fetch import Video_fetch
from Face_detection import Face_detection



if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=09R8_2nJtjg"
    frames_final_directory = r"C:\Users\HP\Documents\Internship_project\video\marked_frames"
    frames_output_directory = r"C:\Users\HP\Documents\Internship_project\video\frames"
    output_directory = r"C:\Users\HP\Documents\Internship_project\video"
    output_vedio = r"C:\Users\HP\Documents\Internship_project\video\frame_vedio"
    video = Video_fetch(video_url, output_directory, frames_output_directory)
    Face_recognition = Face_detection(frames_output_directory, frames_final_directory)
   
