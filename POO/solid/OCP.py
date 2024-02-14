#OCP (open close principle)

class Usuario:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError


class NotificadorEmail(Notificador):
    def notificar(self):
        print(f"Enviando mensaje por mail a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f"Enviando SMS a {self.usuario.phone}")

class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f"Enviando WhatsApp a {self.usuario.phone}")

usuario_info = {"email": "johndoe@example.com", "phone": "+1234567890"}
usuario = Usuario(email=usuario_info["email"], phone=usuario_info["phone"])
mensaje = "Este es un mensaje de prueba."

notificador_email = NotificadorEmail(usuario, mensaje)
notificador_sms = NotificadorSMS(usuario, mensaje)
notificador_wp = NotificadorWhatsApp(usuario, mensaje)

notificador_email.notificar()
notificador_sms.notificar()
notificador_wp.notificar()
