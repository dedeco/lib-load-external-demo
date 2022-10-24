from lib_load_external_demo import __version__
from lib_load_external_demo.sample_service.sample_service import SampleService
from lib_load_external_demo.tag.animal_tag import AnimalTag, SampleEnum


def test_sample_service():

    animal = AnimalTag(
        name="teste",
        baz=SampleEnum.PUBLIC
    )

    service = SampleService()
    result = service.do_some_stuff(
        animal
    )

    assert "Chuck Norris" in result

