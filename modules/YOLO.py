import cv2
import numpy as np

class YOLO:

    def __init__(self, yoloConfig, yoloWeights, classFile):
        self.net = self.load_model(yoloConfig=yoloConfig, yoloWeights=yoloWeights)
        self.classes = self.load_classes(classFile=classFile)

    def load_model(self, yoloConfig, yoloWeights):
        # Load YOLO model
        net = cv2.dnn.readNetFromDarknet(yoloConfig, yoloWeights)
        return net

    def load_classes(self, classFile):
        # Load class names
        with open(classFile, 'r') as f:
            classes = [line.strip() for line in f.readlines()]
        return classes

    def detect_objects(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        # =================
        # DELETE BELOW LINE

        # r = blob[0, 0, :, :]

        # cv2.imshow('blob', r)
        # text = f'Blob shape={blob.shape}'
        # cv2.displayOverlay('blob', text)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # DELETE ABOVE LINE
        # =================
        self.net.setInput(blob)
        layer_names = self.net.getLayerNames()
        # print(layer_names)
        # output_layers = [layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
        # output_layers = [layer_name for name in layer_names]
        
        # return 
        outputs = self.net.forward(output_layers)

        height, width = frame.shape[:2]
        boxes = []
        confidences = []
        class_ids = []

        for output in outputs:
            for detection in output:
                scores = detection[5:]  # Skip the first 5 values
                class_id = np.argmax(scores)  # Get the class with the highest score
                confidence = scores[class_id]  # Get the confidence value for the class
                if confidence > 0.5:  # Confidence threshold (adjust as needed)
                    # Object detected
                    center_x, center_y, w, h = (detection[0:4] * np.array([width, height, width, height])).astype('int')

                    # Rectangle coordinates
                    x = int(center_x - (w / 2))
                    y = int(center_y - (h / 2))

                    boxes.append([x, y, int(w), int(h)])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Non-maxima suppression to eliminate redundant overlapping boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)  # Thresholds may need adjustment

        final_detections = []
        for i in indices:
            box = boxes[i]
            x, y, w, h = box
            label = str(self.classes[class_ids[i]])
            confidence = confidences[i]
            final_detections.append((label, confidence, (x, y, x+w, y+h)))

        return final_detections

    @property
    def available_classes(self):
        return self.classes