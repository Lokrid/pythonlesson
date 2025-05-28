import codecs
import re


def delete_html_tags(html_file, result_file="cleaned.txt"):
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    cleaned = re.sub(r"<[^>]+>", "", html)

    lines = cleaned.splitlines()

    non_empty_lines = [line.strip() for line in lines if line.strip()]

    with codecs.open(result_file, "w", "utf-8") as output:
        output.write("\n".join(non_empty_lines))


delete_html_tags("draft.html")
