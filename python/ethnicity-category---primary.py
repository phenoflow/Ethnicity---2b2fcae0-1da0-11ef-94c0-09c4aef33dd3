# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Ian Buchan, Mamas A Mamas, Naveed Sattar, Darren M Ashcroft, Martin M Rutter, 2024.

import sys, csv, re

codes = [{"code":"9iF9.00","system":"readv2"},{"code":"9iA5.00","system":"readv2"},{"code":"9iF1.00","system":"readv2"},{"code":"9i20.00","system":"readv2"},{"code":"9i2E.00","system":"readv2"},{"code":"9i2H.00","system":"readv2"},{"code":"9iD0.00","system":"readv2"},{"code":"9iF3.00","system":"readv2"},{"code":"9i2K.00","system":"readv2"},{"code":"9iF2.00","system":"readv2"},{"code":"9i22.00","system":"readv2"},{"code":"9i2F.00","system":"readv2"},{"code":"9i2J.00","system":"readv2"},{"code":"9iFE.00","system":"readv2"},{"code":"9iD1.00","system":"readv2"},{"code":"9iA6.00","system":"readv2"},{"code":"9iA4.00","system":"readv2"},{"code":"9iFJ.00","system":"readv2"},{"code":"9iFB.00","system":"readv2"},{"code":"9i2B.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ethnicity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ethnicity-category---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ethnicity-category---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ethnicity-category---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
