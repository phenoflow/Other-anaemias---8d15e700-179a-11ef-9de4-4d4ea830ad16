# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"43330.0","system":"readv2"},{"code":"30637.0","system":"readv2"},{"code":"62257.0","system":"readv2"},{"code":"48145.0","system":"readv2"},{"code":"64601.0","system":"readv2"},{"code":"16052.0","system":"readv2"},{"code":"2743.0","system":"readv2"},{"code":"45929.0","system":"readv2"},{"code":"71773.0","system":"readv2"},{"code":"72276.0","system":"readv2"},{"code":"47225.0","system":"readv2"},{"code":"94387.0","system":"readv2"},{"code":"31205.0","system":"readv2"},{"code":"31550.0","system":"readv2"},{"code":"15936.0","system":"readv2"},{"code":"16929.0","system":"readv2"},{"code":"41699.0","system":"readv2"},{"code":"70732.0","system":"readv2"},{"code":"25394.0","system":"readv2"},{"code":"12176.0","system":"readv2"},{"code":"104812.0","system":"readv2"},{"code":"31040.0","system":"readv2"},{"code":"2452.0","system":"readv2"},{"code":"53422.0","system":"readv2"},{"code":"56752.0","system":"readv2"},{"code":"33278.0","system":"readv2"},{"code":"70835.0","system":"readv2"},{"code":"D64","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-anaemias-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["anaemias---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["anaemias---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["anaemias---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
