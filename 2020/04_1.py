import pathlib

file_name = "04.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    passports = file.readlines()

passport_data_list = []
current_passport = {}
for passport in passports:
    if passport == "\n":
        passport_data_list.append(current_passport)
        current_passport = {}
    else:
        passport_data = passport.split()
        for data in passport_data:
            key, value = data.split(":")
            current_passport[key] = value
passport_data_list.append(current_passport)

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

correct_passports = 0
for passport in passport_data_list:
    missing_fields = []
    for field in fields:
        if field not in passport.keys():
            missing_fields.append(field)
    if len(missing_fields) == 0 or len(missing_fields) == 1 and missing_fields[0]=="cid":
        correct_passports +=1
    print(f"p:{passport} - {missing_fields}")

print(f"Correct: {correct_passports}")

