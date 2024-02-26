import os
import cv2

video_folder_path = input("Video klasörünün adını sal bakayım: ")

video_files = [f for f in os.listdir(video_folder_path) if f.endswith(".mp4")]

current_video_index = 0
current_frame_index = 0

while current_video_index < len(video_files):
    video_file = video_files[current_video_index]
    video_path = os.path.join(video_folder_path, video_file)

    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video', frame)

        if current_frame_index == 0:
            print(f"Şu anki video: {video_file}")

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            cap.release() 
            new_name = f"etiketli{current_video_index + 1}.mp4"
            os.rename(video_path, os.path.join(video_folder_path, new_name))
            print(f"{video_file} adı {new_name} olarak değiştirildi.")
            current_video_index += 1
            current_frame_index = 0
            break
        elif key == ord(' '):
            current_video_index += 1
            current_frame_index = 0
            break

        current_frame_index += 1

    cv2.destroyWindow('Video')

print("Tüm videolar işlendi.")
