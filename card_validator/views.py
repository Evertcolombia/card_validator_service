from card_validator.models import CardNumber
from card_validator.serializers import CardNumberSerializer
from .src.validator import getSupplier, checkLuhn

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from django.http import Http404
import re


class CardNumberList(APIView, LimitOffsetPagination):
    """
    Validate a card number, or obtain a list of validated card numbers.
    """
    # pagination_class = DefaultPagination

    def get(self, request):
        """
        Get a list with validated card numbers
        """
        cards = CardNumber.objects.all()
        results =  self.paginate_queryset(cards, request, view=self)
        serializer = CardNumberSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request):
        """
        Validate a card number

        Parameters example:
        ----------
        {
            "card_num": "string"
        }
        """
        obj = dict()
        serializer = CardNumberSerializer(data=request.data)
        if serializer.is_valid():
            num = serializer.data['card_num'].replace(" ", "")
            
            try:
                int(num)
            except ValueError:
                return error("{} - Must be a number".format(num))

            if len(num) < 7: #  7 is the minum numbers allowed in a Issuer identification number (IIN)
                return error("{} - Must have at leat 7 numbers".format(num))
            
            if checkLuhn(num) == True:
                obj = serializer.data
                obj.update({"supplier": getSupplier(num)})
                serializer = CardNumberSerializer(data=obj)

                if serializer.is_valid():
                    serializer.save()
                return Response(
                    obj,
                    status=status.HTTP_201_CREATED
                )
        return error("{} - Invalid Number".format(num))


class CardNumberDetail(APIView):
    """
    Retrieve, update or delete a card instance.
    """
    def get_object(self, num):
        """ get card object based on number """
        try:
            print(num)
            return CardNumberList.objects.filter(card_num.__startswith(num)).get()
        except:
            print("uju")
            raise Http404

    def get(self, request, num, format=None):
        """ get card object """
        card = self.get_object(num)
        serializer = CardNumberSerializer(card)
        return Response(serializer.data)

    def put(self, request, num, format=None):
        """ update card object """
        card = self.get_object(num)
        serializer = CardNumberSerializer(card, data=request.data)
        if serializer.is_valnum():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, num, format=None):
        """ delete card object """
        card = self.get_object(num)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def error(err):
    """ error mmanage for diffrent messages """
    return Response(
            {"Error": err},
        status=status.HTTP_400_BAD_REQUEST
    )