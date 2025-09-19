from fpdf import FPDF

def get_name():
    name = input("whats your name: ")
    return name

def print_name(name):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_margin(0)
    pdf.add_page()

    pdf.set_font("helvetica", size=30)
    pdf.set_x(60)
    pdf.cell(210, 10,"CS50 Shirtificate" )
    pdf.ln(25)

    pdf.image("shirtificate.png")

    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)

    pdf.set_y(100)
    pdf.cell(210, 10, f"{name} took CS50", align='C')

    pdf.output("shirtificate.pdf")

def main():
    name = get_name()
    print_name(name)

if __name__ == "__main__":
    main()
