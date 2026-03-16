Instructions:

    Install Python Dependencies:
        ultralytics
        opencv-Python
        numpy
        torch
        torchvision
        torchaudio

    (optional) Donwload Training (fine-tuning) Dataset (dont need unless retuning):
        https://www.kaggle.com/datasets/kietzer0/lisa-traffic-light-dataset-yolo?resource=download
        place datasets folder in project folder
        provided dataset.yaml will point to it

    (optional) RUN FINE-tuning (best.pt is already provided)
        Uncomment the model.train with the desired parameters (640 default)

    RUN testing
        place desired test video in project folder and name it test.mp4
        run test.py
        