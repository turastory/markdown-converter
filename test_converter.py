from converter import replace

def test_replace_riiid_simple():
    text = "Hello\n\n\nWorld"
    assert replace("riiid", text) == "Hello\n\n<br>\nWorld"

def test_replace_riiid_complicate():
    text = "This is Sample Text.\n\n\n\nThis is a [link](https://github.com/). \n - Android Studio\n - Intellij\n - VSCode\n\n\nMake your life cool with Vim."
    assert replace("riiid", text) == "This is Sample Text.\n\n<br>\n\nThis is a [link](https://github.com/). \n - Android Studio\n - Intellij\n - VSCode\n\n<br>\nMake your life cool with Vim."

def test_replace_velog_simple():
    text = "Hello\n\n\nWorld"
    assert replace("velog", text) == "Hello\n\n\nWorld"

def test_replace_velog_complicate():
    text = "This is Sample Text.\n\n\n\nThis is a [link](https://github.com/). \n - Android Studio\n - Intellij\n - VSCode\n\n\nMake your life cool with Vim."
    assert replace("velog", text) == "This is Sample Text.\n\n\n\nThis is a [link](https://github.com/). \n - Android Studio\n - Intellij\n - VSCode\n\n\nMake your life cool with Vim."
