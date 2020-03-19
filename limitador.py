import csv

with open('pruebax.csv') as  csv_archivo:
    csv_reader= csv.reader(csv_archivo, delimiter=',')
    line_count = 0
    f = open("sqlfile.txt", "a")
    for row in csv_reader:
        if line_count == 0:
            f.write(f'INSERT INTO myTable((",".join(row))) VALUES \n')
            line_count +=1
        else:
            f.write(f'(\' (row[0])\',\'(row[1])\',\'(row[2])\',\'(row[3])\'), \n')
            line_count +=1
print(f'Processed (line_count) lines.')
