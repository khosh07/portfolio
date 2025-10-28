---

title: Digitization

permalink: /digitization/

layout: page

image: images/Treatiesbanner.jpg

---

# Introduction to the Digitization Project.

## Goal of the Mini-Project

 The aim of this mini-project in digitalization was to acquire practical experience in the work processes and problematic issues of turning printed historical content into digital, searchable forms. The project allowed me to understand how every step of digitization, such as scanning and image processing, Optical Character Recognition (OCR), and text correction, allows preserving and making cultural heritage materials accessible. The project was created to enhance our knowledge of technical, ethical, and archival concerns of converting usable digital resources of physical books. Finally, it was not only necessary to make a digital copy of a rare text but also to report the working process, analyse the OCR quality, and think critically about the tools and methods used. 

## The Book We Digitized
 
The book that we scanned is entitled “هفت باب بابا سیّدنا و مطلوبُ الموءمنین” Haft Baba Baba Sayyidnana wa Matloub-ul-Mu’miniyin. Published in Bombay in 1933 CE (1352 AH), it has 82 pages. This work contains a brief discourse on the theology and philosophy of the Ismaelites, which is expressed in two brief texts. The historical and religious value of the book and its linguistic and typographic peculiarities turned it into an interesting object of digitization. The fact that it uses Persian and Arabic writing also posed fascinating challenges to the OCR precision and layout analysis.

## The Scanning Process
 
The scanning process entailed making good-quality digital copies of every page without destroying the physical shape of the book. I was able to use a scanner so that there is minimal distortion and even lighting on all the pages. All scans were stored in JPG format in order to preserve lossless images. I also made small readjustments on the pages after scanning, such as cropping and contrast correction, to improve the page for optimized OCR processing. The primary difficulty was to make fine details of the script visible, particularly the diacritics and the flourishes of the calligraphy. The last image set gave a consistent basis for correct text identification during the next OCR step.

## The OCR process
 
Four transcription models, developed by Kraken for Arabic and Persian scripts, were tested on a three-page sample from the book.  Their performance, represented by CER (Character Error Rate) and WER (Word Error Rate) values, was measured with the use of a Python script developed by instructors and students at the AKU-ISMC. The script also includes normalization tables, which are used to further qualify the WER and CER results. Based on another Python script (built with the assistance of ChatGPT) involving basic and easily replicable functions – such as split and len– the highest-performing transcription model was concluded to be kraken-gen2-print-n7m5-union-ft_best. The results were then authenticated against calculations made on an Excel spreadsheet.






