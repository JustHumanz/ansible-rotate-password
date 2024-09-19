import csv,yaml,argparse,os,secrets,time
from collections import defaultdict
from pathlib import Path

password_length = 26

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--File", help = "Select CSV file")
parser.add_argument("-g", "--Generate", help = "Use&Generate random password", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

if args.File == None:
    print("Must input csv file")
    os._exit(1)
    
vm_domain = defaultdict(list)
with open(args.File, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    generated_csv = None
    
    if args.Generate:
        generated_pass = open(f'{int(time.time())}-{args.File}', 'w')
        generated_csv = csv.DictWriter(generated_pass, fieldnames=csv_reader.fieldnames)
        generated_csv.writeheader()
        
    for row in csv_reader:
        if args.Generate:  
            rand_passwd = secrets.token_urlsafe(password_length)
            row["password"] = rand_passwd
            generated_csv.writerow({'username': row["username"], "password": row["password"],"vm name": row["vm name"]})
            
        vm_domain[row["vm name"]].append({"username": row["username"],"password": row["password"]})
    
for vm_name in vm_domain:
    Path(f"vars/{vm_name}").mkdir(parents=True, exist_ok=True)
    
    data = dict(
        user_list = vm_domain[vm_name],
    )
    
    with open(f"vars/{vm_name}/user_list.yaml", 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)