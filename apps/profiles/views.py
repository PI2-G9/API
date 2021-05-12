from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from apps.profiles.serializers import ProfileSerializer

# from apps.accounts.forms import PhotoForm
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

class ProfileList(ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    # @property
    # def get_queryset(self):
    #     page = self.request.query_params.get('page')
    #     if page is not None:
    #         page = int(page)
    #     first = 50 * (page - 1) if page else 0
    #     last = 50 * page - 1 if page else 49
    #     queryset = Profile.objects.order_by('created_at')[first:last][::-1]
    #     cpf = self.request.query_params.get('cpf')
    #     if cpf is not None:
    #         queryset = Profile.objects.get(cpf=cpf)
    #     return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


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

# def add_photo_user(request):
#     if request.method == 'POST':
#         form = PhotoForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = PhotoForm()
#     return render(request, 'photo_user_form.html', {'form': form})
#
#
# def success(request):
#     return HttpResponse('successfully uploaded')

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
