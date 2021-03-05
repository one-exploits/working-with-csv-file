import csv
import smtplib
def parse_name_email(fpath):
    names=[];
    emailes=[];
    with open(fpath,"r") as fp:
        data_in_list=list(csv.reader(fp));
        for user in data_in_list:
            names.append(user[2])
            emailes.append(user[3]);
        return names,emailes;
        
n,e=parse_name_email("data.csv");
print(n,e);