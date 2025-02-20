import webbrowser
import os

# Mensaje de detalle en HTML con un sobre clicable
html = """
<!DOCTYPE html>
<html>
<head>
<title>Un pequeño detalle para ti</title>
<style>
    body { text-align: center; font-family: Arial, sans-serif; margin: 0; padding: 20px; }
    .envelope { cursor: pointer; margin-top: 50px; width: 100%; max-width: 200px; }
    .message { display: none; margin-top: 50px; position: relative; }
    img { width: 100%; max-width: 250px; }
    .corner { position: absolute; width: 100px; }
    .top-left { top: 0; left: 0; }
    .top-right { top: 0; right: 0; }
    .bottom-left { bottom: 0; left: 0; }
    .bottom-right { bottom: 0; right: 0; }
</style>
<script>
    function openMessage() {
        document.getElementById('message').style.display = 'block';
        document.getElementById('envelope').style.display = 'none';
    }
</script>
</head>
<body>
<h1>🌹Hola Paula!🌹</h1>
<p>Por favor haz clic en el sobre para abrir tu mensaje:</p>
<img id="envelope" class="envelope" src="https://i.pinimg.com/736x/b3/4d/34/b34d342d4fd2082809e0d221c82dcef6.jpg" alt="Sobre" onclick="openMessage()">
<div id="message" class="message">
    <img src="https://media.tenor.com/eluzziNsiUIAAAAM/triste-sad.gif" alt="Top Left" class="corner top-left">
    <img src="https://media.tenor.com/eluzziNsiUIAAAAM/triste-sad.gif" alt="Top Right" class="corner top-right">
    <img src="https://media.tenor.com/eluzziNsiUIAAAAM/triste-sad.gif" alt="Bottom Left" class="corner bottom-left">
    <img src="https://media.tenor.com/eluzziNsiUIAAAAM/triste-sad.gif" alt="Bottom Right" class="corner bottom-right">
    <h1>Carta</h1>
    <p>Querida Paula<p>
    <p>Queria escribirte una carta una vez mas la verdad por que siento que hay muchas cosas que no te he dicho aún🌹</p>
    <p>Me alegro de haber logrado hablar contigo de nuevo después de meses, espero que siempre estes bien. Te agradezco el tiempo que se das para leer y ver esta carta .</p>
    <p><img src="https://i.pinimg.com/originals/20/7c/f9/207cf91b056be0b7554fcde744208518.gif" alt="Corazón"></p>
    <p>Para mi es relevante poder decirte lo importante que eres para mi, la verdad desde que te vi te llevaste mis pensamientos y mi corazón, y cuando por fin logre hablar contigo fue algo muy bonito, es algo muy relevante y maravilloso poder al menos intercambiar unos pocos mensajes con la persona que uno ama, tu forma de ser junto a tu belleza te hacen una mujer unica e incomparable que vale la pena, y a pesar de muchas cosas siempre te he buscado tratando de demostrarte lo importante que eres para mi y qu quiero estar ahicontigo en las buenas y en las malas, el amor que te tengo es tan grande que me importa que estes bien y asi mismo me arrepiento d eno haberte llamado antes y te pido perdon por no haber buscado la manera de estar a tu lado en el momento tan dificil que estas pasando, solo puedo decir que comprendo el dolor que pasas, por que la unica que lo siente eres tu, enserio te pido perdón, la verdad en estos momentso me gustaria poder demostrarte que no estas sola y que yo incondicionalmente estare contigo por que eres muy valiosa para mi. </p>
    <p>Tambien te escribo esta carta por que si me duele el no poder gustarte ni siquiera poder intentarlo, mis sentimientos por ti son reales y bueno a la final tu eres quien tiene la ultima palabra, pero: <br> 
    🌹No podrias reconsiderar tu respuesta?, podrias darme la oportunidad de demostrarte que te amo de verdad?, no te pido que pases pegada a mi, solo te pido que me permitas ganarme tu amor, con que me regalaras 5 minutos o una llamada como ayer te prometo que para mi es suficiente prometo ser paciente, esperarte y amarte, Porfavor: ¿Podrias reconsiderarlo? Solo te pido 1 portunidad🌹
    <p>Te envio un fuerte abrazo y un beso, ya sea que me aceptes o no quiero q sepas que siempre tendras un lugar especial en mi corazón, mi amor y mi corazón son tuyos, ¿Qué piensas hacer con eso?, porfavor piensalo Meleğim❤, cuando leas esto podrias decirme que piensas porfavor <br>
    Att: Anthony.😊</p>
    <p>🌹Ты самая красивая и никогда не меняешься.🌹</p>
    <p>El video es por si no aceptas darme una oportunidad, siento que expresa como me siento estando lejos de ti, eres la mas hermosa del mundo y bueno tu eres la unica que puede decidir esto, yo quiero ser honesto y al menos decirte lo que siento por ti desde hace mucho tiempo y como dice la canción algun dia sueño y espero que se cumpla la frase: "Se que volveras"".<p>
    <video controls>
        <source src="tu_video.mp4" type="video/mp4">
        Tu navegador no soporta el elemento de video.
    </video>
</div>
</body>
</html>
"""

# Guarda el mensaje en un archivo HTML con codificación UTF-8
with open("detalle_para_paula.html", "w", encoding="utf-8") as file:
    file.write(html)

# Abre el archivo HTML en una nueva pestaña del navegador
webbrowser.open("file://" + os.path.realpath("detalle_para_paula.html"))
