# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"53799.0","system":"readv2"},{"code":"3981.0","system":"readv2"},{"code":"59103.0","system":"readv2"},{"code":"35160.0","system":"readv2"},{"code":"24953.0","system":"readv2"},{"code":"11961.0","system":"readv2"},{"code":"58695.0","system":"readv2"},{"code":"34934.0","system":"readv2"},{"code":"797.0","system":"readv2"},{"code":"10506.0","system":"readv2"},{"code":"99494.0","system":"readv2"},{"code":"4670.0","system":"readv2"},{"code":"3942.0","system":"readv2"},{"code":"5833.0","system":"readv2"},{"code":"8054.0","system":"readv2"},{"code":"57274.0","system":"readv2"},{"code":"58136.0","system":"readv2"},{"code":"882.0","system":"readv2"},{"code":"539.0","system":"readv2"},{"code":"28768.0","system":"readv2"},{"code":"51489.0","system":"readv2"},{"code":"739.0","system":"readv2"},{"code":"99222.0","system":"readv2"},{"code":"31248.0","system":"readv2"},{"code":"56348.0","system":"readv2"},{"code":"51169.0","system":"readv2"},{"code":"1702.0","system":"readv2"},{"code":"25876.0","system":"readv2"},{"code":"26327.0","system":"readv2"},{"code":"37539.0","system":"readv2"},{"code":"71840.0","system":"readv2"},{"code":"100576.0","system":"readv2"},{"code":"40750.0","system":"readv2"},{"code":"4475.0","system":"readv2"},{"code":"4839.0","system":"readv2"},{"code":"35749.0","system":"readv2"},{"code":"7841.0","system":"readv2"},{"code":"3265.0","system":"readv2"},{"code":"92106.0","system":"readv2"},{"code":"19574.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('other-anaemias-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["possible-other-anaemias---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["possible-other-anaemias---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["possible-other-anaemias---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
