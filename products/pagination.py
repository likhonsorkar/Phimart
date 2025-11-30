from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination

class Default_Pagination(PageNumberPagination):
    page_size = 10
