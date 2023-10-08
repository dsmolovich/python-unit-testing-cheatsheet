from unittest.mock import Mock, MagicMock


def test_book_attr():
    book = Mock(author=Mock(last_name="Pushkin"))
    assert book.author.last_name == "Pushkin"

    alternative_book = Mock()
    alternative_book.author.last_name = "Lermontov"
    assert alternative_book.author.last_name == "Lermontov"


def test_book_method():
    book = Mock()
    book.get_title.return_value = "Eugene Onegin"
    assert book.get_title() == "Eugene Onegin"

    alternative_book = Mock(get_title=Mock(return_value="Mtsyri"))
    assert alternative_book.get_title() == "Mtsyri"


def test_implicitly_created_sub_mocks():
    airport = Mock()
    airport.get_tower().team_on_duty.get_dispatcher().first_name = "Joe Patroni"
    assert airport.get_tower().team_on_duty.get_dispatcher().first_name == "Joe Patroni"

    book = Mock()
    book.get_review().reviewer.get_country().short_name = "Nick"
    assert book.get_review(sort="year", order="desc").reviewer.get_country().short_name == "Nick"


def test_mocking_lists():
    book = MagicMock()
    book.data["reviews"][0].reviewer.date = "Jan 12, 2023"
    assert book.data["reviews"][0].reviewer.date == "Jan 12, 2023"

    book.data["reviews"].__len__.return_value = 120
    assert len(book.data["reviews"]) == 120


def test_return_list():
    book = Mock()
    book.get_review.return_value.reviewer = {"name": "Natalia"}
    assert book.get_review(type="oldest").reviewer.get("name", "unknown") == "Natalia"

    alternative_book = MagicMock()
    alternative_book.all_reviews[-1].get_country(locale="en").reviewer = {"name": "Elena"}
    assert alternative_book.all_reviews[-1].get_country(locale="en").reviewer.get("name") == "Elena"


def test_way_to_know_the_path_to_mock():
    # For a.b(c, d).e.f.g().h() to know the path to mock create
    a = Mock()
    # And call the required a.b(c, d).e.f.g().h()
    #   to see the <Mock name='mock.b().e.f.g().h()' id='...'>
    # Then mock replacing "()"" with ".return_value"
    a.b.return_value.e.f.g.return_value.h.return_value = 'some value'
    assert a.b(c=True, d=False).e.f.g().h() == 'some value'



