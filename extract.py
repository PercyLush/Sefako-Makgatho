import PyPDF2

path = "C:\\Users\\Bheki Lushaba\\Downloads\\School-of-Science-and-Technology-Calendar-2020.pdf"

with open(path, "rb") as file1:
    data = PyPDF2.PdfReader(file1)

    Text = ""

    for page in range(32, 157):
        pages = data.pages[page]
        File_Text = pages.extract_text()
        Text += File_Text

with open("C:\\Users\\Bheki Lushaba\\Desktop\\Sefako Makgatho\\ScienceAndTech.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)
