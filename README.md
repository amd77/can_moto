# Leer bus CAN


## Pasos hardware

Estuve barajando entre el MCP2515 y el SN65HVD230 para conectar al bus CAN. El
SN65HVD230 era mas barato (1 euro) pero lo descarté porque era demasiado low
level. Usé un MCP2515 (5 euros), que daba las tramas CAN ya decodificadas.

Ademas es necesario un arduino. En el arduino ide agregar la libreria
arduino-CAN y flashear el ino, que es un CANReceiver tuneado.

https://github.com/sandeepmistry/arduino-CAN/blob/master/examples/CANReceiver/CANReceiver.ino

Los programas de python son:

* `capture.py nombredefichero.txt` para leer de `/dev/ttyUSB0` y guardar los
logs en fichero

* `display.py nombredefichero.txt` para visualizarlos en tiempo real diferido
en forma de "array cambiante", dando diferentes estadísticas por cada código,
como el número de mensajes, número de cambios, tiempo del ultimo mensaje, etc.


## Torrot Muvi

Este proyecto empezó porque me interesaba diagnosticar las baterías y no
recibia soporte oficial por bancarrota de la empresa. Las baterias van con bus
485 a una segunda controladora intermedia (que está en la propia bateria) y que
lo convierte a CAN. Al final resolví el tema con un repuesto oficial y se quedó
este proyecto aparcado.

El bus can se puede obtener de los conectores de la bateria, pero implicaría
hacer un ladrón y sacarlo hacia afuera.

Afortunadamente el bus can está en varios sitios. El más sencillo es en el
centro debajo (encima de la chapa de protección de la controladora) hay un
conector aereo de 2 con un tapón que es el bus can. Para un acceso más
sencillo, yo saqué ese conector por debajo del reposapies izquierdo, y así está
más a mano.

Al conectar el montaje del mcp+arduino a ese bus can y encender el contacto,
empiezan a salir mensajes con códigos. 

Luego te puedes poner a mover el acelerador, a quitar/poner la pata, etc y
verás que solo uno de los mensajes cambia sincronizado con tu acción.

La idea final era ir descubriendo que significaba cada mensaje. En aquel
momento solo descubrí uno, pero tampoco le puse mucho empeño. Está en el
`README.md` de la carpeta `torrot_muvi`.
