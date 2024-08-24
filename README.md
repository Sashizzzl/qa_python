# qa_python
1. test_add_new_book_add_book_with_valid_length_name_new_book_added
Проверяет добавление новой книги с названием длиной максимум 40 символов.
2. test_add_new_book_add_book_with_invalid_length_name_book_not_added
Этот тест проверяет, что невозможно добавить книги с названием, больше 40 символов
3. test_get_book_genre_get_genre_of_added_book_book_genre_returned
Тест на проверку вывода жанра добавленной книги по её имени
4. test_get_books_with_specific_genre_get_books_with_genre
Этот тест проверяет вывод списка книг с заданным жанром
5. test_get_books_genre_get_books_genre_returned_books_list
Тест на проверку вывода текущего словаря books_genre
6. test_get_books_for_children_get_books_without_genre_age_rating
Тест на проверку отсуствия книг с возрастным рейтингом  в списке книг для детей
7. test_add_book_in_favorites_add_book_in_favorites_two_times_impossible
Тест на проверку отсуствия возможности добавления одной и той же книги в список избранного дважды
8. test_delete_book_from_favorites_delete_book_from_favorites_book_deleted_from_favorites
Тест на проверку удаление из избранного книги, ранее добавленной в избранное
9. test_get_list_of_favorites_books_get_list_of_favorites_books_returned_list_of_favorite_books
Тест проверяет вывод списка избранных книг

Эти тесты покрывают основную функциональность класса `BooksCollector`, включая добавление книг, получение жанров, взаимодействие с избранными книгами, а также проверки на соответствие ожиданиям. 
Их выполнение помогает выявить возможные ошибки в коде и улучшить его качество.