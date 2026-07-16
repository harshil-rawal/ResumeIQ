from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
    KeepTogether
)

# ---------------------------------------------------------------------------
# Palette — a restrained, professional indigo/slate scheme
# ---------------------------------------------------------------------------
NAVY = colors.HexColor("#1E2333")        # near-black slate, primary text / headers
INDIGO = colors.HexColor("#4F46E5")      # primary accent (replaces flat purple)
INDIGO_DARK = colors.HexColor("#3730A9") # darker accent for emphasis
SLATE = colors.HexColor("#475569")       # secondary text
SLATE_LIGHT = colors.HexColor("#94A3B8") # muted / captions
BORDER = colors.HexColor("#E2E8F0")      # hairline borders
ROW_ALT = colors.HexColor("#F8FAFC")     # zebra striping
CARD_BG = colors.HexColor("#EEF2FF")     # soft indigo tint for the score card
GOOD = colors.HexColor("#059669")        # green — excellent/good
WARN = colors.HexColor("#D97706")        # amber — average
BAD = colors.HexColor("#DC2626")         # red — needs improvement


def _build_styles():
    """Central place for every custom paragraph style used in the report."""
    base = getSampleStyleSheet()

    styles = {}

    styles["brand"] = ParagraphStyle(
        "brand", parent=base["Title"],
        fontName="Helvetica-Bold", fontSize=24, leading=28,
        textColor=NAVY, alignment=TA_LEFT, spaceAfter=2
    )

    styles["tagline"] = ParagraphStyle(
        "tagline", parent=base["Normal"],
        fontName="Helvetica", fontSize=11.5, leading=14,
        textColor=SLATE, alignment=TA_LEFT, spaceAfter=2
    )

    styles["meta"] = ParagraphStyle(
        "meta", parent=base["Normal"],
        fontName="Helvetica", fontSize=9, leading=12,
        textColor=SLATE_LIGHT, alignment=TA_LEFT
    )

    styles["section_heading"] = ParagraphStyle(
        "section_heading", parent=base["Heading1"],
        fontName="Helvetica-Bold", fontSize=14, leading=18,
        textColor=NAVY, spaceBefore=0, spaceAfter=0
    )

    styles["score_number"] = ParagraphStyle(
        "score_number", parent=base["Title"],
        fontName="Helvetica-Bold", fontSize=40, leading=44,
        alignment=TA_CENTER, textColor=INDIGO
    )

    styles["score_caption"] = ParagraphStyle(
        "score_caption", parent=base["Normal"],
        fontName="Helvetica", fontSize=9.5, leading=12,
        alignment=TA_CENTER, textColor=SLATE_LIGHT
    )

    styles["status_pill"] = ParagraphStyle(
        "status_pill", parent=base["Normal"],
        fontName="Helvetica-Bold", fontSize=12, leading=16,
        alignment=TA_CENTER
    )

    styles["category_label"] = ParagraphStyle(
        "category_label", parent=base["Heading2"],
        fontName="Helvetica-Bold", fontSize=11, leading=15,
        textColor=INDIGO_DARK, spaceBefore=10, spaceAfter=3
    )

    styles["body"] = ParagraphStyle(
        "body", parent=base["BodyText"],
        fontName="Helvetica", fontSize=10.5, leading=16,
        textColor=NAVY
    )

    styles["skill_list"] = ParagraphStyle(
        "skill_list", parent=base["BodyText"],
        fontName="Helvetica", fontSize=10, leading=15,
        textColor=SLATE
    )

    styles["missing_item"] = ParagraphStyle(
        "missing_item", parent=base["BodyText"],
        fontName="Helvetica", fontSize=10.5, leading=17,
        textColor=NAVY, leftIndent=4
    )

    styles["footer"] = ParagraphStyle(
        "footer", parent=base["Normal"],
        fontName="Helvetica", fontSize=8.5, leading=11,
        textColor=SLATE_LIGHT, alignment=TA_CENTER
    )

    return styles


def _status_for_score(score):
    """Returns (label, color) for a given ATS score."""
    if score >= 85:
        return "Excellent ATS Compatibility", GOOD
    elif score >= 70:
        return "Good ATS Compatibility", GOOD
    elif score >= 50:
        return "Average ATS Compatibility", WARN
    else:
        return "Needs Improvement", BAD


def _section_header(elements, styles, title):
    """A consistent, branded heading used above every major section."""
    bar_and_title = Table(
        [[Paragraph(title, styles["section_heading"])]],
        colWidths=[440]
    )
    bar_and_title.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LINEBEFORE", (0, 0), (0, 0), 3, INDIGO),
    ]))
    elements.append(
        KeepTogether([
            bar_and_title,
            HRFlowable(width="100%", thickness=0.75, color=BORDER, spaceAfter=14),
        ])
    )


def add_header(elements, styles):

    elements.append(Paragraph("ResumeIQ", styles["brand"]))
    elements.append(Paragraph("AI Resume Analysis Report", styles["tagline"]))
    elements.append(Spacer(1, 4))
    elements.append(
        Paragraph(
            f"Generated on {datetime.now().strftime('%d %b %Y')}",
            styles["meta"]
        )
    )

    elements.append(Spacer(1, 10))
    elements.append(HRFlowable(width="100%", thickness=1.2, color=NAVY, spaceAfter=22))


