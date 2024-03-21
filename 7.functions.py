def message_creator(text):
   # Escribe tu solución 👇
   message ="Artículo no encontrado"
   if text == "computadora":
      message = "Con mi computadora puedo programar usando Python"
   elif text == "celular":
      message = "En mi celular puedo aprender usando la app de Platzi"
   elif text == "cable":
      message ="¡Hay un cable en mi bota!"

   return message

text = 'computadora'
response = message_creator(text)
print(response)