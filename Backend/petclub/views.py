from django.shortcuts import render

# Create your views here.
# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import ListAPIView

from rest_framework import status

from .models import Pet

from .serializers import PetSerializer




class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
    def patch(self, request): #Sobrescribe el comportamiento del anterior para
        return Response(data="Me encuentro en patch", status = 200)
    def delete(self,request):
        return Response(data = "Me encuentro en delete", status = 200)
    def post(self, request):
        return Response(data = "Me encuentro en post", status = 200)
class PetView(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
    def patch(self, request): #Sobrescribe el comportamiento del anterior para
        return Response(data="Me encuentro en patch", status = 200)
    def delete(self,request):
        return Response(data = "Me encuentro en delete", status = 200)
    def post(self, request):
        return Response(data = "Me encuentro en post", status = 200)

class PersonView(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
    def patch(self, request): #Sobrescribe el comportamiento del anterior para
        return Response(data="Me encuentro en patch", status = 200)
    def delete(self,request):
        return Response(data = "Me encuentro en delete", status = 200)
    def post(self, request):
        return Response(data = "Me encuentro en update", status = 200)

#class PetListAPIView(ListAPIView):
 #   def get(self, request):
  #      pets = Pet.object.all()
   #     pets_serializer = CustomPetSerializer(pets, many=True)
    #    return Response(data = pets_serializer.data(), status = 200)

#class petAPIView(RetrieveAPIView): #se debe poner en la URL
 #   def get(self, request):
  #      return Response(data = "Mi mascota",status = 200)

class PersonApiView(APIView):
    def post(self,request):
        serializer = PersonCustomSerializer(data = request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            person.object.Create(**validated_data)
            status_code = status.HTTP_200_OK
            data = PersonCustomSerializer(new_person).data
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            data = {'error': serializer.errors}

        import pdb;pbd.set_trace()
        return response(data="asd", status = 200)
#LO APRENDIDO CON UDEMY DE ACÁ EN ADELANTE

class ListaPets(ListAPIView):
    serializer_class = PetSerializer
    def get_queryset(self):
        
        return Pet.objects.all()