#!/bin/bash
for file in *.svg
do
  echo $file
  filename=$(basename "$file")
  fname="${filename%.*}"
  ext="${filename##*.}"

  echo "Input File: $file"
#  echo "Filename without Path: $filename"
#  echo "Filename without Extension: $fname"
#  echo "File Extension without Name: $ext"

  #flatext=".svg.flat"
  #fileflat=$fname$flatext
  #echo "New name:$fileflat"

  # Go to flat style: remove shadow style
  # Pb: boundary of blocks are not visible; example 2+3x4
  #sed "s/filter:url([^)]*)/ /g" $file > $fileflat
  
  pdfext=".pdf"
  filepdf=$fname$pdfext

  echo "pdf name:$filepdf"

  # Convert to pdf
  inkscape $file --export-dpi=400 --export-pdf=$filepdf
done



