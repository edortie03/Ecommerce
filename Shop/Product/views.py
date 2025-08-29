
# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
	query = request.GET.get('q')
	if query:
		products = Product.objects.filter(name__icontains=query)
	else:
		products = Product.objects.all()
	return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	return render(request, 'product_detail.html', {'product': product})

def product_search(request):
	query = request.GET.get('q')
	products = Product.objects.filter(name__icontains=query) if query else []
	return render(request, 'product_search.html', {'products': products, 'query': query})
