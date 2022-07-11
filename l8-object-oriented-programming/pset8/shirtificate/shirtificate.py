from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=48)
    pdf.cell(190, 60, "CS50 Shirtificate", align="C")
    pdf.ln()

    pdf.image("shirtificate.png", w=190)

    pdf.set_font(size=25)
    pdf.set_xy(x=0, y=130)
    pdf.set_text_color(r=255, b=255, g=255)
    pdf.cell(210, txt=f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()