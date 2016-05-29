# cs229_emotion_detection

SETUP:
$ sudo pip install --upgrade google-api-python-client

reference paper:
http://cs229.stanford.edu/proj2014/Matthew%20Wang,%20Spencer%20Yee,%20Determining%20Mood%20From%20Facial%20Expressions.pdf

Hey Theo!! Hope the convention is going well and you are meeting lots of long-lost sisters! 
-----------------------------------------------------------------------------------------------------------
Progress report:

We learned that the coordinates returned by the Google API were referenced by the entire original image, so now the process is modified to first crop out the facial region before getting the landmarks. We may think about normalizing/shifting the vectors to be centered around the eyes or nose. Right now the normalizing just readjusts the x and y coordinates so that they are always referenced to a 250x250 square image. 

Despite having accurate and consistent feature vectors now for all the facial landmarks, the SVM results are still really bad (4/65 correct). We're now thinking the primary way to improve is to start implementing angles between landmarks as those are a lot more representative of emotions. (eg. angle between chin and left/right edge of lip) The problem with just distance is that facial structures aren't at all consistent and capture very little information regarding emotion. 

Oh also sidenote I figured out how to save and load the feature vectors to and from a text file, so now we don't have to run google's api all the time. 

TODO: 

Add relevant angles between landmarks to our feature vector. 
