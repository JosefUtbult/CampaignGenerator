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
        res = json.loads(content)
        if "Biografi" in res:
            res["Biografi"] = markdown.markdown(res["Biografi"])
        return CoCSverige.load_template(__file__, "character.html").render(**res)

    def titlepage(content):
        res = json.loads(content)
        return CoCSverige.load_template(__file__, "titlepage.html").render(**res)

    function_map = {'character': character_builder, 'titlepage': titlepage}
