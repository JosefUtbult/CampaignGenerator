import json
import pathlib
import markdown
from game_systems.GameSystem import GameSystem


class CoCSverige(GameSystem):
    abbr = "cocs"
    name = "Call of Cthulhu Sverige"

    # Example to trigger the character builder
    # !!! Character
    # {
    #     "STY": "40",
    #     "FYS": "55",
    #     "STO": "55",
    #     "SMI": "70",
    #     "KAR": "60",
    #     "INT": "45",
    #     "VST": "50",
    #     "UTB": "50",
    #     "KP" : "11",
    #     "Skadebonus"   : "0",
    #     "Kroppsbyggnad": "0",
    #     "Förflyttning" : "8",
    #     "Färdigheter": {
    #         "Språk (Svenska)": "75",
    #         "Språk (Franska)": "40",
    #         "Bibliotekskunskap": "25",
    #         "Konst och hantverk (Författare)": "40",
    #         "Övertyga": "60"
    #     },
    #     "Biografi": "_Anna Olofsson_ är en litteraturstudent..."
    # }
    # !!!

    def stylize(raw):
        return CoCSverige.load_template(__file__, "base.html").render(content=raw)

    def character_builder(content):
        res = json.loads(content.replace('\n', ' '))
        if "Biografi" in res:
            res["Biografi"] = CoCSverige.parse_whitespaces(markdown.markdown(res["Biografi"]))
        return CoCSverige.load_template(__file__, "character.html").render(**res)

    # Example:
    #   !!! Titlepage
    #   {
    #       "Title": "Titlename",
    #       "image": ""
    #   }
    #   !!!

    def titlepage(content):
        res = json.loads(content.replace('\n', ' '))
        return CoCSverige.load_template(__file__, "titlepage.html").render(**res)

    def describe(content):
        return CoCSverige.load_template(__file__, "describe.html").render(content=CoCSverige.parse_whitespaces(content))

    def letter(content):
        content = CoCSverige.parse_json(content)
        content['content'] = CoCSverige.parse_whitespaces(content['content'])
        return CoCSverige.load_template(__file__, "letter.html").render(**content)

    def book(content):
        content = CoCSverige.parse_json(content)
        content['content'] = CoCSverige.parse_whitespaces(content['content'])

        return CoCSverige.load_template(__file__, "book.html").render(**content)

    function_map = {'character': character_builder, 'titlepage': titlepage, 'describe': describe,
                    'letter': letter, 'book': book}
