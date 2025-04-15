# Eğitilmiş YOLO modeli ile nesne tespiti yapıp kayıt etmek.
from ultralytics import YOLO

#yolo11x.pt eğitilmiş bir yolo modelidir.

model = YOLO("yolo11x.pt")

sonuc = model("insan.jpg", save=True)

sonuc[0].show()

