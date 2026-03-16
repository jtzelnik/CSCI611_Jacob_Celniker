from ultralytics import YOLO

model = YOLO("best.pt")
results = model("test.MP4", conf=0.2, iou=0.7, save=True)

