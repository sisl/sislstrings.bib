import sys


class NotSorted(Exception):
    """Exception to raise if successive bib strings are not sorted."""

    def __init__(self, string1: str, string2: str):
        print(
            "Oh no! 💥 💔 💥\nString "
            + string2
            + " comes after "
            + string1
            + ".\n"
            "Please sort the strings!"
        )


def check(string1: str, string2: str):
    """Check if string2 comes after string1 alphabetically."""
    for i in range(min(len(string1), len(string2))):
        if string1[i] < string2[i]:
            break

        elif string1[i] > string2[i]:
            raise NotSorted(string1, string2)


if __name__ == "__main__":

    # read file
    with open("sislstrings.bib") as f:
        lines = f.readlines()

    # extract bibliography strings
    bibstrings = []
    for l in lines:
        bibstrings.append(l.split()[2])

    for i in range(len(bibstrings) - 1):
        check(bibstrings[i], bibstrings[i + 1])
    print("All strings are sorted! ✨ 🍰 ✨")