import re

email = "john@google.com elise@python.com"
pattern = "(\w+)@\w+.com"
ans = re.match(pattern, email)
print(ans.group(1))


email = "john@google.com elise@python.com"
pattern = "\w+@(\w+).com"
ans = re.findall(pattern, email)
print(ans)
