#!/bin/bash

foldername=program-$(date +"%y-%m-%d")
mkdir h1programs 2>/dev/null
mkdir ./h1programs/$foldername/ 2>/dev/null
echo "[+]Scraping programs...."
python geth1programs.py > ./h1programs/$foldername/program_list.txt
nb_prog=wc -l ./h1programs/$foldername/program_list.txt
echo "$nb_prog scraped."
echo "[+]Scraping URLs...."
for prog in $(cat ./h1programs/$foldername/program_list.txt)
do
	python geth1urls.py $prog > ./h1programs/$foldername/$prog.txt
done
echo "[+]Done"



