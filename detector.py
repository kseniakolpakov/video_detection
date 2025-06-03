import cv2
from ultralytics import YOLO
from utils import display_progress


def process_video(input_path: str, output_path: str, device: str = 'cpu') -> None:
    """
    Обрабатывает видео, выполняет детекцию людей и сохраняет аннотированный файл.

    :param input_path: путь к исходному видео
    :param output_path: путь для сохранения видео с разметкой
    :param device: 'cpu' или 'cuda'
    """
    model = YOLO('yolov8n.pt')

    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_id += 1
        results = model.predict(frame, classes=[0], device=device, verbose=False, iou=0.2)
        annotated = results[0].plot()
        out.write(annotated)

        display_progress(frame_id)

    cap.release()
    out.release()
    print(f"\nВидео сохранено: {output_path}")