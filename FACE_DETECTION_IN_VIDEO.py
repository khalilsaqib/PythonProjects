#Detect FAce from Video
import cv2,pandas
from datetime import datetime
cap=cv2.VideoCapture(0)
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start","End"])
while True:
	face_cascade=cv2.CascadeClassifier(r"D:\PYTHON PROJECTS\IMG-VID PROCESSING USING PYTHON\haarcascade_frontalface_default.xml")
	ret,frame=cap.read()
	status=0
	gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	if ret==False:
		continue
	faces=face_cascade.detectMultiScale(gray_frame,1.3,5)
	#cv2.imshow("Frame",frame)
	#cv2.imshow("GrayFrame",gray_frame)
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		status=1
	status_list.append(status)
	status_list=status_list[-2:]
	if status_list[-1]==1 and status_list[-2]==0:
		times.append(datetime.now())
	if status_list[-1]==0 and status_list[-2]==1:
		times.append(datetime.now())

	cv2.imshow("Frame",frame)
	key_pressed=cv2.waitKey(1) & 0xFF
	if key_pressed==ord('q'):
		if status==1:
			times.append(datetime.now())
		break
print(status_list)
print(times)

for i in range(0,len(times),2):
	df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)
	df.to_csv("Times.csv")

cap.release()
cv2.destroyAllWindows()
