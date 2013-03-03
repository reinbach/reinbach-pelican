Title: reportlab colors
Date: 2011-08-19
Tags: python
Slug: reportlab-colors
Author: Greg Reinbach

I was working on generating PDFs using ReportLab today, and I was wanting to change the background and text color of a few cells within a table.


    data = [
        [total_due, total_amount, '', 'BRAND', merchant],
        ['', '', '', 'DATE', datetime.date.today().strftime("%m/%d/%Y")],
        ['', '', '', 'ORDER NUMBER', order.order.order_number],
    ]
    t = Table(data, style=[
        # left side
        ('GRID', (0, 0), (1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, 0), (0, -1), HIGHLIGHT_BACKGROUND_COLOR),
        ('TEXTCOLOR', (0, 0), (0, -1), HIGHLIGHT_TEXT_COLOR),
        ('ALIGN', (0, 0), (-2, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-2, -2), 'MIDDLE'),
        ('SPAN', (0, 0), (0, -1)),
        ('SPAN', (1, 0), (1, -1)),
        # right side
        ('GRID', (-2, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (-2, 0), (-2, -1), HIGHLIGHT_BACKGROUND_COLOR),
        ('TEXTCOLOR', (-2, 0), (-2, -1), HIGHLIGHT_TEXT_COLOR),
    ])


In the above the 'total_due' value appears in the first cell of the table and I was wanting the first 'TEXTCOLOR' assignment to change the text color of that cell. Like it was for the second 'TEXTCOLOR' assignment.

The second assignment was working and setting the text color correctly, but not the first. WTF!

It finally dawned on me to see where/how 'total_due' was being set, and that pretty much solved it. As it was being set with the following;


    total_due = Paragraph("TOTAL DUE", styles['Right-Bold'])


So style['Right-Bold'] had a textColor attribute, so setting that to the color I wanted and we were good.


    styles['Right-Bold'].textColor = colors.HexColor('#1b78d5')
