from PIL import Image 
import pytesseract

#I'm in windows, so for checking the exe of my tesseract for avoiding errors, i had to add this little line:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Getting the image
img = Image.open("./images/testImage_2.jpg") 

#Converting the image to a result
result = pytesseract.image_to_string(img)

#Exporting the results
with open("./text/text_result_2.txt", mode = "w") as file:
    file.write(result)
    print("The text of the image has been printed into the txt file in the folder called \"text\".")

    