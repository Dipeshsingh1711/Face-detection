# Face-detection
This program will detect and also recognize face

FACE DETECTION AND FACE RECOGNITION

ABSTRACT

The face is one of the easiest ways to distinguish the individual identity of each other. Face recognition is a personal identification system that uses personal characteristics of a person to identify the person's identity. Human face recognition procedure basically consists of two phases, namely face detection, where this process takes place very rapidly in humans, except under conditions where the object is located at a short distance away, the next is the introduction, which recognize a face as individuals. Stage is then replicated and developed as a model for facial image recognition (face recognition) is one of the much-studied biometrics technology and developed by experts. There are three kinds of methods that are currently popular in developed face recognition pattern namely, Eigenface method, Fisherface method and Local Binary Patterns Histograms (LBPH). Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
Keywords: Local Binary patter, OpenCV.

Extension: There is vast number of applications from this face detection project, this project can be extended that the various parts in the face can be detect which are in various directions and shapes.
 

CHAPTER-1 INTRODUCTION
The face of a human being conveys a lot of information about identity and emotional state of the person. Face recognition is an interesting and challenging problem, and impacts important applications in many areas such as identification for law enforcement, authentication for banking and security system access, and personal identification among others. In our research work mainly consists of three parts, namely face representation, feature extraction and classification. Face representation represents how to model a face and determines the successive algorithms of detection and recognition. The most useful and the face and is used to measure similarities between images. Facial expression is one of the most powerful, natural and immediate means for human beings to communicate their emotions and intensions. Face recognition is an interesting and challenging problem, and impacts important applications in many areas such as identification for law enforcement, authentication for banking and security system access, and also persona identification among other. The face plays a major role in our social intercourse in conveying identity and emotion. The human ability to recognize faces is remarkable. Modern Civilization heavily depends on person authentication for several purposes. Face recognition has always a major focus of research because of its noninvasive nature and because it is peoples primary method of person identification



Popular recognition algorithms include:

•	EigenFaces – cv2.face.createEigenFaceRecognizer()
•	FisherFaces – cv2.face.createFisherFaceRecognizer()
•	Local Binary Patterns Histograms (LBPH) – cv2.face.createLBPHFaceRecognizer()



Local binary patterns histograms (LBPH) Face Recognizer

We know that Eigenfaces and Fisherfaces are both affected by light and, in real life, we can't guarantee perfect light conditions. LBPH face recognizer is an improvement to overcome this drawback.

The idea with LBPH is not to look at the image as a whole, but instead, try to find its local structure by comparing each pixel to the neighboring pixels. 

The LBPH Face Recognizer Process
Take a 3×3 window and move it across one image. At each move (each local part of the picture), compare the pixel at the center, with its surrounding pixels. Denote the neighbors with intensity value less than or equal to the center pixel by 1 and the rest by 0.

After you read these 0/1 values under the 3×3 window in a clockwise order, you will have a binary pattern like 11100011 that is local to a particular area of the picture. When you finish doing this on the whole image, you will have a list of local binary patterns.

 
                          CHAPTER-2 TECHNOLOGY


1.	Python
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales

Use Python for…

•	Web Development: Django, Pyramid, Bottle, Tornado, Flask, web2py
•	GUI Development: tkInter, PyGObject, PyQt, PySide, Kivy, wxPython
•	Scientific and Numeric: SciPy, Pandas, IPython
•	Software Development: Buildbot, Trac, Roundup
•	System Administration: Ansible, Salt, OpenStack


2.	Machine learning
Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.
 


3.	OpenCV
OpenCV is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source BSD license 
 
                                           CHAPTER-3 PROCESS

To create a complete project on Face Recognition, we must work on 3 very distinct phases:
•	Face Detection and Data Gathering
•	Train the Recognizer
•	Face Recognition
The below block diagram resumes those phase

               

•	Face Detection
The most basic task on Face Recognition is of course, "Face Detecting". Before anything, you must "capture" a face (Phase 1) in order to recognize it, when compared with a new face captured on future (Phase 3). 
The most common way to detect a face (or any objects), is using the "Haar Cascade classifier"
Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection uses a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.
Here we will work with face detection. Initially, the algorithm needs a lot of positive images (images of faces) and negative images (images without faces) to train the classifier. Then we need to extract features from it. The good news is that OpenCV comes with a trainer as well as a detector. If you want to train your own classifier for any object like car, planes etc. you can use OpenCV to create one.
                      
•	Trainer
On this second phase, we must take all user data from our dataset and "trainer" the OpenCV Recognizer. This is done directly by a specific OpenCV function. The result will be a .yml file that will be saved on a "trainer/" directory.

                         

We will use as a recognizer, the LBPH (LOCAL BINARY PATTERNS HISTOGRAMS) Face Recognizer, included on OpenCV package. We do this in the following line:
The function "getImagesAndLabels (path)", will take all photos on directory: "dataset/", returning 2 arrays: "Ids" and "faces". With those arrays as input, we will "train our recognizer"
As a result, a file named "trainer.yml" will be saved in the trainer directory that was previously created by us.
That's it! I included the last print statement where I displayed for confirmation, the number of User's faces we have trained.
Every time that you perform Phase 1, Phase 2 must also be run

•	Recognizer
Now, we reached the final phase of our project. Here, we will capture a fresh face on our camera and if this person had his face captured and trained before

                         
We are including here a new array, so we will display "names", instead of numbered ids So, for example: Marcelo will the user with id = 1; Paula: id=2, etc.
Next, we will detect a face, same we did before with the haarCascade classifier.



