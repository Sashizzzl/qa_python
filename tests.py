from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # тест на проверку добавления новой книги с названием длиной максимум 40 символов
    import pytest
    @pytest.mark.parametrize('valid_name', ['1','2_','39_символов_123456789123456789123456789', '40_символов_1234567891234567891234567891'])
    def test_add_new_book_add_book_with_valid_length_name_new_book_added(self,collector, valid_name):
        collector.add_new_book(valid_name)
        assert valid_name in collector.get_books_genre()

     # тест на проверку невозможности добавления книги с названием, больше 40 символов
    @pytest.mark.parametrize('long_name', ['41_символ_1234567890123456789012345678912','42_символа_1234567890123456789012345678912'])
    def test_add_new_book_add_book_with_invalid_length_name_book_not_added(self, collector, long_name):
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

       #тест на проверку вывода жанра добавленной книги по её имени
    def test_get_book_genre_get_genre_of_added_book_book_genre_returned(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

        # тест на проверку вывода списка книг с определённым жанром
    def test_get_books_with_specific_genre_get_books_with_genre(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_with_specific_genre(genre) == [book]

# тест на вывод текущего словаря books_genre
    def test_get_books_genre_get_books_genre_returned_books_list(self, collector,  book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_genre() == {book: genre}
# тест на отсуствие книг с возрастным рейтингом  в списке книг для детей
    def test_get_books_for_children_get_books_without_genre_age_rating(self, collector,  book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_books_for_children() == []

# тест на невозможность повторного добавления книги в избранное
    def test_add_book_in_favorites_add_book_in_favorites_two_times_impossible(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 1

        # тест на удаление из избранного книги, ранее добавленной в избранное
    def test_delete_book_from_favorites_delete_book_from_favorites_book_deleted_from_favorites(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert book not in collector.get_list_of_favorites_books()

# тест на получение списка избранных книг
    def test_get_list_of_favorites_books_get_list_of_favorites_books_returned_list_of_favorite_books(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]









