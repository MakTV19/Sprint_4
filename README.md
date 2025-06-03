Основные сценарии
add_new_book (test_add_new_book_add_two_books) — добавление книг с допустимой длиной названия

add_new_book (test_add_new_book_check_name_length_and_uniqueness) — проверка ограничений: длина названия, уникальность

set_book_genre (test_set_book_genre_sets_correct_genre) — присвоение допустимого жанра книге

get_book_genre (test_get_book_genre_returns_empty_string_for_new_book) — проверка жанра у новой книги (ожидается пустая строка)

get_books_with_specific_genre (test_get_books_with_specific_genre_returns_correct_books) — получение списка книг по конкретному жанру

get_books_genre (test_get_books_genre_returns_full_dictionary) — получение полного словаря книг

get_books_for_children (test_get_books_for_children_excludes_age_restricted_genres) — проверка фильтрации книг с возрастными жанрами

add_book_in_favorites (test_add_book_in_favorites_adds_only_existing_book) — добавление книги в избранное, если она есть в словаре

add_book_in_favorites (test_add_book_in_favorites_does_not_add_twice) — проверка, что книга не добавляется в избранное дважды

delete_book_from_favorites (test_delete_book_from_favorites_removes_book) — удаление книги из списка избранного
