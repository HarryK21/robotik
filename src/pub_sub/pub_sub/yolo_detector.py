import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO

class YoloDetector(Node):
    def __init__(self):
        super().__init__('yolo_detector')
        self.subscription = self.create_subscription(Image, 'image_raw', self.listener_callback, 10)
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt') # Lädt das Modell automatisch

    def listener_callback(self, msg):
        # ROS Bild zu OpenCV konvertieren
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # YOLO Vorhersage
        results = self.model(cv_image, stream=True)
        # Ergebnisse im Bild einzeichnen und anzeigen
        for r in results:
            annotated_frame = r.plot()
            cv2.imshow("YOLOv8 Erkennung", annotated_frame)
            cv2.waitKey(1)

def main():
    rclpy.init()
    node = YoloDetector()
    rclpy.spin(node)
    cv2.destroyAllWindows()
    rclpy.shutdown()

if __name__ == '__main__':
    main()