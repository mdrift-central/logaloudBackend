
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from mobilebackend.models import *
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django import db
from django.conf import settings
from django.db import transaction
import uuid, os
import json, traceback, sys

@csrf_exempt
def hi(request):
	print(request.POST , "Hi there")
	data = request.POST
	data_test = data.get('res_id')
	return HttpResponse(content=json.dumps({'result':'false', 'data':data_test, 'message':'Username is already in use.Please use a different one.'}), status=200, content_type="application/json")
    

@csrf_exempt
def mobile_login(request):
	print request.POST
	username = request.POST.get('username')
	password = request.POST.get('password')

	try:
		user = User.objects.get(username = username)
		if not user.is_active:
			return HttpResponse(content=json.dumps({'result':'false', 'data':{}, 'message':'You are not authorised to use the app'}), status=200, content_type="application/json")
		if user.check_password(password):
			return HttpResponse(content=json.dumps({'result':'true','data':{'user_id':user.id,'user_name':user.username},'message':'Success'}), content_type="application/json", status=200)
		else:
			return HttpResponse(content=json.dumps({'result':'false', 'data':{}, 'message':'You are not authorised to use'}),status=200, content_type="application/json")
	except User.DoesNotExist as e:
		return HttpResponse(content=json.dumps({'result':'false', 'data':{}, 'message':'User does not exist.'}), status=200, content_type="application/json")
	except Exception as e:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		err = "\n".join(traceback.format_exception(*sys.exc_info()))
		print err
		return HttpResponse(content=json.dumps({'result':'false', 'data':{}, 'message':'Server error.'}), status=200, content_type="application/json")

@csrf_exempt
def mobile_signup(request):
	print request.POST
	err = ""
	username = request.POST.get('username')
	if User.objects.filter(username=username).exists():
		return HttpResponse(content=json.dumps({'result':'false', 'data':{}, 'message':'Username is already in use.Please use a different one.'}), status=200, content_type="application/json")
	if User.objects.filter(email=username).exists():
		return HttpResponse(content=json.dumps({'result':'false', 'data':{}, 'message':'Email is already in use.Please use a different one.'}), status=200, content_type="application/json")
	try:
		with transaction.atomic():
			data = request.POST
			obj_user = User(
				first_name = data.get('firstname'),
                last_name = data.get('lastname'),
                username = username,
                email = data.get('email'),
			)
			password = data.get('password')
			obj_user.set_password(password)
			obj_user.full_clean()
			obj_user.save()
			return HttpResponse(content=json.dumps({'result':'true','data':{'user_id':obj_user.id,'user_name':obj_user.username},'message':'Success'}), content_type="application/json", status=200)
	except Exception as e:
		exc_type, exc_value, exc_traceback = sys.exc_info()
        err = "\n".join(traceback.format_exception(*sys.exc_info()))
        print err
        return HttpResponse(content=json.dumps({'result':'false', 'data':{},'error': err, 'message':'Server error.'}), status=200, content_type="application/json")



@csrf_exempt
def get_listings(request):
	print request.POST
	all_entries = Listing.objects.all()
	result = []
	for entry in all_entries:
		listing = {}
		listing['owner'] = str(entry.owner.username)
		listing['listing_type'] = str(entry.listing_type)
		listing['street'] = str(entry.listing_address.street)
		result.append(listing)
	print result
	return HttpResponse(content=json.dumps({'result':'false', 'data':result, 'message':'Server error.'}), status=200, content_type="application/json")


