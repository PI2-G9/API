from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from .serializers import UserProfileSerializer

from apps.accounts.forms import PhotoForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


# class ProductViewSet(BaseViewSet, viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     @detail_route(methods=['post'])
#     def upload_docs(request):
#         try:
#             file = request.data['file']
#         except KeyError:
#             raise ParseError('Request has no resource file attached')
#         product = Product.objects.create(image=file, ....)

def add_photo_user(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PhotoForm()
    return render(request, 'photo_user_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

##### nao sei se devo fazer com função dentro da classe ou fora ( segundo o q eu segui era fora mas isso parece errado pra gente)


#  def hotel_image_view(request):
#  if request.method == 'POST':
#     form = PhotoForm(request.POST, request.FILES)
#
#     if form.is_valid():
#          form.save()
#          return redirect('success')
#  else:
#      form = PhotoForm()
#  return render(request, 'hotel_image_form.html', {'form': form})
#
#
# def success(request):
# return HttpResponse('successfully uploaded')
