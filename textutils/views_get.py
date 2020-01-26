from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
    user=os.environ["USER"].capitalize()
    params={'user':user}
    resp=render(request,'index.html',params)
    #resp=HttpResponse('<h3>Wecome to Django Tutorial</h3><br><a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">click here</a>')
    return resp

def analysed(request):
    params={}
    val=request.GET
    print (val)
    analyse_text=request.GET.get('analyse_text')
    rmpunc_flag=request.GET.get('rmpunc','off')
    rmnline_flag=request.GET.get('rmnline','off')
    rmexspac_flag=request.GET.get('rmexspac','off')
    rmnonalpha_flag=request.GET.get('rmnonalpha','off')
    uppercase_flag=request.GET.get('uppercase','off')
    mtext=analyse_text
    process_types=[]
    puncode='''<>'\*():,{}_"-?/[]$%#&@'''
    if rmpunc_flag=='on':
        process_types.append('Removing Punctuation')
        mtext=''
        for char in analyse_text:
            if not char in puncode:
                mtext+=char
    if uppercase_flag =='on':
        process_types.append('UPPER CASE')
        tmp_text=mtext
        mtext=tmp_text.upper()
    ptype_text=None
    if not analyse_text:
        mtext="Please enter the text"
    if process_types:
        #mprocess_list=[ptype for ptype in process_types]
        ptype_text=', '.join(process_types)
    else:
        ptype_text="Option Not Selected"
        mtext='Error'
    params["process_type"]=ptype_text
    params["anlaysed_text"]=mtext
    resp=render(request,'analysed.html',params)
    return resp

def analyse(request):
    resp=render(request,'analyse.html')
    return resp
