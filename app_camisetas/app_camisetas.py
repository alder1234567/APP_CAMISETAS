
import reflex as rx

def index() -> rx.Component:
    return rx.container(
        # Botón para cambiar el tema
        rx.color_mode.button(position="absolute", top="1rem", right="1rem"),
        
        # Contenedor principal de la página
        rx.vstack(
            # Contenedor para el título, texto y botones en la parte superior
            rx.hstack(
                # Columna de imágenes a la izquierda
                rx.vstack(
                    rx.image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ__ZLcyyfdxMS1o1zFQ-o_1KU-MHKntf62xnfppYWwOPU-Xti9roYZRTVsGLjkWfQj3K8&usqp=CAU",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTmk-Tk8NI-oLI7A3GAJcpd1Hjl8dq7wQvw3g&s",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="4",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_right="2rem",  # Espaciado entre las imágenes y el contenido de la derecha
                ),
                
                # Espaciador para centrar el título y texto
                rx.spacer(flex="1"),  # Esto asegura que el contenido se quede centrado
                
                # Contenedor para el título, texto y botones en la parte derecha
                rx.vstack(
                    # Contenedor con título y texto
                    rx.vstack(
                        # Título centrado
                        rx.heading("¡Bienvenido a app camisetas!", size="2xl", color="white", text_align="center"),
                        
                        # Descripción centrada
                        rx.text(
                            "app camisetas  es una aplicación móvil diseñada para conectar a los amantes de la diseños con una amplia gama de camisetas . "
                            "Su nombre evoca la imagen de un manantial de diseños , haciendo referencia a la abundancia y variedad de opciones que ofrece la aplicación.",
                            size="md",
                            color="white",
                            max_width="40rem",
                            text_align="center",  # Centrado del texto
                            margin_top="1rem",  # Margen superior para el texto
                        ),
                        spacing="6",  # Espaciado entre el título y el texto
                        align="center",  # Alineación centrada
                    ),
                    
                    # Botones en la parte superior derecha
                    rx.hstack(
                        # Botón "Regístrate aquí"
                        rx.link(
                            rx.button("¡Regístrate aquí!", color_scheme="green"),
                            href="https://forms.gle/fKuHUqbSzgsf9EM16",
                            is_external=True,
                        ),  
                        # Botón "Facebook" 
                        rx.link(
                            rx.button(rx.icon(tag="facebook"), color_scheme="blue"),
                            href="https://facebook.com",
                            is_external=True,
                        ),
                        # Botón "Instagram"
                        rx.link(
                            rx.button(rx.icon(tag="instagram"), color_scheme="pink"),
                            href="https://instagram.com",
                            is_external=True,
                        ),
                        spacing="4",  # Espaciado entre los botones
                        align="end",  # Alineación de los botones a la derecha
                    ),
                    
                    # Espaciado para que los botones no se peguen al contenido
                    margin_top="2rem",
                ),
                
                # Columna de imágenes a la derecha
                rx.vstack(
                    rx.image(
                        src="data:image/jpeg;base64,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",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="data:image/jpeg;base64,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",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="4",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_left="2rem",  # Espaciado entre las imágenes y el contenido de la izquierda
                ),
                
                spacing="6",  # Espaciado general entre las columnas
                justify="space-between",  # Distribución equitativa de espacio entre las columnas
                align="center",  # Alineación centrada entre las columnas
            ),
            
            # Fondo y padding de la página
            bg="#000000",  # Fondo negro
            padding="2rem",
            min_height="100vh",  # Asegura que la página ocupe toda la altura de la pantalla
        ),
    )


# Crear la aplicación
app = rx.App()
app.add_page(index) 