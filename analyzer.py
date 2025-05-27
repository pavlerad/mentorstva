import re

with open('logs_regex/http.log', "r") as file:
    lines = file.readlines()

print(lines)


#pattern = r"Error \d{3}"

#re.findall(pattern, lines)


#for line in lines:
 #   match = re.search(pattern, line)
  #  if match:
   #     print(line)



error_pattern = r"Error \d{3}"



for line in lines:
    match = re.search(error_pattern, line)
    if match:
        print(line)


status_pattern = r"Status \d{3}"

# ISTO OVAKO: with open('logs_regex/errors.log', "a") as error_file, open('logs_regex/success.log', "a") as success_file:

for line in lines:
    if re.search(error_pattern, line):
        with open('logs_regex/errors.log', "a") as error_file:
            error_file.write(line)

    elif re.search(status_pattern, line):
        if re.search(status_pattern, line):
            with open('logs_regex/success.log', "a") as success_file:
                success_file.write(line)








