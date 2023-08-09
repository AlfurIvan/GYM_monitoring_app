from rest_framework import views, response, exceptions, permissions


from . import serializer as user_serializer
from . import services
from . import authentication


class RegisterApi(views.APIView):
    """
    API to register new user with unique email

    POST: {first_name, last_name, email, password}
    :returns data same as input
    """
    # good to redirect to LoginAPI after
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data)


class LoginApi(views.APIView):
    """
    API to login exciting user

    POST: {email, password}
    :returns empty response with jwt-token, which contains user ID
            and expires after 24 hours(look for services.create_token)

    """
    def post(self, request):

        exception = exceptions.AuthenticationFailed("Invalid credentials.")

        try:
            email = request.data["email"]
            password = request.data["password"]
        except:
            raise exception

        user = services.user_email_selector(email=email)

        if user is None:
            raise exception
        if not user.check_password(raw_password=password):
            raise exception

        token = services.create_token(user_id=user.id)
        resp = response.Response()
        resp.set_cookie(key="jwt", value=token, httponly=True)
        return resp


class UserApi(views.APIView):
    """
    This endpoint can only be used if user is authenticated

    GET::returns User object data
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    """
    API to logout user

    POST: nothing in payload

    kills the exciting token
    :returns dumb message
    """
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, requset):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "go f_ck yourself, junk!"}

        return resp