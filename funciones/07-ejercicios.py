def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reverse(text):
    upside_down_text = ""
    for char in text:
        upside_down_text = char + upside_down_text
    return upside_down_text


def is_palindrome(text):
    text = no_space(text)
    upside_down_text = reverse(text)
    return text.lower() == upside_down_text.lower()


print(is_palindrome("amo la paloma"))
print(is_palindrome("Abraham"))
