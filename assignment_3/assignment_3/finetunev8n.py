from ultralytics import YOLO


model = YOLO("yolov8n.pt") #load pretrained model


model.train(
    data="dataset.yaml",
    epochs=30,
    imgsz=640,
    batch=16
)
'''
model.train(
    data="dataset.yaml",
    epochs=30,
    imgsz=1280,
    batch=16
)

model.train(
    data="dataset.yaml",
    epochs=30,
    imgsz=1280,
    batch=16,
    degrees=5.0,
    shear=2.0,
    perspective=0.0005,
    mixup=0.1
)
'''