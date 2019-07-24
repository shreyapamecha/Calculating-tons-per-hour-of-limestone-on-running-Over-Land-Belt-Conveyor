# Calculating-tons-per-hour-of-limestone-on-running-Over-Land-Belt-Conveyor
The main objective is to reckon or calculate the area covered by limestone on running OLBC (Over Land Belt Conveyor) and subsequently, converting it into volume to thereby estimate tons per hour.

To run Calculating_TPH.py, follow these steps below:
  1. Download IDLE python from this site: 'https://www.python.org/downloads/'.
  2. Install the following libraries: cv2, matplotlib, numpy, sys.
  3. Through Command Prompt, run this code. (Make sure to change the directories)
  
Methodology:
  1. Finding Contours: 
     CONTOURS: these are simple curves joining all the continuous points (along the boundary), having color in a specified range (0-40, 0-70, 190-255). Contours are a useful tool for shape analysis, object detection and recognition.
     For better accuracy, binary images are used. In OpenCV, finding contours is similar to finding white objects from black background.
     
  2. Closing Morphological Operation:
     Morphological transformations are simple operations based on the shape of an image. Generally, this operations are carried out on binary images. It requires two inputs: a binary image and a kernel or a structuring element. There are many types of Morphological Operations such as: Erosion, Dilation, Opening, Closing, Morphological Gradient, Top Hat, Black Hat, etc. The best suitable one for the above transformation is Closing Morphological Operation (kernel: 20X20).
  
  3. Finding Contours
  
  4. Determining Area of the white region
  
Limitations:
  1. Selection of Unwanted Areas.
  2. Accuracy on stake (Morphological Operation)
     Kernel used in the closing operation: 20 X 20
     The larger the size of the kernel, lower will be the accuracy level.
