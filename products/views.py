from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm

def all_products(request):
    """" A view to show an items product details and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Oops! It looks like you didn't enter anything")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)    
            products = products.filter(queries)

    context = {
        'products': products,
        'search_input': query,
        'selected_categories': categories,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """" A view to show all products"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """" Add products to site"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)