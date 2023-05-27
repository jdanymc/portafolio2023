from flask import Flask, render_template, request, redirect,url_for, flash,session
from . import admin # importa bluerprint

import pyrebase
from app.firebase_config import firebaseConfig

fb_app = pyrebase.initialize_app(firebaseConfig)
auth = fb_app.auth()

from app import fb
from .forms import ProyectoForm
from .forms import RedForm

@admin.route('/')
def index():
    if('token' not in session):
        return redirect(url_for('admin.login'))
   
    return render_template('admin/index.html')


""" VISTAS PARA LOGIN """
@admin.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            usuario = auth.sign_in_with_email_and_password(email,password)
            data_usuario = auth.get_account_info(usuario['idToken'])
            print(data_usuario)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.index'))
            #return render_template('admin/index.html')
        except:
            print('Usuario no válido')
            flash('Usuario o password no válido')
            #return render_template('admin/login.html')
        
    return render_template('admin/login.html')

@admin.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('admin.index'))

@admin.route('/proyectos',methods=['GET','POST'])
def proyectos():
    if('token' not in session):
        return redirect(url_for('admin.login'))
    
    lista_proyectos = fb.get_collection('proyectos')
    proyecto_form = ProyectoForm()

    if proyecto_form.validate_on_submit():
        #registrar nuevo proyecto
        data_nuevo_proyecto={
            'nombre':proyecto_form.nombre.data,
            'descripcion':proyecto_form.descripcion.data,
            'imagen':proyecto_form.imagen.data,
        }


        nuevo_proyecto = fb.insert_document('proyectos',data_nuevo_proyecto)

        return redirect(url_for('admin.proyectos'))


    context = {
        'proyectos':lista_proyectos,
        'proyecto_form':proyecto_form,
    }
    #"print(lista_proyectos)
    return render_template('admin/proyectos.html',**context)

@admin.route('/proyecto/<id>',methods=['GET','POST'])
def proyecto(id=''):
    if('token' not in session):
        return redirect(url_for('admin.login'))
    
    lista_proyectos = fb.get_collection('proyectos')
    proyecto_data = fb.get_document('proyectos',id)
   # print(proyecto_data)

    proyecto_form = ProyectoForm(data=proyecto_data)

##actualizar el proyecto
    if proyecto_form.validate_on_submit():
        #registrar nuevo proyecto
        data_proyecto_actualizar = {
            'nombre': proyecto_form.nombre.data,
            'descripcion':proyecto_form.descripcion.data,
            'imagen':proyecto_form.imagen.data
        }
        proyecto_actualizado = fb.update_document('proyectos',id,data_proyecto_actualizar)
       # print(nuevo_proyecto)
        
        return redirect(url_for('admin.proyectos'))

    context = { 
        'proyectos':lista_proyectos,
        'proyecto_form':proyecto_form,
    }
    return render_template('admin/proyectos.html',**context)

@admin.route('/delproyecto/<id>')
def del_proyecto(id=''):
    if('token' not in session):
        return redirect(url_for('admin.login'))
    
    resultado_del_proyecto = fb.delete_document('proyectos',id)
    if(resultado_del_proyecto==True):
        return redirect(url_for('admin.proyectos'))
    
@admin.route('/redes',methods=['GET','POST'])
def redes():
    if('token' not in session):
        return redirect(url_for('admin.login'))
    
    lista_redes = fb.get_collection('redes_sociales')
    red_form = RedForm()

    if red_form.validate_on_submit():
        #registrar nuevo proyecto
        data_nueva_red={
            'icono':red_form.icono.data,
            'url':red_form.url.data,
        }


        nueva_red = fb.insert_document('redes_sociales',data_nueva_red)

        return redirect(url_for('admin.redes'))


    context = {
        'redes':lista_redes,
        'red_form':red_form,
    }
    #"print(lista_proyectos)
    return render_template('admin/redes.html',**context)

@admin.route('/red/<id>',methods=['GET','POST'])
def red(id=''):
    if('token' not in session):
        return redirect(url_for('admin.login'))
    
    lista_redes = fb.get_collection('redes_sociales')
    red_data = fb.get_document('redes_sociales',id)
   # print(proyecto_data)

    red_form = RedForm(data=red_data)

##actualizar el proyecto
    if red_form.validate_on_submit():
        #registrar nuevo proyecto
        data_red_actualizar = {
            'icono': red_form.icono.data,
            'url':red_form.url.data,
        }
        red_actualizado = fb.update_document('redes_sociales',id,data_red_actualizar)
       # print(nuevo_proyecto)
        
        return redirect(url_for('admin.redes'))

    context = { 
        'redes':lista_redes,
        'red_form':red_form,
    }
    return render_template('admin/redes.html',**context)

@admin.route('/delred/<id>')
def del_red(id=''):
    if('token' not in session):
        return redirect(url_for('admin.login'))
    
    resultado_del_red = fb.delete_document('redes_sociales',id)
    if(resultado_del_red==True):
        return redirect(url_for('admin.redes'))
    
