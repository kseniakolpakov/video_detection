def display_progress(frame_id: int, interval: int = 30) -> None:
    """
    Печатает прогресс каждые N кадров.

    :param frame_id: номер текущего кадра
    :param interval: интервал вывода прогресса
    """
    if frame_id % interval == 0:
        print(f"Обработано кадров: {frame_id}")