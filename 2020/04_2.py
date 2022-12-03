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
ecl_acceptable = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
hcl_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

correct_passports = 0
for passport in passport_data_list:
    missing_fields = []
    for field in fields:
        if field not in passport.keys():
            missing_fields.append(field)
    if len(missing_fields) == 0 or len(missing_fields) == 1 and missing_fields[0]=="cid":
        # check field values:
        passport_ok = True
        for field in fields:
            try:
                value = passport[field]
            except KeyError:
                if field == "cid":
                    pass
                else:
                    passport_ok = False
            if field == "byr":
                if len(value) != 4:
                    passport_ok = False
                if int(value) < 1920 or int(value) > 2002:
                    passport_ok = False
            if field == "iyr":
                if len(value) != 4:
                    passport_ok = False
                if int(value) < 2010 or int(value) > 2020:
                    passport_ok = False
            if field == "eyr":
                if len(value) != 4:
                    passport_ok = False
                if int(value) < 2020 or int(value) > 2030:
                    passport_ok = False
            if field == "hgt":
                if value[-2:] == "cm":
                    if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                        passport_ok = False
                elif value[-2:] == "in":
                    if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                        passport_ok = False
                else:
                    passport_ok = False
            if field == "hcl":
                if value[0] != "#":
                    passport_ok = False
                if len(value) != 7:
                    passport_ok = False
                hcl = list(value[1:])
                for digit in hcl:
                    if digit not in hcl_digits:
                        passport_ok = False
            if field == "ecl":
                if value not in ecl_acceptable:
                    passport_ok = False
            if field == "pid":
                if len(value) != 9:
                    passport_ok = False
                try:
                    value_int = int(value)
                except:
                    passport_ok = False
        if passport_ok:
            correct_passports +=1

print(f"Correct: {correct_passports}")

