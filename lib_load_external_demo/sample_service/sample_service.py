from typing import Union

import requests

from lib_load_external_demo.tag.animal_tag import AnimalTag

TagDefinition = Union[AnimalTag,]


class SampleService:

    def __init__(self):
        self.url = "https://api.chucknorris.io/jokes/random?category={0}"

    def do_some_stuff(self, tag_definition: TagDefinition):
        response = requests.get(self.url.format(tag_definition.get_tag_id()))
        return response.text
