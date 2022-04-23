import os


def list_matched_files(files, pattern, prompt_message):
    """とりあえず一覧します"""

    print(prompt_message, end='')

    count_of_matched = 0

    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            # グループ数
            groupCount = len(result.groups())
            buf = f"({i+1}) {basename}"
            for j in range(0, groupCount):
                buf += f" \\{j+1}=[{result.group(j+1)}]"
            print(buf)
            count_of_matched += 1
        else:
            # Unmatched
            print(f"( ) {basename}")

    print(f"\ncount_of_matched = {count_of_matched}")
