import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load the image
    img = plt.imread("frenchRoadSign.jpg")

    # Gray scale
    from skimage.color import rgb2gray
    img = rgb2gray(img)

    # Canny edge detection
    from skimage.feature import canny
    edges = canny(img, sigma=3, low_threshold=0.18, high_threshold=0.20)

    # Display the image and plot all contours found
    fig, ax = plt.subplots()
    ax.imshow(edges)
    ax.axis('off')
    plt.show()
