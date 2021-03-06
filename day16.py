import sys
from math import prod

#lines = list(map(str.rstrip, open("%s_sample2.txt" % sys.argv[0].split('.')[0], "r").readlines()))
lines = list(map(str.rstrip, open("%s_input.txt" % sys.argv[0].split('.')[0], "r").readlines()))

# Read input
fields_range = {}
i = 0
while lines[i] != "":
    field, values = lines[i].split(": ")
    fields_range[field] = [tuple(map(int, v.split("-"))) for v in values.split(" or ")]
    i += 1
my_ticket = list(map(int, lines[i + 2].split(",")))
nearby_tickets = [] 
i += 5
while i < len(lines):
    nearby_tickets.append(list(map(int, lines[i].split(","))))
    i += 1

def value_in_range(value, field_range):
    return field_range[0][0] <= value <= field_range[0][1] or field_range[1][0] <= value <= field_range[1][1]
    
def values_not_in_ranges(value):
    for field_range in fields_range.values():
        if value_in_range(value, field_range):
            return False
    return True

def invalid_fields(ticket):
    return list(filter(values_not_in_ranges, ticket))

def is_valid(ticket):
    return all(map(lambda v: not(values_not_in_ranges(v)), ticket))

# ex 1 
print("Ex1: %d" % sum(map(sum, map(invalid_fields, nearby_tickets))))


# ex 2
valid_nearby_tickets = list(filter(is_valid, nearby_tickets))
unsolved_cols = list(fields_range.keys())
cols = {}

while len(unsolved_cols) > 0:
    #print(unsolved_cols)
    for field in unsolved_cols:
        matchs = 0
        matched_col = 0
        for col in range(len(my_ticket)):
            if col not in cols.values():
                if all(map(lambda v: value_in_range(v[col], fields_range[field]), valid_nearby_tickets + [my_ticket])):
                    matchs += 1
                    matched_col = col
        if matchs == 1:
            cols[field] = matched_col
            unsolved_cols.remove(field)
            break

product = 1
for f in filter(lambda x: x.startswith('departure'), cols):
    product *= my_ticket[cols[f]]

print("Ex2: %d" % product)