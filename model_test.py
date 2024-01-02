import ultralytics

model = ultralytics.YOLO("best.pt")

print(int(model.predict(source="images/img1.jpg", conf=0.15, save=True)[0].boxes.cls))