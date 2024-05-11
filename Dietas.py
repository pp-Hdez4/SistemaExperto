from experta import *
import os
import pdfkit
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def limpiar_pantalla():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        
def convertir_html_a_pdf(html_content, output_filename):
    try:
        output_path = "Dietas"
        # Crear la carpeta Dietas si no existe
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Crear el documento PDF
        output_file = os.path.join(output_path, output_filename)
        doc = SimpleDocTemplate(output_file, pagesize=letter)
        styles = getSampleStyleSheet()
        flowables = []

        # Separar el contenido HTML en líneas y crear un Paragraph para cada línea
        lines = html_content.strip().split('\n')
        for line in lines:
            p = Paragraph(line, styles['Normal'])
            flowables.append(p)
            flowables.append(Spacer(1, 12))  # Agregar espacio entre párrafos

        # Construir el PDF
        doc.build(flowables)

        limpiar_pantalla()
        print("Dieta generada con éxito!")
        print(f"El PDF se ha guardado en: {output_file}")
    except Exception as e:
        print(f"Error al generar el PDF: {e}")


class Dieta(Fact):
    """Información sobre la dieta."""
    pass


class SistemaExperto(KnowledgeEngine):
    #------------------Dietas sin problemas medicos / ACTIVIDAD FISIFCA = SI----------------------------------
    @Rule(Dieta(objetivo="perder peso"),
      Dieta(actividad_fisica="si"),
      Dieta(problemas_medicos="no"),
      Dieta(embarazo="no"))
    def dieta_para_perder_peso_activo(self):
        limpiar_pantalla()
        print("Dieta para perder peso (activo):")
        print("\nLunes:")
        print("- Desayuno: Batido de frutas con yogur bajo en grasa.")
        print("- Almuerzo: Ensalada de espinacas, queso feta y nueces.")
        print("- Cena: Pechuga de pollo a la plancha con espárragos al vapor.")
        
        print("\nMartes:")
        print("- Desayuno: Avena cocida con trozos de manzana y canela.")
        print("- Almuerzo: Salmón al horno con brócoli al vapor.")
        print("- Cena: Ensalada de quinoa con vegetales asados.")
        
        print("\nMiércoles:")
        print("- Desayuno: Tortilla de claras de huevo con espinacas y tomates cherry.")
        print("- Almuerzo: Filete de pavo a la plancha con espárragos a la parrilla.")
        print("- Cena: Sopa de verduras con pollo desmenuzado.")
        
        print("\nJueves:")
        print("- Desayuno: Batido de proteínas con espinacas y plátano.")
        print("- Almuerzo: Ensalada de garbanzos, pepino y tomate con vinagreta de limón.")
        print("- Cena: Pescado al horno con espárragos y zanahorias al vapor.")
        
        print("\nViernes:")
        print("- Desayuno: Yogur griego con nueces y arándanos.")
        print("- Almuerzo: Tiras de pollo a la parrilla con ensalada de col.")
        print("- Cena: Berenjenas rellenas de carne magra y verduras.")
        
        print("\nSábado:")
        print("- Desayuno: Tostadas integrales con aguacate y huevo pochado.")
        print("- Almuerzo: Sopa de lentejas con verduras y un poco de queso parmesano.")
        print("- Cena: Brochetas de camarones con vegetales a la parrilla.")
        
        print("\nDomingo:")
        print("- Desayuno: Smoothie de espinacas, piña y jengibre.")
        print("- Almuerzo: Pollo al curry con arroz integral y verduras al vapor.")
        print("- Cena: Salmón a la plancha con espárragos y batata al horno.")
        
        contenido = """
                <html>
                <head>
                    <title>Dieta para perder peso (activo)</title>
                </head>
                <body>
                    <h1>Dieta para perder peso (activo)</h1>
                    <h1>Lunes:</h1>
                    <h2>Desayuno:</h2>
                    <p>- Batido de frutas con yogur bajo en grasa.</p>
                    <p>- Almuerzo: Ensalada de espinacas, queso feta y nueces.</p>
                    <p>- Cena: Pechuga de pollo a la plancha con espárragos al vapor.</p>

                    <h1>Martes:</h1>
                    <h2>Desayuno:</h2>
                    <p>- Avena cocida con trozos de manzana y canela.</p>
                    <p>- Almuerzo: Salmón al horno con brócoli al vapor.</p>
                    <p>- Cena: Ensalada de quinoa con vegetales asados.</p>

                    <h1>Miércoles:</h1>
                    <h2>Desayuno:</h2>
                    <p>- Tortilla de claras de huevo con espinacas y tomates cherry.</p>
                    <p>- Almuerzo: Filete de pavo a la plancha con espárragos a la parrilla.</p>
                    <p>- Cena: Sopa de verduras con pollo desmenuzado.</p>

                    <h1>Jueves:</h1>
                    <h2>Desayuno:</h2>
                    <p>- Batido de proteínas con espinacas y plátano.</p>
                    <p>- Almuerzo: Ensalada de garbanzos, pepino y tomate con vinagreta de limón.</p>
                    <p>- Cena: Pescado al horno con espárragos y zanahorias al vapor.</p>

                    <h1>Viernes:</h1>
                    <h2>Desayuno:</h2>
                    <p>- Yogur griego con nueces y arándanos.</p>
                    <p>- Almuerzo: Tiras de pollo a la parrilla con ensalada de col.</p>
                    <p>- Cena: Berenjenas rellenas de carne magra y verduras.</p>

                    <h1>Sábado:</h1>
                    <h2>Desayuno:</h2>
                    <p>- Tostadas integrales con aguacate y huevo pochado.</p>
                    <p>- Almuerzo: Sopa de lentejas con verduras y un poco de queso parmesano.</p>
                    <p>- Cena: Brochetas de camarones con vegetales a la parrilla.</p>

                    <h1>Domingo:</h1>
                    <h2>Desayuno:</h2>
                    <p>- Smoothie de espinacas, piña y jengibre.</p>
                    <p>- Almuerzo: Pollo al curry con arroz integral y verduras al vapor.</p>
                    <p>- Cena: Salmón a la plancha con espárragos y batata al horno.</p>
                </body>
                </html>
            """
             # Nombre del archivo de salida PDF
        nombre_archivo_pdf = 'dieta_para_perder_peso_activo.pdf'
        print("Presiona enter para generar el PDF de la dieta \n")
        input()

        # Convertir HTML a PDF utilizando la función separada
        convertir_html_a_pdf(contenido, nombre_archivo_pdf)
            
        
        



    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="no"))
    def dieta_para_mantener_peso_activo(self):
        limpiar_pantalla()
        print("Dieta para mantener peso (activo):")
        print("\nLunes:")
        print("- Desayuno: Tostadas integrales con aguacate y huevo revuelto.")
        print("- Almuerzo: Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.")
        print("- Cena: Filete de salmón al horno con espárragos y batata asada.")

        print("\nMartes:")
        print("- Desayuno: Batido de proteínas con espinacas, plátano y leche de almendras.")
        print("- Almuerzo: Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.")
        print("- Cena: Tacos de pescado con tortillas de maíz, repollo rallado y salsa de yogur.")

        print("\nMiércoles:")
        print("- Desayuno: Avena cocida con rodajas de manzana, canela y almendras.")
        print("- Almuerzo: Tiras de carne magra salteadas con pimientos y cebolla, servidas con arroz integral.")
        print("- Cena: Sopa de verduras con garbanzos y un trozo de pan integral.")

        print("\nJueves:")
        print("- Desayuno: Yogur griego con granola y frutos rojos.")
        print("- Almuerzo: Ensalada de lentejas con espinacas, tomate y aguacate.")
        print("- Cena: Pechuga de pollo al horno con brócoli al vapor y puré de papas.")

        print("\nViernes:")
        print("- Desayuno: Tostadas de pan integral con crema de cacahuate y plátano en rodajas.")
        print("- Almuerzo: Salmón al horno con espárragos y quinoa cocida.")
        print("- Cena: Ensalada de garbanzos con tomate, pepino, cebolla morada y aderezo de tahini.")

        print("\nSábado:")
        print("- Desayuno: Tortilla de claras de huevo con espinacas y champiñones.")
        print("- Almuerzo: Pollo al curry con arroz basmati y verduras al vapor.")
        print("- Cena: Rollitos de sushi con relleno de salmón, aguacate y pepino.")

        print("\nDomingo:")
        print("- Desayuno: Smoothie de frutas con espinacas y semillas de chía.")
        print("- Almuerzo: Hamburguesas de pavo a la parrilla con ensalada verde y papas asadas.")
        print("- Cena: Pasta integral con salsa de tomate casera y albóndigas de carne magra.")
        
        contenido = """
                    <html>
                    <head>
                        <title>Dieta para mantener peso (activo)</title>
                    </head>
                    <body>
                        <h1>Dieta para mantener peso (activo)</h1>
                        <h1>Lunes:</h1>
                        <h2>Desayuno:</h2>
                        <p>- Tostadas integrales con aguacate y huevo revuelto.</p>
                        <h2>Almuerzo:</h2>
                        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
                        <h2>Cena:</h2>
                        <p>- Filete de salmón al horno con espárragos y batata asada.</p>

                        <h1>Martes:</h1>
                        <h2>Desayuno:</h2>
                        <p>- Batido de proteínas con espinacas, plátano y leche de almendras.</p>
                        <h2>Almuerzo:</h2>
                        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>
                        <h2>Cena:</h2>
                        <p>- Tacos de pescado con tortillas de maíz, repollo rallado y salsa de yogur.</p>

                        <h1>Miércoles:</h1>
                        <h2>Desayuno:</h2>
                        <p>- Avena cocida con rodajas de manzana, canela y almendras.</p>
                        <h2>Almuerzo:</h2>
                        <p>- Tiras de carne magra salteadas con pimientos y cebolla, servidas con arroz integral.</p>
                        <h2>Cena:</h2>
                        <p>- Sopa de verduras con garbanzos y un trozo de pan integral.</p>

                        <h1>Jueves:</h1>
                        <h2>Desayuno:</h2>
                        <p>- Yogur griego con granola y frutos rojos.</p>
                        <h2>Almuerzo:</h2>
                        <p>- Ensalada de lentejas con espinacas, tomate y aguacate.</p>
                        <h2>Cena:</h2>
                        <p>- Pechuga de pollo al horno con brócoli al vapor y puré de papas.</p>

                        <h1>Viernes:</h1>
                        <h2>Desayuno:</h2>
                        <p>- Tostadas de pan integral con crema de cacahuate y plátano en rodajas.</p>
                        <h2>Almuerzo:</h2>
                        <p>- Salmón al horno con espárragos y quinoa cocida.</p>
                        <h2>Cena:</h2>
                        <p>- Ensalada de garbanzos con tomate, pepino, cebolla morada y aderezo de tahini.</p>

                        <h1>Sábado:</h1>
                        <h2>Desayuno:</h2>
                        <p>- Tortilla de claras de huevo con espinacas y champiñones.</p>
                        <h2>Almuerzo:</h2>
                        <p>- Pollo al curry con arroz basmati y verduras al vapor.</p>
                        <h2>Cena:</h2>
                        <p>- Rollitos de sushi con relleno de salmón, aguacate y pepino.</p>

                        <h1>Domingo:</h1>
                        <h2>Desayuno:</h2>
                        <p>- Smoothie de frutas con espinacas y semillas de chía.</p>
                        <h2>Almuerzo:</h2>
                        <p>- Hamburguesas de pavo a la parrilla con ensalada verde y papas asadas.</p>
                        <h2>Cena:</h2>
                        <p>- Pasta integral con salsa de tomate casera y albóndigas de carne magra.</p>
                    </body>
                    </html>
                    """
        nombre_archivo_pdf = 'dieta_para_mantener_peso_activo.pdf'
        print("Presiona enter para generar el PDF de la dieta \n")
        input()
        # Convertir HTML a PDF utilizando la función separada
        convertir_html_a_pdf(contenido, nombre_archivo_pdf)


    @Rule(Dieta(objetivo="perder peso"),
      Dieta(actividad_fisica="no"),
      Dieta(problemas_medicos="no"),
      Dieta(embarazo="no"))
    def dieta_para_sedentario(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria [Perder peso]:")
        print("\nLunes:")
        print("- Desayuno: Té verde con tostadas integrales y aguacate.")
        print("- Almuerzo: Ensalada de espinacas, tomate y pechuga de pollo a la plancha.")
        print("- Cena: Sopa de verduras con un trozo de pan integral.")

        print("\nMartes:")
        print("- Desayuno: Yogur natural con granola y frutos rojos.")
        print("- Almuerzo: Salmón al horno con brócoli al vapor.")
        print("- Cena: Ensalada de garbanzos con tomate, pepino y aderezo de limón.")

        print("\nMiércoles:")
        print("- Desayuno: Batido de frutas con espinacas.")
        print("- Almuerzo: Pavo al horno con ensalada verde.")
        print("- Cena: Tortilla de claras con champiñones y espinacas.")

        print("\nJueves:")
        print("- Desayuno: Avena cocida con rodajas de manzana y canela.")
        print("- Almuerzo: Ensalada de quinoa con vegetales asados.")
        print("- Cena: Pechuga de pollo a la plancha con espárragos.")

        print("\nViernes:")
        print("- Desayuno: Tostadas integrales con mantequilla de almendras y plátano en rodajas.")
        print("- Almuerzo: Atún al natural con ensalada de tomate y aguacate.")
        print("- Cena: Berenjenas al horno con queso fresco.")

        print("\nSábado:")
        print("- Desayuno: Smoothie de bayas con espinacas.")
        print("- Almuerzo: Lentejas estofadas con verduras.")
        print("- Cena: Ensalada de salmón ahumado con aguacate y pepino.")

        print("\nDomingo:")
        print("- Desayuno: Té de hierbas con tostadas integrales y mermelada sin azúcar añadido.")
        print("- Almuerzo: Pollo a la parrilla con espárragos al vapor.")
        print("- Cena: Crema de calabaza con un trozo de pan integral.")
        contenido = """
        <html>
        <head>
            <title>Dieta para una vida sedentaria [Perder peso]</title>
        </head>
        <body>
            <h1>Dieta para una vida sedentaria [Perder peso]</h1>
            <h1>Lunes:</h1>
            <h2>Desayuno:</h2>
            <p>- Té verde con tostadas integrales y aguacate.</p>
            <h2>Almuerzo:</h2>
            <p>- Ensalada de espinacas, tomate y pechuga de pollo a la plancha.</p>
            <h2>Cena:</h2>
            <p>- Sopa de verduras con un trozo de pan integral.</p>

            <h1>Martes:</h1>
            <h2>Desayuno:</h2>
            <p>- Yogur natural con granola y frutos rojos.</p>
            <h2>Almuerzo:</h2>
            <p>- Salmón al horno con brócoli al vapor.</p>
            <h2>Cena:</h2>
            <p>- Ensalada de garbanzos con tomate, pepino y aderezo de limón.</p>

            <h1>Miércoles:</h1>
            <h2>Desayuno:</h2>
            <p>- Batido de frutas con espinacas.</p>
            <h2>Almuerzo:</h2>
            <p>- Pavo al horno con ensalada verde.</p>
            <h2>Cena:</h2>
            <p>- Tortilla de claras con champiñones y espinacas.</p>

            <h1>Jueves:</h1>
            <h2>Desayuno:</h2>
            <p>- Avena cocida con rodajas de manzana y canela.</p>
            <h2>Almuerzo:</h2>
            <p>- Ensalada de quinoa con vegetales asados.</p>
            <h2>Cena:</h2>
            <p>- Pechuga de pollo a la plancha con espárragos.</p>

            <h1>Viernes:</h1>
            <h2>Desayuno:</h2>
            <p>- Tostadas integrales con mantequilla de almendras y plátano en rodajas.</p>
            <h2>Almuerzo:</h2>
            <p>- Atún al natural con ensalada de tomate y aguacate.</p>
            <h2>Cena:</h2>
            <p>- Berenjenas al horno con queso fresco.</p>

            <h1>Sábado:</h1>
            <h2>Desayuno:</h2>
            <p>- Smoothie de bayas con espinacas.</p>
            <h2>Almuerzo:</h2>
            <p>- Lentejas estofadas con verduras.</p>
            <h2>Cena:</h2>
            <p>- Ensalada de salmón ahumado con aguacate y pepino.</p>

            <h1>Domingo:</h1>
            <h2>Desayuno:</h2>
            <p>- Té de hierbas con tostadas integrales y mermelada sin azúcar añadido.</p>
            <h2>Almuerzo:</h2>
            <p>- Pollo a la parrilla con espárragos al vapor.</p>
            <h2>Cena:</h2>
            <p>- Crema de calabaza con un trozo de pan integral.</p>
        </body>
        </html>
        """
        nombre_archivo_pdf = 'dieta_para_sedentario_perder_peso.pdf'
        print("Presiona enter para generar el PDF de la dieta \n")
        input()
        # Convertir HTML a PDF utilizando la función separada
        convertir_html_a_pdf(contenido, nombre_archivo_pdf)

        

    @Rule(Dieta(objetivo="mantener peso"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="no"))
    def dieta_para_sedentario_mantenerpeso(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria: [mantener peso]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")  


    @Rule(Dieta(objetivo="ganar peso"),
      Dieta(actividad_fisica="no"),
      Dieta(problemas_medicos="no"),
      Dieta(embarazo="no"))
    def dieta_para_sedentario_ganarpeso(self):
        limpiar_pantalla()
        print("Dieta para una vida sedentaria: [ganar peso]")
        print("- Controlar las porciones y evitar alimentos altos en calorías.")
        print("- Priorizar alimentos integrales y frescos.")
        print("- Limitar el consumo de alimentos procesados y azucarados.")    



    #--------------------Fin dietas sin problemas medicos---------------------------------

    #------------------Dietas con problemas medicos / ACTIVIDAD FISIFCA = SI--------------------------------------
    @Rule(Dieta(objetivo="ganar peso"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_ganar_peso(self):
        limpiar_pantalla()
        print("Dieta para ganar peso: [Problemas medicos]")
        print("- Aumentar la ingesta de calorías con alimentos nutritivos.")
        print("- Incluir carbohidratos complejos, proteínas y grasas saludables.")
        print("- Realizar comidas frecuentes y snacks nutritivos.")

    @Rule(Dieta(objetivo="perder peso"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="no"))
    def dieta_para_perder_peso(self):
        limpiar_pantalla()
        print("Dieta para perder peso: [Problemas medicos]")
        print("- Aumentar la ingesta de calorías con alimentos nutritivos.")
        print("- Incluir carbohidratos complejos, proteínas y grasas saludables.")
        print("- Realizar comidas frecuentes y snacks nutritivos.")


    # -------------------------------------------------------------------------------
    @Rule(Dieta(objetivo="mantener peso"),
        Dieta(actividad_fisica="si"),
        Dieta(problemas_medicos="si"),
        Dieta(embarazo="no"))
    def dieta_para_mantener_peso(self):
        limpiar_pantalla()
        contenido = """
        <html>
        <head><title>Dieta para mantener peso con problemas médicos</title></head>
        <body>
        <h1>Dieta para mantener peso con problemas médicos</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Tostadas integrales con aguacate y huevo pochado.</p>
        <h2>Almuerzo:</h2>
        <p>- Sopa de lentejas con verduras y un poco de queso parmesano.</p>
        <h2>Cena:</h2>
        <p>- Salmón a la plancha con espárragos y batata al horno.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con espinacas y plátano.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de garbanzos, pepino y tomate con vinagreta de limón.</p>
        <h2>Cena:</h2>
        <p>- Pescado al horno con espárragos y zanahorias al vapor.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur griego con nueces y arándanos.</p>
        <h2>Almuerzo:</h2>
        <p>- Tiras de pollo a la parrilla con ensalada de col.</p>
        <h2>Cena:</h2>
        <p>- Berenjenas rellenas de carne magra y verduras.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con yogur bajo en grasa.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <h2>Cena:</h2>
        <p>- Ensalada de quinoa con vegetales asados.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Avena cocida con trozos de manzana y canela.</p>
        <h2>Almuerzo:</h2>
        <p>- Filete de pavo a la plancha con espárragos a la parrilla.</p>
        <h2>Cena:</h2>
        <p>- Sopa de verduras con pollo desmenuzado.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Smoothie de espinacas, piña y jengibre.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo al curry con arroz integral y verduras al vapor.</p>
        <h2>Cena:</h2>
        <p>- Pechuga de pollo a la plancha con espárragos al vapor.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Tortilla de claras de huevo con espinacas y tomates cherry.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de espinacas, queso feta y nueces.</p>
        <h2>Cena:</h2>
        <p>- Brochetas de camarones con vegetales a la parrilla.</p>
        </body>
        </html>
        """
        pdfkit.from_string(contenido, 'dieta_mantener_peso.pdf')


    # -----------------------------------------Problemas medicos/ Sin actividad fisica ------------------------------------------------------
    @Rule(Dieta(objetivo="perder peso"),
        Dieta(actividad_fisica="no"),
        Dieta(problemas_medicos="si"),
        Dieta(embarazo="no"))
    def dieta_para_sedentario_medico(self):
        limpiar_pantalla()
        contenido = """
        <html>
        <head><title>Dieta para una vida sedentaria: [Perder Peso - Problemas médicos]</title></head>
        <body>
        <h1>Dieta para una vida sedentaria: [Perder Peso - Problemas médicos]</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con trozos de frutas frescas.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de pollo a la parrilla con vegetales variados.</p>
        <h2>Cena:</h2>
        <p>- Pescado al horno con brócoli al vapor.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de espinacas, plátano y leche de almendras.</p>
        <h2>Almuerzo:</h2>
        <p>- Filete de ternera a la plancha con ensalada de tomate y pepino.</p>
        <h2>Cena:</h2>
        <p>- Sopa de verduras casera.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Tostadas de pan integral con aguacate y tomate.</p>
        <h2>Almuerzo:</h2>
        <p>- Lentejas estofadas con verduras.</p>
        <h2>Cena:</h2>
        <p>- Pollo al horno con espárragos.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Avena cocida con nueces y un poco de miel.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón a la plancha con ensalada de espinacas y quinoa.</p>
        <h2>Cena:</h2>
        <p>- Ensalada de garbanzos con atún en agua.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Omelette de claras de huevo con espinacas y champiñones.</p>
        <h2>Almuerzo:</h2>
        <p>- Tortilla de patatas con ensalada verde.</p>
        <h2>Cena:</h2>
        <p>- Pavo al horno con puré de calabaza.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con frutas y un puñado de almendras.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de pasta integral con vegetales asados.</p>
        <h2>Cena:</h2>
        <p>- Sopa de calabaza y zanahoria.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Pan integral con queso fresco y rodajas de tomate.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo asado con patatas al horno y ensalada mixta.</p>
        <h2>Cena:</h2>
        <p>- Pescado al horno con espárragos y batata al vapor.</p>
        </body>
        </html>
        """
        pdfkit.from_string(contenido, 'dieta_sedentario_medico.pdf')
    


    @Rule(Dieta(objetivo="mantener peso"),
        Dieta(actividad_fisica="no"),
        Dieta(problemas_medicos="si"),
        Dieta(embarazo="no"))
    def dieta_para_sedentario_medico_mantenerpeso(self):
        limpiar_pantalla()
        contenido = """
        <html>
        <head><title>Dieta para una vida sedentaria: [Mantener Peso - Problemas médicos]</title></head>
        <body>
        <h1>Dieta para una vida sedentaria: [Mantener Peso - Problemas médicos]</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con trozos de frutas frescas y granola.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de quinoa con vegetales asados.</p>
        <h2>Cena:</h2>
        <p>- Pechuga de pollo a la plancha con espárragos al vapor.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de espinacas, piña y jengibre.</p>
        <h2>Almuerzo:</h2>
        <p>- Sopa de verduras casera.</p>
        <h2>Cena:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Tostadas de pan integral con aguacate y huevo pochado.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de garbanzos con atún en agua.</p>
        <h2>Cena:</h2>
        <p>- Berenjenas al horno con tomate y queso fresco.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Avena cocida con trozos de manzana y canela.</p>
        <h2>Almuerzo:</h2>
        <p>- Filete de pavo a la plancha con ensalada de espinacas y nueces.</p>
        <h2>Cena:</h2>
        <p>- Tortilla de claras de huevo con espárragos.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con plátano y un puñado de almendras.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de pollo con quinoa y vegetales frescos.</p>
        <h2>Cena:</h2>
        <p>- Pescado al horno con espárragos y batata al vapor.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Pan integral con queso cottage y rodajas de tomate.</p>
        <h2>Almuerzo:</h2>
        <p>- Lentejas estofadas con verduras.</p>
        <h2>Cena:</h2>
        <p>- Pollo al curry con arroz integral y vegetales al vapor.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Omelette de claras de huevo con espinacas y champiñones.</p>
        <h2>Almuerzo:</h2>
        <p>- Filete de salmón a la plancha con ensalada de espinacas y aguacate.</p>
        <h2>Cena:</h2>
        <p>- Sopa de calabaza y zanahoria.</p>
        </body>
        </html>
        """
        pdfkit.from_string(contenido, 'dieta_sedentario_medico_mantenerpeso.pdf')



    @Rule(Dieta(objetivo="ganar peso"),
        Dieta(actividad_fisica="no"),
        Dieta(problemas_medicos="si"),
        Dieta(embarazo="no"))
    def dieta_para_sedentario_medico_ganarpeso(self):
        limpiar_pantalla()
        contenido = """
        <html>
        <head><title>Dieta para una vida sedentaria: [Ganar Peso - Problemas médicos]</title></head>
        <body>
        <h1>Dieta para una vida sedentaria: [Ganar Peso - Problemas médicos]</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de plátano, avena y leche entera.</p>
        <h2>Almuerzo:</h2>
        <p>- Pasta integral con salsa de tomate y albóndigas de carne.</p>
        <h2>Cena:</h2>
        <p>- Salmón al horno con batata asada.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Tostadas de pan integral con mantequilla de maní y plátano en rodajas.</p>
        <h2>Almuerzo:</h2>
        <p>- Arroz con pollo al curry y verduras salteadas.</p>
        <h2>Cena:</h2>
        <p>- Ensalada de pasta con atún, mayonesa y guisantes.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Tortilla de huevos enteros con aguacate y tomate.</p>
        <h2>Almuerzo:</h2>
        <p>- Estofado de carne con patatas y zanahorias.</p>
        <h2>Cena:</h2>
        <p>- Pizza casera con base de masa integral, queso y vegetales.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur griego con miel y nueces.</p>
        <h2>Almuerzo:</h2>
        <p>- Pechuga de pollo empanizada con puré de papas.</p>
        <h2>Cena:</h2>
        <p>- Lasaña de carne con espinacas y queso.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con plátano, nueces y leche entera.</p>
        <h2>Almuerzo:</h2>
        <p>- Hamburguesa casera de carne con queso, aguacate y ensalada.</p>
        <h2>Cena:</h2>
        <p>- Tacos de pescado con guacamole y arroz.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Panqueques de avena con miel y frutas frescas.</p>
        <h2>Almuerzo:</h2>
        <p>- Risotto de champiñones con pollo a la parrilla.</p>
        <h2>Cena:</h2>
        <p>- Rollitos de carne rellenos de queso y espinacas.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Huevos revueltos con queso cheddar y jamón.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo asado con patatas asadas y brócoli al vapor.</p>
        <h2>Cena:</h2>
        <p>- Sándwich de pavo, queso y aguacate con ensalada.</p>
        </body>
        </html>
        """
        pdfkit.from_string(contenido, 'dieta_sedentario_medico_ganarpeso.pdf')




    #--------------------Fin dietas con problemas medicos---------------------------------
    #-------------------------------Dietas Embarazo ----------------------------------------------------
    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo(self):
        limpiar_pantalla()
        contenido = """
        <html>
        <head><title>Dieta para embarazo [Activa]</title></head>
        <body>
        <h1>Dieta para embarazo [Activa]</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con yogur bajo en grasa.</p>
        <p>- Tostadas integrales con aguacate y huevo pochado.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con espinacas, plátano y leche de almendras.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>
        <p>- Tacos de pescado con tortillas de maíz, repollo rallado y salsa de yogur.</p>
        <h2>Cena:</h2>
        <p>- Avena cocida con rodajas de manzana, canela y almendras.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con yogur bajo en grasa.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con granola y frutos rojos.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con espinacas, plátano y leche de almendras.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con yogur bajo en grasa.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>
        <p>- Tacos de pescado con tortillas de maíz, repollo rallado y salsa de yogur.</p>
        <h2>Cena:</h2>
        <p>- Avena cocida con rodajas de manzana, canela y almendras.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con granola y frutos rojos.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor.</p>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <h2>Cena:</h2>
        <p>- Té de hierbas con tostadas integrales y mermelada sin azúcar añadido.</p>
        </body>
        </html>
        """
        # Nombre del archivo de salida PDF
        nombre_archivo_pdf = 'dieta_para_embarazo.pdf'

        # Convertir HTML a PDF utilizando la función separada
        convertir_html_a_pdf(contenido, nombre_archivo_pdf)

    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="no"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo_sedentaria(self):
        limpiar_pantalla()

        contenido = """
        <html>
        <head><title>Dieta para embarazo [sedentaria]</title></head>
        <body>
        <h1>Dieta para embarazo [sedentaria]</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Té verde con tostadas integrales y aguacate.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de espinacas, tomate y pechuga de pollo a la plancha.</p>
        <h2>Cena:</h2>
        <p>- Sopa de verduras con un trozo de pan integral.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con granola y frutos rojos.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <h2>Cena:</h2>
        <p>- Ensalada de garbanzos con tomate, pepino y aderezo de limón.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con espinacas.</p>
        <h2>Almuerzo:</h2>
        <p>- Pavo al horno con ensalada verde.</p>
        <h2>Cena:</h2>
        <p>- Tortilla de claras de huevo con champiñones y espinacas.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Avena cocida con rodajas de manzana y canela.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de quinoa con vegetales asados.</p>
        <h2>Cena:</h2>
        <p>- Pechuga de pollo a la plancha con espárragos.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Tostadas integrales con mantequilla de almendras y plátano en rodajas.</p>
        <h2>Almuerzo:</h2>
        <p>- Atún al natural con ensalada de tomate y aguacate.</p>
        <h2>Cena:</h2>
        <p>- Berenjenas al horno con queso fresco.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Smoothie de bayas con espinacas.</p>
        <h2>Almuerzo:</h2>
        <p>- Lentejas estofadas con verduras.</p>
        <h2>Cena:</h2>
        <p>- Ensalada de salmón ahumado con aguacate y pepino.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Té de hierbas con tostadas integrales y mermelada sin azúcar añadido.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor.</p>
        <h2>Cena:</h2>
        <p>- Crema de calabaza con un trozo de pan integral.</p>
        </body>
        </html>
        """
        nombre_archivo_pdf = 'dieta_para_embarazo_sedentaria.pdf'
        print("Presiona enter para generar el PDF de la dieta \n")
        input()
        # Convertir HTML a PDF utilizando la función separada
        convertir_html_a_pdf(contenido, nombre_archivo_pdf)
       
    #---------------------PROBLEMAS MEDICOS-----------------------
    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="si"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo_medico_fisico(self):
        limpiar_pantalla()
        contenido = """
        <html>
        <head><title>Dieta para embarazo [Problemas medicos - Actividad fisica]</title></head>
        <body>
        <h1>Dieta para embarazo [Problemas medicos - Actividad fisica]</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con yogur bajo en grasa.</p>
        <p>- Tostadas integrales con aguacate y huevo pochado.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con espinacas, plátano y leche de almendras.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>
        <p>- Tacos de pescado con tortillas de maíz, repollo rallado y salsa de yogur.</p>
        <h2>Cena:</h2>
        <p>- Avena cocida con rodajas de manzana, canela y almendras.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con yogur bajo en grasa.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con granola y frutos rojos.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de proteínas con espinacas, plátano y leche de almendras.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <p>- Ensalada de quinoa con vegetales mixtos y aderezo de limón y aceite de oliva.</p>
        <h2>Cena:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con yogur bajo en grasa.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>
        <p>- Tacos de pescado con tortillas de maíz, repollo rallado y salsa de yogur.</p>
        <h2>Cena:</h2>
        <p>- Avena cocida con rodajas de manzana, canela y almendras.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con granola y frutos rojos.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor y una ensalada de tomate y pepino.</p>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <h2>Cena:</h2>
        <p>- Té de hierbas con tostadas integrales y mermelada sin azúcar añadido.</p>
        </body>
        </html>
        """
        nombre_archivo_pdf = 'dieta_para_embarazo_medico_fisico.pdf'
        print("Presiona enter para generar el PDF de la dieta \n")
        input()
        # Convertir HTML a PDF utilizando la función separada
        convertir_html_a_pdf(contenido, nombre_archivo_pdf)

        
    @Rule(Dieta(objetivo="salud"),
          Dieta(actividad_fisica="no"),
          Dieta(problemas_medicos="si"),
          Dieta(embarazo="si"))
    def dieta_para_embarazo_nofisico_medico(self):
        limpiar_pantalla()
        contenido = """
        <html>
        <head><title>Dieta para embarazo [Problemas medicos - sedentaria]</title></head>
        <body>
        <h1>Dieta para embarazo [Problemas medicos - sedentaria]</h1>
        <h1>Lunes:</h1>
        <h2>Desayuno:</h2>
        <p>- Té verde con tostadas integrales y aguacate.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de espinacas, tomate y pechuga de pollo a la plancha.</p>
        <h2>Cena:</h2>
        <p>- Sopa de verduras con un trozo de pan integral.</p>

        <h1>Martes:</h1>
        <h2>Desayuno:</h2>
        <p>- Yogur natural con granola y frutos rojos.</p>
        <h2>Almuerzo:</h2>
        <p>- Salmón al horno con brócoli al vapor.</p>
        <h2>Cena:</h2>
        <p>- Ensalada de garbanzos con tomate, pepino y aderezo de limón.</p>

        <h1>Miércoles:</h1>
        <h2>Desayuno:</h2>
        <p>- Batido de frutas con espinacas.</p>
        <h2>Almuerzo:</h2>
        <p>- Pavo al horno con ensalada verde.</p>
        <h2>Cena:</h2>
        <p>- Tortilla de claras de huevo con champiñones y espinacas.</p>

        <h1>Jueves:</h1>
        <h2>Desayuno:</h2>
        <p>- Avena cocida con rodajas de manzana y canela.</p>
        <h2>Almuerzo:</h2>
        <p>- Ensalada de quinoa con vegetales asados.</p>
        <h2>Cena:</h2>
        <p>- Pechuga de pollo a la plancha con espárragos.</p>

        <h1>Viernes:</h1>
        <h2>Desayuno:</h2>
        <p>- Tostadas integrales con mantequilla de almendras y plátano en rodajas.</p>
        <h2>Almuerzo:</h2>
        <p>- Atún al natural con ensalada de tomate y aguacate.</p>
        <h2>Cena:</h2>
        <p>- Berenjenas al horno con queso fresco.</p>

        <h1>Sábado:</h1>
        <h2>Desayuno:</h2>
        <p>- Smoothie de bayas con espinacas.</p>
        <h2>Almuerzo:</h2>
        <p>- Lentejas estofadas con verduras.</p>
        <h2>Cena:</h2>
        <p>- Ensalada de salmón ahumado con aguacate y pepino.</p>

        <h1>Domingo:</h1>
        <h2>Desayuno:</h2>
        <p>- Té de hierbas con tostadas integrales y mermelada sin azúcar añadido.</p>
        <h2>Almuerzo:</h2>
        <p>- Pollo a la parrilla con espárragos al vapor.</p>
        <h2>Cena:</h2>
        <p>- Crema de calabaza con un trozo de pan integral.</p>
        </body>
        </html>
        """
        nombre_archivo_pdf = 'dieta_para_embarazo_nofisico_medico.pdf'
        print("Presiona enter para generar el PDF de la dieta \n")
        input()

        # Convertir HTML a PDF utilizando la función separada
        convertir_html_a_pdf(contenido, nombre_archivo_pdf)
        

    #------------------Fin Dietas Embarazo ----------------------------------------------------
    # Regla por defecto
    @Rule(AS.f1 << Dieta(objetivo=MATCH.o),
        AS.f2 << Dieta(actividad_fisica=MATCH.af),
        AS.f3 << Dieta(problemas_medicos=MATCH.pm),
        AS.f4 << Dieta(embarazo=MATCH.e),
        TEST(lambda o, af, pm, e: o not in ["si", "no"] or af not in ["si", "no"] or pm not in ["si", "no"] or e not in ["si", "no"]))
    def default_rule(self, f1, f2, f3, f4, o, af, pm, e):
        print("Lo siento, no hay dietas disponibles para tus respuestas.")




if __name__ == "__main__":
    engine = SistemaExperto()
    engine.reset()
    is_correct = False
    while not is_correct:
        objetivo = input("1. ¿Cuál es tu objetivo del plan alimenticio? (perder peso / mantener peso / ganar peso / salud): ").lower()
        actividad_fisica = input("2. ¿Realizas alguna actividad física? (Si / No): ").lower()
        problemas_medicos = input("3. ¿Sufres de algún problema médico? (Si / No): ").lower()
        embarazo = input("4. ¿Te encuentras en etapa de gestación? (si / No): ").lower()

        if objetivo in ["perder peso", "mantener peso", "ganar peso", "salud"]:
            if actividad_fisica in ["si", "no"]:
                if problemas_medicos in ["si", "no"]:
                    if embarazo in ["si", "no"]:
                        is_correct = True
                    else:
                        print("Respuesta incorrecta para la pregunta 4.")
                else:
                    print("Respuesta incorrecta para la pregunta 3.")
            else:
                print("Respuesta incorrecta para la pregunta 2.")
        else:
            print("Respuesta incorrecta para la pregunta 1.")

        if not is_correct:
            print("Por favor, ingresa respuestas válidas.\n")
            input()
            limpiar_pantalla()

    engine.declare(Dieta(objetivo=objetivo, actividad_fisica=actividad_fisica, problemas_medicos=problemas_medicos, embarazo=embarazo))
    engine.run()
