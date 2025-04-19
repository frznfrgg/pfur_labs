import re
with open("data/text.txt") as f:
    l = f.read()
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", l)
    phones = re.findall(r"\+\d-\d{3}-\d{3}-\d{2}-\d{2}", l)
    capitals = re.findall(r" [A-Z][a-z]+", l)
with open("results/emails.txt", "w") as f:
    for elem in emails:
        f.write(elem)
with open("results/phones.txt", "w") as f:
    for elem in phones:
        f.write(elem)
with open("results/capital_words.txt", "w") as f:
    for elem in capitals:
        f.write(elem)