from rest_framework.pagination import PageNumberPagination

class LimitofPage(PageNumberPagination):
    page_size = 2 