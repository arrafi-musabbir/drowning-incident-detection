import ultralytics
import os
import shutil
import glob
directory = "runs/detect/predict"
img_path = glob.glob(os.path.join(directory, "*.jpg"))[0]
print(img_path)


# # Specify the directory from which to delete subdirectories
# directory = "runs/detect"

# # Iterate over all entries in the directory
# for entry in os.listdir(directory):
#     path = os.path.join(directory, entry)
    
#     # Check if the entry is a directory
#     if os.path.isdir(path):
#         # Remove the subdirectory
#         shutil.rmtree(path)

# model = ultralytics.YOLO("best.pt")


# print(model.predict(source="images/img1.jpg", conf=0.15, save=True, name='predict')[0])
