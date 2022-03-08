import jinja2
import pathlib
import json


class GameSystem:
    abbr = ""
    name = ""
    function_map = []

    def stylize(raw):
        return raw

    def load_template(child_class, filename):
        template_loader = jinja2.FileSystemLoader(searchpath=pathlib.Path(child_class).parent.absolute() / "templates")
        template_env = jinja2.Environment(loader=template_loader)
        return template_env.get_template(filename)

    def parse_json(content):
        try:
            return json.loads(content.replace('\n', ' '))
        except ValueError:
            return {'content': content}

    def parse_whitespaces(content):
        return content.replace('//', '</p><p>')
