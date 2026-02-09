from rest_framework.pagination import PageNumberPagination

class QuestionPagination(PageNumberPagination):
    page_size = 10         # sayfa başına öğe sayısı
    page_size_query_param = 'page_size'  # kullanıcı URL'den değiştirebilir
    max_page_size = 50     # maksimum sayfa boyutu
