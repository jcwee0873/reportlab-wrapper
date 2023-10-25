#-*- coding: utf-8 -*-
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from report_writer.utils import get_default_kor_font, get_font_list

class PDFCanvas:
    def __init__(
        self,
        report_path: str | None = None,
        page_size: str = 'A4',
        page_compression: bool = False
    ) -> None:
        """
        Canvas

        Parameters
        ----------
        report_path: str
             Controls the name of the final PDF file.
        page_size: enum
            A0 ~ A10, B0 ~ B10, C0 ~ C10, LETTER, LEGAL, ELEVENSEVENTEEN. Default: A4
        page_comporession: bool
             Whether the stream of PDF operations for each page is compressed. Default: False 

        Returns
        -------
        None
        """
        if not report_path:
            report_path = os.path.dirname(__file__)
            report_path = os.path.join(report_path, '../..', 'ormas_report.pdf')
            report_path = os.path.abspath(report_path)
        
        self.report_path = report_path

        self.canvas = canvas.Canvas(
            report_path,
            pagesize=eval(page_size),
            bottomup=1,
            pageCompression=int(page_compression),
            initialFontName=None,
            initialFontSize=None,
            initialLeading=None,
            cropBox=None,
            artBox=None,
            trimBox=None,
            bleedBox=None,
            lang=None
        )
    

        pdfmetrics.registerFont(TTFont('DefaultKor', get_default_kor_font()))

    def draw_cover(self):
        """
        """
