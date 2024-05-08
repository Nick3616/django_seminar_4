from django.shortcuts import redirect, render
from .models import User, Order, Commodity
from django.utils import timezone
from datetime import timedelta
from .forms import CommodityForm, CommodityUpdateForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

def user_orders(request, name_id):
    name = User.objects.get(pk=name_id)
    orders = Order.objects.filter(name=name)
    return render(request, 'orders.html', {'name': name, 'orders': orders})

def user_orders_filtered(request, name_id):
    name = User.objects.get(pk=name_id)
    today = timezone.now()
    orders_last_week = Order.objects.filter(name=name, data__gte=today - timedelta(days=7))
    orders_last_month = Order.objects.filter(name=name, data__gte=today - timedelta(days=30))
    orders_last_year = Order.objects.filter(name=name, data__gte=today - timedelta(days=365))

    context = {
        'name': name,
        'orders_last_week': orders_last_week,
        'orders_last_month': orders_last_month,
        'orders_last_year': orders_last_year
    }
    return render(request, 'orders_filtered.html', context)

def commodity_form(request):
    if request.method == 'POST':
        form = CommodityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommodityForm()
    return render(request, 'commodity_form.html', {'form': form})

def edit_commodity(request, commodity_id):
    commodity = Commodity.objects.get(pk=commodity_id)
    if request.method == 'POST':
        form = CommodityUpdateForm(request.POST, request.FILES, instance=commodity)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommodityUpdateForm(instance=commodity)
    return render(request, 'edit_commodity.html', {'form': form})

