# DETECT ONLY RED CIRCLES IN A GIVEN IMAGE


### PROBLEM STATEMENT : 
Write a program to process the Image given and output a image detecting only **RED CIRCLES** leaving other colored shapes aside.

_Language used_ : **C++**

_Library used_ : **[OpenCV](https://opencv.org/)**

_Platform used_ : **Visual Studio 2019**


### PRE-REQUISITE

> Install OpenCV and setup Visula studio. Please visit this **[link](https://www.youtube.com/watch?v=7SM5OD2pZKY&t=654s)**.

### CODE EXPLATION [DETECT_RED_CIRCLES.CPP](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/detect_red_circles.cpp)
* Open the desired image for analysis.

* Threshold the Input image to [HSV space](https://en.wikipedia.org/wiki/HSL_and_HSV), as it has the desirable property 
that allows us to identify a particular color using a single value, the **hue**, instead of three values. 

* Combine the two threshold images i.e low range and high range images.

* Apply Hough Transform to detect circles in the image and patch the red color and circles together.

### RESULTS

> Input: [Input 1](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/all_circles.png)

![](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/result1.png)

> Input: [Input 2](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/all_red.png)

![](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/result2.png)

> Input: [Input 3](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/diff_shapes.png)

![](https://github.com/smitz94/Projects/blob/master/Detect%20only%20Red%20circles%20in%20a%20given%20Image/Images/result3.png)
