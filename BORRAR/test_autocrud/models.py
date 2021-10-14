from django.db import models

from core.autocrud.models import BaseModel


class Category(BaseModel):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField('Nombre de Categoría', max_length=150)    

    exclude_fields = ['date_created','date_modified','date_deleted']
    exclude_model = False
    server_side = True
    login_required = False
    model_permissions = False
    default_permissions = True
    all_cruds_types = True
    normal_cruds = False
    ajax_crud = False

    list_template = None

    def get_create_form(self, form=None):
        # IMPORTANTE: la carga del form se debe hacer dentro de la función
        from .forms import CategoryForm 
        self.create_form = CategoryForm
        return self.create_form        

    def get_update_form(self, form=None):
        # IMPORTANTE: la carga del form se debe hacer dentro de la función
        from .forms import CategoryForm
        self.update_form = CategoryForm
        return self.update_form

    class Meta:
        """Meta definition for Category."""
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    def natural_key(self):
        return self.name


class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre de Producto', max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
