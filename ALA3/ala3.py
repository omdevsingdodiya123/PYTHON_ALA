str1 = "Hello World"

i = 0
count = 0

while i < len(str1):
    c = str1[i]

    # check letter chhe ke nahi
    if (('a' <= c <= 'z') or ('A' <= c <= 'Z')):

        # check vowel nathi (etle consonant)
        if (c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u' and
            c != 'A' and c != 'E' and c != 'I' and c != 'O' and c != 'U'):

            count += 1

    i += 1

print("Consonants =", count)