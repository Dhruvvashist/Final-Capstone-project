import glob
import os
import cv2
from random import randrange
a=0
b=3
videos=[]
final=[]
if a==0:
    for name in glob.glob("C:/Users/hp/Desktop/AD/male/*"):
        videos.append(name)

print(videos[b])
dir=videos[b]

for entry in os.scandir(dir):
    if entry.path.endswith(".mp4") and entry.is_file():
        final.append(entry.path)

random_index=randrange(len(final))
print(final[random_index])

cap = cv2.VideoCapture(final[random_index])
   
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break

cap.release()
cv2.destroyAllWindows()
