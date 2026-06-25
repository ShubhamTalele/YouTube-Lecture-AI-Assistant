from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


class PDFGenerator:

    @staticmethod
    def create_pdf(text, filename="lecture_notes.pdf"):

        doc = SimpleDocTemplate(filename)
        styles = getSampleStyleSheet()

        content = []

        for line in text.split("\n"):
            content.append(Paragraph(line, styles["Normal"]))
            content.append(Spacer(1, 10))

        doc.build(content)

        return filename