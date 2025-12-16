# 📌 Conectar Django con PostgreSQL — Guía Completa

Esta guía te mostrará paso a paso cómo conectar un proyecto **Django** con una base de datos **PostgreSQL** de forma profesional.

---

# 🧱 1. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

### ✅ PostgreSQL

Descárgalo desde la web oficial.

Incluye también **pgAdmin** (opcional, pero muy útil).

### ✅ Python + Django

```
pip install django
```

### ✅ Conector Psycopg

Django usa **psycopg** como driver para conectarse a PostgreSQL.

```
pip install psycopg2-binary
```

> Si usas producción, lo ideal es instalar `psycopg2` en vez de `binary`.

---

# 🛠️ 2. Crear Base de Datos en PostgreSQL

1. Abre **pgAdmin** o la terminal.
2. Crea una nueva base llamada:

```
mi_proyecto_db
```

3. Crea un usuario con contraseña:

```
CREATE USER miusuario WITH PASSWORD 'miclave';
```

4. Dale permisos:

```
ALTER ROLE miusuario SET client_encoding TO 'utf8';
ALTER ROLE miusuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE miusuario SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE mi_proyecto_db TO miusuario;
```

---

# ⚙️ 3. Configurar Django para usar PostgreSQL

En tu proyecto Django, abre:

```
settings.py
```

Busca la sección `DATABASES` y reemplázala por:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mi_proyecto_db',
        'USER': 'miusuario',
        'PASSWORD': 'miclave',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🔍 Explicación de cada campo

* **ENGINE** → Django usará PostgreSQL
* **NAME** → nombre de tu base
* **USER** → usuario creado en PostgreSQL
* **PASSWORD** → clave del usuario
* **HOST** → dónde está la base (local o remoto)
* **PORT** → puerto default de PostgreSQL

---

# 🧪 4. Probar la Conexión

Corre:

```
python manage.py migrate
```

Si todo está bien, Django creará automáticamente sus tablas en PostgreSQL.

---

# 📤 5. Crear un Superusuario

```
python manage.py createsuperuser
```

Inicia sesión en admin para verificar que todo funciona:

```
http://127.0.0.1:8000/admin/
```

---

# 🧩 6. Uso en Producción (Importante)

Cuando subas tu proyecto a un servidor (Ubuntu, Docker, Render, Railway, etc.) sigue estas reglas:

### 🔐 Usa variables de entorno

Nunca pongas la clave directamente en `settings.py`.

Ejemplo:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

Exportarlas en Linux:

```
export DB_NAME=mi_proyecto_db
export DB_USER=miusuario
export DB_PASSWORD=miclave
export DB_HOST=localhost
```

### ⚠️ Configurar PostgreSQL para conexiones remotas

Editar:

```
/etc/postgresql/15/main/postgresql.conf
```

Cambiar:

```
listen_addresses = '*'
```

Luego editar:

```
/etc/postgresql/15/main/pg_hba.conf
```

Agregar:

```
host    all     all     0.0.0.0/0       md5
```

Reiniciar PostgreSQL:

```
sudo service postgresql restart
```

---

# 📊 7. Verificar Que Django Está Usando PostgreSQL

Abre la consola Django:

```
python manage.py dbshell
```

Si entras al shell de PostgreSQL, ¡todo está bien!

Prueba una consulta:

```
SELECT * FROM auth_user;
```

---

# 🧱 8. Crear un Modelo y Probar Datos

Ejemplo:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
```

Migrar:

```
python manage.py makemigrations
python manage.py migrate
```

Crear registro en shell:

```
python manage.py shell
```

```python
from tienda.models import Producto
Producto.objects.create(nombre="Mouse", precio=30.000)
```

---

# 📦 9. Checklist Final

✔ PostgreSQL instalado
✔ Base creada
✔ Usuario + permisos configurados
✔ `psycopg2-binary` instalado
✔ `settings.py` configurado
✔ Migraciones funcionando
✔ Admin accesible
✔ Datos probados

---

# 🎉 ¡Conexión lista!

Tu proyecto Django ahora usa una **base de datos real**, optimizada, segura y profesional. Si quieres, puedo agregar:

* Plantillas reales de `.env`
* Docker Compose para PostgreSQL + Django
* Guía para deploy en Render/Railway
* Optimización avanzada para producción (índices, tuning, etc.)

Solo pídelo 👌
