from detector import process_video
import sys
import os
import subprocess


if __name__ == '__main__':
    INPUT_VIDEO = 'crowd.mp4'
    OUTPUT_VIDEO = 'crowd_annotated_yolo.mp4'

    process_video(input_path=INPUT_VIDEO, output_path=OUTPUT_VIDEO, device='cpu')

    if sys.platform.startswith('win'):
        os.startfile(OUTPUT_VIDEO)
    elif sys.platform.startswith('darwin'):
        subprocess.run(['open', OUTPUT_VIDEO])
    elif sys.platform.startswith('linux'):
        subprocess.run(['xdg-open', OUTPUT_VIDEO])
    else:
        print(f"Автоматическое открытие не поддерживается на платформе {sys.platform}")