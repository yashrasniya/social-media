from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Post, PostComments
from django.core import serializers
from .forms import post_upload
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import (PostSerializers,
                          PostActionSerializers,
                          PostCreateSerializers,
                          PostCommentSerializers,
                          PostCommentCreateSerializers,
                          PostCommentActionSerializers)
from rest_framework import viewsets


def home(requst):
    print(requst.user)
    return render(requst, 'home/index.html', context={'user': requst.user}, status=200)


def error_404(request,exception):

    return render(request, '404.html', status=200,context={'exception',exception})


@api_view(['GET'])
def post_data(request, post_id):
    obj = Post.objects.get(id=post_id)
    print(request.user,PostSerializers(obj,context={'request': request}).data)
    return JsonResponse( PostSerializers(obj,context={'request': request}).data, status=200)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment_likes(request):
    print(request.user)
    post_comment_serializers = PostCommentActionSerializers(data=request.data)

    if post_comment_serializers.is_valid(raise_exception=True):
        data = post_comment_serializers.validated_data
        id = data.get("id")
        action = data.get("action")

        obj = PostComments.objects.filter(id=id)
        if not obj.exists():
            return Response({"message": "this Post is deleted"}, status=404)
        obj = obj.first()

        if action == "like":

            likes = PostCommentSerializers(obj).data['likes']
            obj.likes.add(request.user)
            if likes != PostCommentSerializers(obj).data['likes']:
                DoLikes = True
            else:
                DoLikes = False
            data = PostCommentSerializers(obj,context={'request': request}).data
            data.update({'DoLikes': DoLikes})
            return Response(data, status=200)
        elif action == "unlike":
            unlikes = PostCommentSerializers(obj).data['likes']
            obj.likes.remove(request.user)
            if unlikes != PostCommentSerializers(obj).data['likes']:
                DoLikes = True
            else:
                DoLikes = False
            data = PostCommentSerializers(obj,context={'request': request}).data
            data.update({'DoLikes': DoLikes})
            return Response(data, status=200)

    else:
        print('post is not valid')
        return Response({"message": f"Post {id} is Deleted"}, status=200)


@api_view(['GET'])
def one_post_view(request, post_id):
    print(request.user)
    obj = Post.objects.get(id=post_id)
    return render(request, 'react/post/index.html', context={'data': (PostSerializers(obj).data)}, status=200)


@api_view(['GET'])
def post_detial_view(requst):
    post_data = Post.objects.all()
    post_list = PostSerializers(post_data, many=True, context={
        'request': requst
    })

    return JsonResponse({"data":post_list.data}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment_saver(request):
    obj = PostCommentCreateSerializers(data=request.data or None, context={'user': request.user})
    if obj.is_valid():
        obj.save(user=request.user)
        return Response(obj.data, status=200)
    return JsonResponse({}, status=403)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PostCreateView(request):
    obj = PostCreateSerializers(data=request.data or None)
    print(obj, "true\n\n", obj.is_valid())
    if obj.is_valid():
        obj.save(user=request.user)
        print(obj.data)
        return Response(obj.data, status=201)
    return JsonResponse({}, status=403)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def post_delete_view(request, post_id):
    jj = Post.objects.filter(id=post_id)
    if not jj.exists():
        return Response({"message": "this Post is deleted"}, status=404)
    qs = jj.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You are not Login"})
    obj = qs.first()
    obj.delete()
    return Response({"message": f"Post {post_id} is Deleted"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_action(request):
    post_serializers = PostActionSerializers(data=request.data)

    if post_serializers.is_valid(raise_exception=True):
        data = post_serializers.validated_data
        id = data.get("id")
        action = data.get("action")
        post_description = data.get("post_description")
        obj = Post.objects.filter(id=id)
        if not obj.exists():
            return Response({"message": "this Post is deleted"}, status=404)
        obj = obj.first()

        if action == "like":

            likes = PostSerializers(obj).data['likes']
            obj.likes.add(request.user)
            if likes != PostSerializers(obj).data['likes']:
                DoLikes = True
            else:
                DoLikes = False
            data = PostSerializers(obj,context={'request': request}).data
            data.update({'DoLikes': DoLikes})
            return Response(data, status=200)
        elif action == "unlike":
            unlikes = PostSerializers(obj).data['likes']
            obj.likes.remove(request.user)
            if unlikes != PostSerializers(obj).data['likes']:
                DoLikes = True
            else:
                DoLikes = False
            data = PostSerializers(obj,context={'request': request}).data
            data.update({'DoLikes': DoLikes})
            return Response(data, status=200)
        elif action == "comment":
            # ke la na
            comment = obj
            newPoat = Post.objects.create(user=request.user, comment=comment, post_description=post_description)
            Response(PostSerializers(newPoat).data, status=201)
    else:
        print('post is not valid')
        return Response({"message": f"Post {id} is Deleted"}, status=200)


def get_post_detial_pure_django(request):
    # if this is a POST request we need to process the form data
    user = request.user
    print(request.FILES)
    if not request.user.is_authenticated:
        if request.is_ajax():
            user = None
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = post_upload(request.POST, request.FILES)
        next_url = request.POST.get("next") or None
        print(request.POST)
        # check whether it's valid:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = user
            obj.save()
            if request.is_ajax():
                obj.serialize(request)["image"] = settings.MEDIA_URL + obj.serialize(request)["image"]
                return JsonResponse(obj.serialize(request), status=201)  # 201 is created Items
            elif next_url != None:
                return redirect(next_url)
        if form.errors:
            if request.is_ajax():
                return JsonResponse(form.errors, status=400)

    else:
        form = post_upload()

    return render(request, 'home/post_upload.html', {'form': form})
