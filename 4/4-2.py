import sys
import re

values = dict()
valid = 0

def validate_byr(v):
    m = re.match(r'^(\d{4})$', v)
    return m and 1920 <= int(m[0]) <= 2002


def validate_iyr(v):
    m = re.match(r'^(\d{4})$', v)
    return m and 2010 <= int(m[0]) <= 2020


def validate_eyr(v):
    m = re.match(r'^(\d{4})$', v)
    return m and 2020 <= int(m[0]) <= 2030


def validate_hgt(v):
    m = re.match(r'^(\d+)(cm|in)$', v)
    if not m:
        return False
    if m[2] == 'in':
        return 59 <= int(m[1]) <= 76
    elif m[2] == 'cm':
        return 150 <= int(m[1]) <= 193

def validate_hcl(v):
    m = re.match(r'^#(\d|[abcdef]){6}$', v)
    return m is not None

def validate_ecl(v):
    m = re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', v)
    return m is not None

def validate_pid(v):
    m = re.match(r'^\d{9}$', v)
    return m is not None

required = {
    'byr' : validate_byr, 
    'iyr' : validate_iyr, 
    'eyr' : validate_eyr, 
    'hgt' : validate_hgt, 
    'hcl' : validate_hcl, 
    'ecl' : validate_ecl, 
    'pid' : validate_pid
}


def validate():
    for k in required:
        value = values.get(k, None)
        if value is None or not required[k](value):
            return False
    
    return True


for line in sys.stdin:
    line = line.strip()
    if not line:
        if validate():
            valid += 1
        values.clear()
        

    for pair in line.split():
        k, v = pair.split(':')
        values[k] = v

if validate():
    valid += 1

print(valid)