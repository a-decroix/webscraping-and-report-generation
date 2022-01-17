#!/bin/bash

rm results.txt
python BreakawayNews.py
rm searchdoc.docx
pandoc results.txt --output searchdoc.docx
open searchdoc.docx


