# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from models import RestaurantReview, Restaurant, Dish
from forms import RestaurantForm, DishForm
from django.views.generic import View
from .models import Restaurant

class RestaurantDetail(DetailView):
  model = Restaurant
  template_name = 'restaurant_detail.html'

  def get_context_data(self, **kwargs):
    context = super(RestaurantDetail, self).get_context_data(**kwargs)
    context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
    return context

class RestaurantCreate(CreateView):
  model = Restaurant
  template_name = 'form.html'
  form_class = RestaurantForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(RestaurantCreate, self).form_valid(form)

class DishCreate(CreateView):
  model = Dish
  template_name = 'form.html'
  form_class = DishForm
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
    return super(DishCreate, self).form_valid(form)

def review(request, pk):
  restaurant = get_object_or_404(Restaurant, pk=pk)
  review = RestaurantReview(
      rating=request.POST['rating'],
      comment=request.POST['comment'],
      user=request.user,
      restaurant=restaurant)
  review.save()
  return HttpResponseRedirect(reverse('restaurant_detail', args=(restaurant.id,)))
 
 
  
def Restaurants(request):
		Res = Restaurant.objects.all()
		context = {
		'Res' : Res,
		
		}
		return render(request,"restaurant_detail.html",context)
