from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_author
        )

    # def has_permission(self, request, view):
    #     """ Разрешаем создание только пользователям с ролью "автор" """
    #     if request.method == 'create':
    #         return request.user.role.lower() == 'author'
    #     return True
    #
    # def has_object_permission(self, request, view, obj):
    #     """Разрешаем редактирование и удаление только автору статьи"""
    #     if request.method in ['update', 'partial_update', 'destroy']:
    #         return obj.author == request.user
    #     return True
