from flask import Flask,render_template,request,url_for,session,redirect
class home:
    def index():
        return render_template('./cr_acc.html')
