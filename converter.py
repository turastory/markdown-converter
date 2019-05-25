def replace(platform, input_text):
    if platform == "riiid":
        return input_text.replace("\n\n\n", "\n\n<br>\n")
    else:
        return input_text
