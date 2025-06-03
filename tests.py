import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name,expected_result", [
        ('Книга', True),
        ('Книга с очень длинным названием, превышающим сорок символов', False),
        ('', False),
    ])
    def test_add_new_book_check_name_length_and_uniqueness(self, book_name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected_result

    def test_get_book_genre_returns_empty_string_for_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Без жанра')
        assert collector.get_book_genre('Без жанра') == ''

    def test_set_book_genre_sets_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    def test_get_books_genre_returns_full_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Сказка')
        assert collector.get_books_genre() == {'Сказка': ''}

    def test_get_books_for_children_excludes_age_restricted_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Мультфильм')
        collector.add_new_book('Хоррор')
        collector.set_book_genre('Мультфильм', 'Мультфильмы')
        collector.set_book_genre('Хоррор', 'Ужасы')
        result = collector.get_books_for_children()
        assert 'Мультфильм' in result
        assert 'Хоррор' not in result

    def test_add_book_in_favorites_adds_only_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Избранная')
        collector.add_book_in_favorites('Избранная')
        assert collector.get_list_of_favorites_books() == ['Избранная']

    def test_add_book_in_favorites_does_not_add_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Одна')
        collector.add_book_in_favorites('Одна')
        collector.add_book_in_favorites('Одна')
        assert collector.get_list_of_favorites_books().count('Одна') == 1

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Удалить')
        collector.add_book_in_favorites('Удалить')
        collector.delete_book_from_favorites('Удалить')
        assert 'Удалить' not in collector.get_list_of_favorites_books()
