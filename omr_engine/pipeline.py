import cv2, numpy as np, tensorflow as tf

model = tf.keras.models.load_model("omr_engine/bubble_cnn.h5")

def classify_bubble(crop_img):
    img = cv2.resize(crop_img, (28,28))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=(0,-1))
    pred = model.predict(img, verbose=0)[0][0]
    return 1 if pred > 0.5 else 0, float(pred)

def evaluate_sheet(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape
    bubble_h, bubble_w = h//10, w//10

    scores = []
    for r in range(10):
        for c in range(10):
            bubble = gray[r*bubble_h:(r+1)*bubble_h, c*bubble_w:(c+1)*bubble_w]
            label, conf = classify_bubble(bubble)
            scores.append(label)

    total_score = sum(scores)
    return {"total_score": total_score, "details": scores}
