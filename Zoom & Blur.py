import cv2     #Import opencv from library

array = []     #Array for saving mouse clicks coordinates
def click(event, x, y, flags, param):     #function for detecting mouse events
    
    global array

    if event == cv2.EVENT_LBUTTONDOWN:     #Save mouse left click down coordinates
        array = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:     #Save mouse left click up coordinates
        array.append((x, y))
       

image = cv2.imread("Wallpaper.jpg")     #Read the image
clone = image.copy()               #Make a copy of image to keep  the original file unchanged
cv2.namedWindow("image")            #Make a window to show the image
cv2.setMouseCallback("image", click)     #Use function to select the desired location

key = 0
while key != 27:     #Loop run until press ESC keyboard button to close image
    key = cv2.waitKey(1) & 0xFF
    cv2.imshow("image", image)

    if len(array) == 2:     #If both coordinates are saved and not same , increases the size
        if abs(array[0][1]-array[1][1]) > 0  and abs(array[0][0] - array[1][0]) > 0:     #Use abs function so we can also click right down and then left up
            X = [array[0][1] , array[1][1]]
            Y = [array[0][0] , array[1][0]]
            X.sort()     #Sort X to prevent problems
            Y.sort()     #Sort Y to prevent problems

            roi = clone[X[0]:X[1], Y[0]:Y[1]]    #Copy selected area
            scaleup = cv2.resize(roi, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)     #Double the size of selected location
            blured = cv2.blur(scaleup,(10,10))     #Blur image by 10 scale
            cv2.imshow("scaleup", scaleup)
            cv2.imshow("blured", blured)

cv2.destroyAllWindows()     #Close all windows


#Written by Mohammad Abbasi Moghadam
#20/7/2020
