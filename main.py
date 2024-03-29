import os
import re
import sys
from fs_operation import input_change_current_directory, list_current_directory_files, input_y, \
    list_current_directory_files_no_echo
from this_operation import list_matched_files

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')

# ディレクトリーを選んでください
while True:
    input_change_current_directory("""Which directory?
Example: .
"""
                                   )

    print(f"""Current directory: {os.getcwd()}""")

    # フィル名を一覧します
    files = list_current_directory_files()

    is_y = input_y("""
Are you sure this is the right directory (y/n)?
""")

    if is_y:
        break
    else:
        print("Canceld")

is_dirty_files = False

while True:

    if is_dirty_files:
        files = list_current_directory_files_no_echo()

    is_dirty_files = True

    # 正規表現のパターンを入力してください
    while True:
        print(r"""
Please enter a regular expression pattern.
Example: ^example-([\d\w]+)-([\d\w]+).txt$""")

        patternText = input()
        pattern = re.compile(patternText)

        # とりあえず一覧します
        list_matched_files(files, pattern, """
Numbering
---------
""")

        is_y = input_y("""
Was there a match (y/n)?
""")

        if is_y:
            break
        else:
            print("Canceld")

    # 置換後の正規表現
    while True:
        print(r"""
Enter the pattern after the conversion.
Example: example-\2-\1.txt""")

        replacement = input()

        # 置換のシミュレーション
        print("""
Simulation
----------""")
        for i, file in enumerate(files):
            basename = os.path.basename(file)
            result = pattern.match(basename)
            if result:
                # Matched
                converted = re.sub(patternText, replacement, basename)
                print(f"({i+1}) {basename} --> {converted}")

        is_y = input_y("""
Do you want to run it (y/n)?
""")

        if is_y:
            break
        else:
            print("Canceld")

    print("""
Result
------""")

    # 置換実行
    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            converted = re.sub(patternText, replacement, basename)
            oldPath = os.path.join(os.getcwd(), basename)
            newPath = os.path.join(os.getcwd(), converted)
            print(f"({i})Rename {oldPath} --> {newPath}")
            os.rename(oldPath, newPath)

    is_y = input_y("""
Continue (y/n)?
""")

    if is_y:
        pass
    else:
        print("Canceld")
        break
