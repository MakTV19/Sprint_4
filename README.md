# **Основные сценарии:**
1. add_new_book (test_add_new_book_add_two_books) Добавление книг с допустимой длиной названия
2. check_name_length_and_uniqueness (test_add_new_book_check_name_length_and_uniqueness) Проверка ограничений: длина названия, уникальность
3. set_book_genre(test_set_book_genre_sets_correct_genre) Присвоение допустимого жанра книге
4. get_book_genre(test_get_book_genre_returns_empty_string_for_new_book) Проверка жанра у новой книги (ожидается пустая строка)
5. get_books_with_specific_genre(test_get_books_with_specific_genre_returns_correct_books) Получение списка книг по конкретному жанру
6. get_books_genre(test_get_books_genre_returns_full_dictionary) Получение полного словаря книг
7. get_books_for_children (test_get_books_for_children_excludes_age_restricted_genres)	Проверка фильтрации книг с возрастными жанрами
8. add_book_in_favorites	(test_add_book_in_favorites_adds_only_existing_book)	Добавление книги в избранное, если она есть в словаре
9. (test_add_book_in_favorites_does_not_add_twice)	Проверка, что книга не добавляется в избранное дважды
10. delete_book_from_favorites	(test_delete_book_from_favorites_removes_book)	Удаление книги из списка избранного
