from TextDetection.textDetector import TextDetector
from Camera.cameraFeedProvider import CameraFeedProvider

import cv2

if __name__ == "__main__":
    text_detector = TextDetector()
    camera_feed_provider = CameraFeedProvider()
    
    try:
        while True:
            frame = camera_feed_provider.get_next_frame()

            if frame is not None:
                # Process the frame for text detection
                detected_text = text_detector.process_frame(frame)

                if detected_text is not None:
                    # You can use the 'detected_text' variable for further processing or display
                    print("Final Detected Text: ", detected_text)

    finally:
        camera_feed_provider.release_camera()
        cv2.destroyAllWindows()
