import datetime as ts
# import cv2
import edgenum as en
from edgenum import edgenum
img = "C:/Users/user/Downloads/g2.jpg/"
tweet = en.edgenum(img)
dt1 = ts.datetime(2022, 11, 26, 12, 25, 29, 674107)


timedf = tweet[0]-dt1
print(tweet)
diff_in_minutes = timedf.total_seconds() / 60
if diff_in_minutes <= 60:
    Amount = 20
elif diff_in_minutes > 60 and diff_in_minutes <= 120:
    amount = 30
elif diff_in_minutes > 120 and diff_in_minutes <= 180:
    amount = 40
elif diff_in_minutes > 180:
    amount = 50

beepboop = True

while beepboop is True:
    csr = str(input(f"Vehicle number {tweet[1]}, Parking system has requested {amount} rupees. A/R: "))
    if csr.casefold() == "a":
        print("Paymted received, exit gate opened.")
        beepboop = False
        break
    elif csr.casefold() == "r":
        print("Payment rejected, please try again.")


