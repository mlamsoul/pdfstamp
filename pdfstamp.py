import pymupdf
from pymupdf import Document, Page

def ajouter_tampon_et_marque(pdf_entree: str, pdf_sortie: str, tampon_texte: str, marque_texte: str):
    doc: Document = pymupdf.open(pdf_entree)
    page: Page = doc[0]  # première page

    # Dimensions de la page
    largeur_page: float = page.rect.width

    # --- TAMPON ROUGE ---
    page.insert_text(  # type: ignore[attr-defined]
        pymupdf.Point(40, 40),  # position (gauche, haut)
        tampon_texte,
        fontname="helv",
        fontsize=11,
        fill=(1, 0, 0),  # rouge
        render_mode=0
    )

    # --- MARQUAGE NOIR SUR FOND NOIR ---
    largeur_marque = 120
    hauteur_marque = 20
    x_marque = largeur_page - largeur_marque - 100  # position x ajustable
    y_marque = 35

    # Dessin d'un rectangle noir
    rect = pymupdf.Rect(x_marque, y_marque, x_marque + largeur_marque, y_marque + hauteur_marque)
    page.draw_rect(rect, color=(0, 0, 0), fill=(0, 0, 0))    # type: ignore[attr-defined]

    # Texte blanc sur fond noir
    page.insert_textbox(   # type: ignore[attr-defined]
        rect,
        marque_texte,
        fontname="helv",
        fontsize=11,
        align=1,  # centré
        fill=(1, 1, 1)
    )

    # Sauvegarde
    doc.save(pdf_sortie)
    doc.close()

# --- Exemple d'utilisation ---
ajouter_tampon_et_marque(
    pdf_entree="loremipsum.pdf",
    pdf_sortie="loremipsum-stamped.pdf",
    tampon_texte="Investissement Société\nHub pour laptop",
    marque_texte="Fr-2025_01_011"
)