@csrf_exempt
def get_great_perks(request):
	print request.POST
	all_entries = Listing.objects.filter(listing_type='Great Perks')
	result = []
	for entry in all_entries:
			listing = {}
			listing['owner'] = str(entry.owner.username)
			listing['listing_type'] = str(entry.listing_type)
			listing['street'] = str(entry.listing_address.street)
			images = Media.objects.filter(listing=entry ,media_type='great_perks_cover')
			listing['cover_image'] = images[0].image_path
			listing['name'] = str(entry.listing_name)
			listing['short_title'] = str(entry.listing_short_title)
			listing['id'] = str(entry.pk)
			'''listing['image_url'] = str(cover_image.id)'''
			allylist_main = []
			
			print str(entry.listing_name)
			connections = BConnection.objects.filter(listing=entry)
			print "Connections ", connections
			i = 0
			for connection in connections:
				allylist_main_1 = {}
				print connection
				allylist_main_1['ally_name'] = str(connection.ally.listing_name)
				thumbnail = Media.objects.filter(listing = connection.ally, media_type='thumbnail')
				allylist_main_1['thumbnail_url'] = str(thumbnail[0].image_path)
				allylist_main.append(allylist_main_1)				
				i = i + 1

			'''global b_connections 
			b_connections = BConnection.objects.filter(listing=entry)
			i = 0
			for connection in b_connnections :
				allylist_main_1['listing_name'] = connection.listing.listing_name
				allylist_main_1['ally_name'] = connection.ally.listing_name
				thumbnail = Media.objects.filter(listing = connection.ally, media_type='thumbnail')
				allylist_main_1['thumbnail_url'] = str(thumbnail.image_path)
				i = i + 1
				allylist_main.append(allylist_main_1)
			listing['allylist'] = allylist_main'''
			listing['allies'] = allylist_main
			result.append(listing)
	return HttpResponse(content=json.dumps({'result':'true', 'result':result, 'message':'Server request succesful.'}), status=200, content_type="application/json")

@csrf_exempt
def get_allies_and_perks(request):
	print request.POST
	listing_id = request.POST.get('listing_id')
	listing_main = Listing.objects.get(pk=listing_id)
	b_connections = BConnection.objects.filter(listing=listing_main)
	result = []
	ally = {}
	perk_array = []
	
	for connection in b_connections:
		print connection.ally.listing_name
		ally['id'] = connection.ally.pk
		ally['ally_name'] = connection.ally.listing_name
		perks = Perk.objects.filter(from_listing=listing_main, ally=connection.ally)
		for perk in perks:
			print perk.perk_name
			perk_item = {}
			perk_item['name'] = perk.perk_name
			perk_item['description'] = perk.perk_description
			perk_item['coupon'] = perk.perk_coupon_code
			perk_item['ally'] = connection.ally.listing_name
			perk_array.append(perk_item)
		ally['perk_list'] = perk_array
		result.append(ally)
	return HttpResponse(content=json.dumps({'result':'true', 'data': result,'message':'Server request succesful.'}), status=200, content_type="application/json")






@csrf_exempt
def get_what_we_have(request):
	print request.POST
	all_entries = Listing.objects.all()
	result = []
	for entry in all_entries:
		listing = {}
		listing['owner'] = str(entry.owner.username)
		listing['listing_type'] = str(entry.listing_type)
		listing['street'] = str(entry.listing_address.street)
		result.append(listing)
	print result
	return HttpResponse(content=json.dumps({'result':'false', 'data':result, 'message':'Server error.'}), status=200, content_type="application/json")

@csrf_exempt
def get_featured(request):
	print request.POST
	all_entries = Listing.objects.filter(listing_type='Featured')
	result = []
	result_bool = 'false'
	print all_entries.count()
	if all_entries.count() > 0:
		result_bool = 'true'
		for entry in all_entries:
			listing = {}
			listing['owner'] = str(entry.owner.username)
			listing['listing_type'] = str(entry.listing_type)
			listing['street'] = str(entry.listing_address.street)
			listing['listing_title'] = str(entry.listing_short_title)
			thumbnail = Media.objects.filter(listing = entry, media_type='thumbnail')
			if not thumbnail:
				listing['thumbnail_url'] = 'http://i.imgur.com/pcvBkWy.jpg'
			else:
				listing['thumbnail_url'] = str(thumbnail[0].image_path)
			result.append(listing)
	print result
	return HttpResponse(content=json.dumps({'result':result_bool, 'data':result, 'message':'No Specific Message. Happy weekend!'}), status=200, content_type="application/json")


