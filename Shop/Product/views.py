from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, ContactMessage
from cart.forms import CartAddProductForm
from .forms import ContactForm

# Create your views here.
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request,'shop/product/list.html',{
		'category': category,
		'categories': categories,
		'products': products,
		'show_search': True
	})

def product_detail(request, id, slug):
	product = get_object_or_404(
		Product, id=id, slug=slug, available=True
	)
	cart_product_form = CartAddProductForm()
	return render(request,'shop/product/detail.html',{'product': product, 'cart_product_form': cart_product_form})

def product_search(request):
	query = request.GET.get('q')
	products = Product.objects.filter(name__icontains=query) if query else []
	categories = Category.objects.all()
	return render(request, 'shop/product/search.html', {'products': products, 'query': query, 'categories': categories})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'shop/product/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'shop/product/contact.html', {'form': form})

def about(request):
    return render(request, 'shop/product/about.html')
