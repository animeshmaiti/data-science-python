# convert tsv file to csv
import csv

tsv_file = "five-years.tsv"
csv_file = "output.csv"

with open(tsv_file, "r", encoding="utf-8") as tsv_in, open(csv_file, "w", encoding="utf-8", newline="") as csv_out:
    tsv_reader = csv.reader(tsv_in, delimiter="\t")
    csv_writer = csv.writer(csv_out, delimiter=",")

    for row in tsv_reader:
        csv_writer.writerow(row)
