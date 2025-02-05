1 - Para ejecutar la API rest en Postman escribo lo siguiente en la terminal de VSC: 'uvicorn main:app --reload', copio el https y lo coloco en un get en Postman.
2 - Voy a send y si está todo bien, creo una ventana con POST, lo convierto a JSON mediante el body, creo los cursos que quiera, le doy a send en POST y GET me devuelve la lista de cursos.
3 - PUT: Le paso un curso concreto a modificar previa conversión a JSON en el body, luego de ser modificado le doy a send desde el PUT y a GET para obtener el curso o cursos modificados.
4 - DEL: Simplemente le paso la ID (PUT tambien necesita el ID) y mediante esta info, borra el curso en concreto.
NOTA: no hay que hacer estos pasos en concreto, solo explico como funciona GET,POST,PUT y DEL para verificar que funcionen bien.
