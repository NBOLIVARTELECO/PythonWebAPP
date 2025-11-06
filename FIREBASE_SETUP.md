# 🔥 Configuración de Firebase - Solución de Errores 401

## Error 401: Unauthorized

Si estás recibiendo el error `401 Client Error: Unauthorized`, significa que Firebase está rechazando las peticiones. Esto generalmente se debe a:

1. **Reglas de seguridad de Firebase Realtime Database**
2. **Credenciales incorrectas o expiradas**
3. **URL de base de datos incorrecta**

## Solución Paso a Paso

### 1. Verificar las Reglas de Seguridad de Firebase

El problema más común es que las reglas de seguridad de Firebase están bloqueando el acceso. Necesitas configurar las reglas para permitir el acceso desde el Admin SDK.

#### Pasos:

1. Ve a la [Consola de Firebase](https://console.firebase.google.com/)
2. Selecciona tu proyecto (`testvscode-5996d`)
3. Ve a **Realtime Database** en el menú lateral
4. Haz clic en la pestaña **Rules** (Reglas)
5. Cambia las reglas a:

```json
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null",
    "users": {
      ".read": true,
      ".write": true
    }
  }
}
```

**⚠️ IMPORTANTE:** Estas reglas permiten acceso público a la ruta `/users`. Para producción, deberías usar autenticación.

**Para desarrollo/educación, puedes usar reglas más permisivas temporalmente:**

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

6. Haz clic en **Publish** (Publicar)

### 2. Verificar el Archivo de Credenciales

Asegúrate de que el archivo `testvscode.json` existe y contiene las credenciales correctas:

1. Ve a **Project Settings > Service Accounts**
2. Haz clic en **Generate new private key**
3. Descarga el archivo JSON
4. Renombra el archivo a `testvscode.json`
5. Colócalo en la raíz del proyecto

### 3. Verificar la URL de la Base de Datos

Asegúrate de que el archivo `.env` contiene la URL correcta de tu base de datos:

1. Ve a **Realtime Database** en Firebase Console
2. Copia la URL de la base de datos (debería ser algo como: `https://testvscode-5996d-default-rtdb.firebaseio.com`)
3. Añade esta URL a tu archivo `.env`:

```env
DATABASE_URL=https://testvscode-5996d-default-rtdb.firebaseio.com
SECRET_KEY=tu_clave_secreta_aqui
```

### 4. Verificar que el Proyecto de Firebase está Activo

Asegúrate de que:
- El proyecto de Firebase está activo
- La Realtime Database está habilitada
- No hay restricciones de facturación que bloqueen el acceso

## Verificación

Después de hacer estos cambios:

1. Reinicia la aplicación Flask
2. Intenta acceder a la página principal
3. Si el error persiste, verifica los logs de la consola para ver mensajes más específicos

## Reglas de Seguridad Recomendadas para Producción

Para producción, usa reglas más seguras:

```json
{
  "rules": {
    "users": {
      "$uid": {
        ".read": "$uid === auth.uid",
        ".write": "$uid === auth.uid"
      }
    }
  }
}
```

## Alternativa: Usar Firestore

Si sigues teniendo problemas con Realtime Database, considera usar Firestore, que tiene un sistema de autenticación más robusto.

## Contacto

Si el problema persiste después de seguir estos pasos, verifica:
- Los logs de Firebase Console
- Los logs de la aplicación Flask
- Que las credenciales no hayan expirado