def add_ats_summary(elements, styles, report):

    score = report["ats"]["overall_score"]
    status, status_color = _status_for_score(score)

    _section_header(elements, styles, "Overall ATS Score")

    # --- Score card: number, status pill, and a proportional progress bar ---
    filled_width = max(0, min(100, score)) * 3.6  # out of 360pt track
    empty_width = 360 - filled_width

    if filled_width > 0 and empty_width > 0:
        bar_table = Table([["", ""]], colWidths=[filled_width, empty_width], rowHeights=[7])
        bar_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), INDIGO),
            ("BACKGROUND", (1, 0), (1, 0), BORDER),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))
    else:
        fill_color = INDIGO if filled_width > 0 else BORDER
        bar_table = Table([[""]], colWidths=[360], rowHeights=[7])
        bar_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), fill_color),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ]))

    status_hex = "#" + status_color.hexval()[2:]
    status_para = Paragraph(
        f'<font color="{status_hex}">{status}</font>',
        styles["status_pill"]
    )

    card_inner = [
        [Paragraph(f"{score}/100", styles["score_number"])],
        [Paragraph("OVERALL SCORE", styles["score_caption"])],
        [Spacer(1, 8)],
        [bar_table],
        [Spacer(1, 10)],
        [status_para],
    ]

    card = Table(card_inner, colWidths=[400])
    card.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, 0), 18),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 18),
        ("LEFTPADDING", (0, 0), (-1, -1), 30),
        ("RIGHTPADDING", (0, 0), (-1, -1), 30),
        ("BOX", (0, 0), (-1, -1), 1, BORDER),
    ]))

    elements.append(card)
    elements.append(Spacer(1, 22))

    # --- Breakdown table ---
    breakdown = report["ats"]["breakdown"]

    table_data = [["Metric", "Score"]]

    for metric, values in breakdown.items():
        table_data.append([
            metric.replace("_", " ").title(),
            f"{values['score']}/{values['max']}"
        ])

    table = Table(table_data, colWidths=[320, 100])

    row_styles = []
    for i in range(1, len(table_data)):
        if i % 2 == 0:
            row_styles.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, 0), 10),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 1), (-1, -1), 10),
            ("TEXTCOLOR", (0, 1), (-1, -1), NAVY),
            ("ALIGN", (1, 0), (-1, -1), "CENTER"),
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            ("LINEBELOW", (0, 0), (-1, 0), 0.75, NAVY),
            ("LINEBELOW", (0, 1), (-1, -2), 0.5, BORDER),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            *row_styles,
        ])
    )

    elements.append(table)
    elements.append(Spacer(1, 28))


def add_career_domains(elements, styles, report):

    _section_header(elements, styles, "Detected Career Domains")

    domains = report["ats"]["detected_domains"]

    table_data = [["Career Domain", "Confidence"]]

    for domain_name, domain in domains.items():
        table_data.append([
            domain_name,
            f"{int(domain['confidence']*100)}%"
        ])

    table = Table(table_data, colWidths=[340, 80])

    row_styles = []
    for i in range(1, len(table_data)):
        if i % 2 == 0:
            row_styles.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INDIGO),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 10),
        ("TEXTCOLOR", (0, 1), (-1, -1), NAVY),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        *row_styles,
    ]))

    elements.append(table)
    elements.append(Spacer(1, 28))


def add_detected_skills(elements, styles, report):

    _section_header(elements, styles, "Detected Skills")

    skills = report["skills"]

    for category, skill_list in skills.items():

        if not skill_list:
            continue

        chips = " &nbsp;&middot;&nbsp; ".join(skill_list)
        block = [
            Paragraph(category, styles["category_label"]),
            Paragraph(chips, styles["skill_list"]),
            Spacer(1, 6),
        ]
        elements.append(KeepTogether(block))

    elements.append(Spacer(1, 12))


def add_missing_skills(elements, styles, report):

    _section_header(elements, styles, "Top Missing Skills")

    missing = report["top_missing_skills"]

    if not missing:
        elements.append(
            Paragraph("No major missing skills detected.", styles["body"])
        )
        elements.append(Spacer(1, 15))
        return

    for skill in missing:
        elements.append(
            Paragraph(
                f'<font color="#DC2626">&#9679;</font>&nbsp;&nbsp;{skill["skill"]}',
                styles["missing_item"]
            )
        )

    elements.append(Spacer(1, 18))


def add_ai_summary(elements, styles, report):

    _section_header(elements, styles, "AI Career Coach Summary")

    summary_table = Table(
        [[Paragraph(report["ai_feedback"]["summary"], styles["body"])]],
        colWidths=[460]
    )
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), ROW_ALT),
        ("BOX", (0, 0), (-1, -1), 0.75, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 14),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 14),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
    ]))

    elements.append(summary_table)


def _footer_canvas(canvas, doc):
    """Draws a slim branded footer with a live page number on every page."""
    canvas.saveState()
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(0.85 * inch, 0.65 * inch, letter[0] - 0.85 * inch, 0.65 * inch)

    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(SLATE_LIGHT)
    canvas.drawString(0.85 * inch, 0.5 * inch, "Generated by ResumeIQ \u2022 AI Resume Analysis Report")
    canvas.drawRightString(letter[0] - 0.85 * inch, 0.5 * inch, f"Page {doc.page}")
    canvas.restoreState()


def generate_pdf_report(report, output_path):

    styles = _build_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=0.85 * inch,
        bottomMargin=0.95 * inch,
        leftMargin=0.85 * inch,
        rightMargin=0.85 * inch,
    )

    elements = []

    add_header(elements, styles)

    add_ats_summary(elements, styles, report)

    if report["ats"]["detected_domains"]:
        add_career_domains(elements, styles, report)

    if any(report["skills"].values()):
        add_detected_skills(elements, styles, report)

    if report["top_missing_skills"]:
        add_missing_skills(elements, styles, report)

    add_ai_summary(elements, styles, report)

    doc.build(elements, onFirstPage=_footer_canvas, onLaterPages=_footer_canvas)