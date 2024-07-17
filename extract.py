import PyPDF2

path = "C:\\Users\\Bheki Lushaba\\Downloads\\School-of-Medicine-Calendar-2021-Revised-04-April-2021-Final (1).pdf"

with open(path, "rb") as file1:
    data = PyPDF2.PdfReader(file1)

    Text = ""

    for page in range(124, 140):
        pages = data.pages[page]
        File_Text = pages.extract_text()
        Text += File_Text

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\MedicineDescriptions.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)
