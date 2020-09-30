from django.shortcuts import render,redirect
from cmanagement.models import category,items,vendor,locationn,inventory
from cmanagement.forms import catform,itemform,vendorform,locationform,inventoryform
from django.http import HttpResponse
# Create your views here.
def seyd(request):
	if request.method=='POST':
		form=catform(request.POST)
		if form.is_valid():  
			form.save()
			return redirect('/cmanagement/show/')
		else:
			return HttpResponse('form not valid')
	else:
			form = catform()
			return render(request,'index.html',{'cat':form})  
def hello(request):
	form = category.objects.all()
	return render(request,"show.html",{'cat':form})
def destroy(request, id):
	employee = category.objects.get(id=id)
	employee.delete()
	return redirect("/cmanagement/show/")

def demo(request):
	return render(request,'item.html')	
def ali(request):
		formm=itemform(request.POST)
		form1 = category.objects.all()
		val = request.POST.get("ca")
		h=request.POST.get('cate')
		if request.method=='POST':
			formm=items(categoryy=val,item=h)
			formm.save()
			return redirect("/cmanagement/alishow/")
		else:
			formm=itemform()

		return render(request,'item.html',{'alii':form1	,'key':formm})
		
		
		
def alishow(request):
	forms=items.objects.all()
	return render(request,'showw.html',{'c':forms})
def alidelete(request, id):
	kee = items.objects.get(id=id)
	kee.delete()
	return redirect("/cmanagement/alishow/")


def vendr(request):
	if request.method=='POST':
		form=vendorform(request.POST)
		if form.is_valid():  
			form.save()
			return redirect('/cmanagement/vendorshow/')
		else:
			return HttpResponse('form not valid')
	else:
		form = vendorform()
		return render(request,'vendorindex.html',{'v':form})

def vendrshow(request):
	form = vendor.objects.all()
	return render(request,"vendorshow.html",{'v':form})

def vendrdelete(request, id):
	x= vendor.objects.get(id=id)
	x.delete()
	return redirect("/cmanagement/vendorshow/")	

def loc(request):
	if request.method=='POST':
		form=locationform(request.POST)
		if form.is_valid():  
			form.save()
			return redirect('/cmanagement/locationshow/')
		else:
			return HttpResponse('form not valid')
	else:
		form = locationform()
		return render(request,'location index.html',{'v':form})	

def locshow(request):
	form = locationn.objects.all()
	return render(request,"locationshow.html",{'v':form})

def locdelete(request, id):
	x= locationn.objects.get(id=id)
	x.delete()
	return redirect("/cmanagement/locationshow/")

def home(request):
	return render(request,"home.html")	

def hom(request):
	return render(request,"g.html")


def inv(request):
		form=inventoryform(request.POST)
		c=category.objects.all()
		cat=request.POST.get('cat')
		l=locationn.objects.all()
		loca=request.POST.get('l')
		i=items.objects.all()	
		it=request.POST.get('it')
		m=request.POST.get('man')
		snumber=request.POST.get('snum')
		purchase=request.POST.get('purchase')
		v=vendor.objects.all()
		ven=request.POST.get('ve')
		w=request.POST.get('war')
		q=request.POST.get('quantity')
		cost=request.POST.get('cost')
		total=request.POST.get('total')
		if request.method=='POST':
			print('success')
			formm=inventory(category=cat,locations=loca,item=it,manufacture=m,serial_number=snumber,
				purchase_date=purchase,vendor=ven,warranty=w,quantity=q,cost=cost,total=total)	
			print('222222')
			formm.save()
			return redirect('/cmanagement/inventshow/')
		# else:
		# 	form=inventoryform()
		# 	return HttpResponse('kalanjitt podeyy....')


		return render(request,'inventory.html',{'IN':c, 's':v, 'lo':l, 'item':i})

		# formm=itemform(request.POST)
		# form1 = category.objects.all()
		# val = request.POST.get("ca")
		# h=request.POST.get('cate')
		# if request.method=='POST':
		# 	formm=items(categoryy=val,item=h)
		# 	formm.save()
		# 	return redirect("/cmanagement/alishow/")
		# else:
		# 	formm=itemform()

		# return render(request,'item.html',{'alii':form1	,'key':formm})
		
def invshow(request):
	form=inventory.objects.all()
	return render(request,'inventoryshow.html',{'inv':form})

def invdelete(request, id):
	form=inventory.objects.get(id=id)
	form.delete()
	return redirect('/cmanagement/inventshow/')
