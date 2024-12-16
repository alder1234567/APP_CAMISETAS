import reflex as rx

def index() -> rx.Component:
    return rx.container(
        # Fondo completo de la página
        rx.box(
            # Contenedor general con fondo cielo
            rx.vstack(
                # Sección de bienvenida con un fondo diferente
                rx.box(
                    rx.vstack(
                        rx.heading("¡Bienvenido a App Camisetas!", size="3xl", color="white", text_align="center"),
                        rx.text(
                            "Conecta con diseños únicos y personaliza tu estilo con nuestra amplia gama de camisetas. "
                            "Explora opciones creativas y únete a nuestra comunidad.",
                            size="lg",
                            color="white",
                            max_width="50rem",
                            text_align="center",
                            margin_top="1rem",
                        ),
                        spacing="4",  # Espaciado entre elementos
                        align="center",
                    ),
                    bg="#4A90E2",  # Fondo azul
                    padding="3rem",
                    width="100%",  # Ocupa todo el ancho
                ),
                
                # Zona principal con imágenes y botones
                rx.hstack(
                    # Imágenes en la izquierda
                    rx.vstack(
                        rx.image(
                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ__ZLcyyfdxMS1o1zFQ-o_1KU-MHKntf62xnfppYWwOPU-Xti9roYZRTVsGLjkWfQj3K8&usqp=CAU",
                            alt="Diseño 1",
                            border_radius="lg",
                            box_shadow="lg",
                            max_width="15rem",
                        ),
                        rx.image(
                            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmk-Tk8NI-oLI7A3GAJcpd1Hjl8dq7wQvw3g&s",
                            alt="Diseño 2",
                            border_radius="lg",
                            box_shadow="lg",
                            max_width="15rem",
                        ),
                        spacing="6",
                        align="center",
                    ),
                    
                    # Zona central con botón con texto
                     rx.vstack(
                        rx.box(
                            rx.button(
                                rx.text("¡Regístrate aquí!"),
                                size="lg",
                                color_scheme="teal",
                                text_align="center",
                                width="100%",
                            ),
                            align="center",
                            width="auto",
                            padding="1rem",
                        ),
                        rx.hstack(
                            rx.link(
                                rx.button(rx.icon(tag="facebook"), size="lg", color_scheme="blue"),
                                href="https://facebook.com",
                                is_external=True,
                            ),
                            rx.link(
                                rx.button(rx.icon(tag="instagram"), size="lg", color_scheme="pink"),
                                href="https://instagram.com",
                                is_external=True,
                            ),
                            spacing="4",
                        ),
                        spacing="6",
                        align="center",
                    ),
                    
                    # Imágenes en la derecha
                    rx.vstack(
                        rx.image(
                            src="https://i.pinimg.com/736x/59/62/8f/59628f5c29c6b0aad6537b96eb4d262f.jpg",
                            alt="Diseño 3",
                            border_radius="lg",
                            box_shadow="lg",
                            max_width="15rem",
                        ),
                        rx.image(
                            src="https://i.pinimg.com/736x/48/7d/51/487d51d0eb5b5dee71a03312d35f1d75.jpg",
                            alt="Diseño 4",
                            border_radius="lg",
                            box_shadow="lg",
                            max_width="15rem",
                        ),
                        spacing="6",
                        align="center",
                    ),
                    
                    spacing="8",
                    padding="2rem",
                ),
                
                # Pie de página con información adicional
                rx.box(
                    rx.text(
                        "Explora, personaliza y encuentra tus camisetas favoritas con App Camisetas. ¡Únete ahora!",
                        size="md",
                        color="white",
                        text_align="center",
                        padding="1rem",
                    ),
                    bg="#2D4C7C",  # Fondo azul oscuro
                    width="100%",
                    padding="2rem",
                ),
            ),
            bg="#87CEEB",  # Fondo color cielo
            min_height="100vh",  # Altura completa de la pantalla
        ),
    )

# Crear la aplicación
app = rx.App()
app.add_page(index)
