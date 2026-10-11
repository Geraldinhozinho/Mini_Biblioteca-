from django.contrib import admin
from biblioteca.models import Livro, Author, Category

admin.site.register(Category)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autores", "ano_publicacao", "disponivel"]
    search_fields = ["titulo", "mul_autor__name"]
    list_filter = ["disponivel", "categoria"]
    filter_horizontal = ["categoria", "mul_autor"]

    @admin.display()
    def autores(self, obj):
        nomes = []
        for autor in obj.mul_autor.all():
            nomes.append(autor.name)
        return ", ".join(nomes)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ["name"]
 