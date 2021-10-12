from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Book
from .forms import BookForm


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Book.objects.all()
            data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
                'books': books
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
    else:
        form = BookForm()
    return save_book_form(request, form, 'books/includes/partial_book_create.html')


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
    else:
        form = BookForm(instance=book)
    return save_book_form(request, form, 'books/includes/partial_book_update.html')


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    data = dict()
    if request.method == 'POST':
        book.delete()
        data['form_is_valid'] = True
        books = Book.objects.all()
        data['html_book_list'] = render_to_string('books/includes/partial_book_list.html', {
            'books': books
        })
    else:
        context = {'book': book}
        data['html_form'] = render_to_string('books/includes/partial_book_delete.html', context, request=request)
    return JsonResponse(data)






from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView

from core.audit.models import AuditableMixin
from core.comunes.utils import PagedFilteredTableView, where_are_we_going

from .models import Book
from .tables import BookTable
# from .filters import BookFilter, BookFilterForm
from .forms import BookForm


PERMISSION_REQUIRED = '{domain}.view_{app}'.format(domain='books', app='book')


class BookTemplateView(generic.TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return BookListView.as_view()(request)


class BookListView(PermissionRequiredMixin, SingleTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = PERMISSION_REQUIRED
    model = Book
    table_class = BookTable              # SingleTableView
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class BookCreateView(PermissionRequiredMixin, generic.CreateView, AuditableMixin):
    """CreateView formulario para la creación de un registro en la tabla"""
    permission_required = PERMISSION_REQUIRED
    model = Book
    form_class = BookForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class BookReadView(PermissionRequiredMixin, generic.DetailView):
    pass


class BookUpdateView(generic.UpdateView):
    pass


class BookDeleteView(generic.DeleteView):
    pass