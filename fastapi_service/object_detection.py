import torch
import cv2
import os
import logging
from pathlib import Path
from ultralytics import YOLO

# Configure logging
logging.basicConfig(filename="yolo_detection.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Load YOLOv5 model (Pre-trained on COCO dataset)
model = YOLO("models/yolov5su.pt")  # Using YOLOv5 Small model (you can use yolov5m.pt or yolov5l.pt for better accuracy)

# Paths
input_folder = "yolo_input/raw/"
output_folder = "yolo_output/"
os.makedirs(output_folder, exist_ok=True)

def run_object_detection():
    images = [f for f in os.listdir(input_folder) if f.endswith((".jpg", ".png", ".jpeg"))]
    
    if not images:
        logger.error("No images found for object detection.")
        return
    
    for img_name in images:
        img_path = os.path.join(input_folder, img_name)
        output_path = os.path.join(output_folder, img_name)

        try:
            # Run YOLOv5 model on image
            results = model(img_path)

            # Process detections
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = box.xyxy[0].tolist()  # Bounding box
                    conf = box.conf[0].item()  # Confidence score
                    cls = box.cls[0].item()  # Class label

                    # Draw bounding boxes on image
                    img = cv2.imread(img_path)
                    label = f"{model.names[int(cls)]} {conf:.2f}"
                    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    # Save processed image
                    cv2.imwrite(output_path, img)

            logger.info(f"Object detection completed for {img_name}. Results saved in {output_folder}")

        except Exception as e:
            logger.error(f"Error processing {img_name}: {str(e)}")

if __name__ == "__main__":
    run_object_detection()
