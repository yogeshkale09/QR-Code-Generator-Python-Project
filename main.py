"""
    1) take upi id of user.
    2) defined payment url for every transaction
    3) for every payment it will generate unique payment QR code using qrcode.make function
    4) you can save generated qr code in your system
    5) Display  QR code
"""

import qrcode


#Taking UPI ID as a input

upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID%apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Define the payment URL based on the UPI ID and the payment app
#You can modify these URLS based on the payment apps you want to support

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR code for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the QR code to image file

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')


#Display the QR codes(you may need to install PIL/pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()