import cv2



img= cv2.imread("mia.jpg",0)

cv2.imshow("mia",img)

k=cv2.waitKey(0) & 0XFF

if k == 27:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("home/nur/desktop/grimia.jpg",img)
