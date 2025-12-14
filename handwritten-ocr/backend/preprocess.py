import os

def preprocess_image(image_path: str) -> str:
    """
    Takes an image path, applies preprocessing,
    saves a new image, and returns the new path.
    """

    import cv2  # lazy import for faster startup

    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Denoising
    denoised = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive thresholding
    thresh = cv2.adaptiveThreshold(
        denoised,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Save processed image
    base, _ = os.path.splitext(image_path)
    processed_path = base + "_processed.png"
    cv2.imwrite(processed_path, thresh)

    return processed_path
