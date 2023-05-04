# Proteger archivos estáticos en Django con Nginx

Cuando queramos proteger ciertos archivos, por ejemplo, los archivos subidos en la carpeta `media/` tenemos que realizar cierta configuración tanto en **Nginx** como en **Django** debido a que Nginx sirve los archivos estáticos de manera pública por default. A continuación se muestra un ejemplo de como proteger nuestros archivos.

## 1. archivo `views.py`
Con esta vista se valida lo siguiente si el usuario **está autenticado** se crea una respuesta con la cabecera `X-Accel-Redirect` a la url del servidor `/protectedMedia/<ruta_y_nombre_del_archivo>` , con esto el servidor podrá responder servir el archivo para que este usuario lo pueda ver. Si **no está autenticado** no se muestra el archivo ni se puede acceder a este.
```python
@login_required
def mostrar_documento_protegido(request, path):
    access_granted = False
    try:
        #sessionid = request.session.session_key
        user = request.user
        # Usuario admin de Django

        if user.is_authenticated:
            access_granted = True

        if access_granted:
            response = HttpResponse()
            # Content-type will be detected by nginx
            response['Content-Type'] = ''
            response['X-Accel-Redirect'] = '/protectedMedia/' + path
            return response
        else:
            return HttpResponseForbidden('Not authorized to access this media.')

    except Exception as err:
        print(err)
        return HttpResponseForbidden('Error al acceder al recurso.')
        
```

## 2. archivo `urls.py`
Se crea una **url** para la ruta **media** con esto nos aseguramos de que nuestra vista se ejecute cuando accedan a un archivo de **media**.
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)', posts_views.mostrar_documento_protegido, name='serve_protected_document'),
]
```

## 3. archivo de configuración de la aplicación `nginx`
Por último la configuración en **Nginx** deberá ser la siguiente. Nótese que no existe una ruta para `/media` esto debido que queremos que nuestra vista de **mostrar_documento_protegido** entre en juego cuando se entre a la ruta `/media` por lo que la ruta que se encarga de mostrar los archivos es `/protectedMedia` y la regla `internal` nos ayuda a que los archivos no se muestren de manera **pública**:


```nginx
upstream instagram {
	server 127.0.0.1:8000;
}

server {
	listen 80;
	listen [::]:80;
	server_name 54.86.30.108;

	location /static {
		alias /home/ubuntu/instagram/staticfiles;
	}
	
	location /protectedMedia {
		internal;
		alias /home/ubuntu/instagram/media/;
	}

	location / {
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header Host $http_host;
		proxy_redirect off;
		proxy_pass http://instagram;
	}

}
```
