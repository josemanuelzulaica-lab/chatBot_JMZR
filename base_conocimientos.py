# Esta es la base de conocimiento que ayudará a responder las dudas de los clientes de acuerdo a las intenciones detectadas. Esta basada en las 
# preguntas frecuentes registradas al día de hoy, si se llegan a detectar nuevas preguntas frecuentes de los clientes,
#  aqui se debe agregar la intención junto con su respuesta

intenciones = {
    "saludo": {
        "dudas": [
            "hola",
            "buenos dias",
            "necesito ayuda",
            "buenas tardes",
            "tengo dudas",
            "ayudame"
        ],
        "respuesta": "Hola, muy buen día, dime ¿En qué te puedo ayudar?"
    },

   
    "duda_tasa_interes": {
        "dudas": [
            "que es la tasa de interes",
            " que significa tasa de interes",
            "para que sirve la tasa de interes"
        ],
        "respuesta": "Es el porcentaje que se utiliza para calcular los intereses que pueden generarse por el uso de tu crédito."
    },

    "duda_fecha_corte": {
        "dudas": [
            "que es la fecha de corte",
            "cuando es el corte",
            "que significa fecha de corte"
        ],
        "respuesta": "Es el día en que termina el periodo de registro de movimientos de tu tarjeta para poder generar tu estado de cuenta."
    },

    "duda_fecha_pago": {
        "dudas": [
            "que significa la fecha limite de pago",
            "que es la fecha de pago",
            "para que sirve la fecha limite de pago"
        ],
        "respuesta": "Es el último día que tienes para realizar el pago de tu tarjeta correspondiente al periodo."
    },

    "duda_pago_minimo": {
        "dudas": [
            "que pasa si solo pago el minimo",
            "que es el pago minimo",
            "para que sirve el pago minimo"
        ],
        "respuesta": "Si pagas el mínimo a tiempo, mantienes tu crédito al corriente, pero generalmente se generan intereses sobre el saldo que quede pendiente."
    },

    "duda_pago_sin_intereses": {
        "dudas": [
            "que es el pago para no generar intereses",
            "cuanto debo pagar para no generar intereses",
            "como evitar pagar intereses"
        ],
        "respuesta": "Es el monto que debes cubrir antes o en tu fecha límite de pago para evitar intereses ordinarios sobre las compras del periodo, conforme a las condiciones de tu tarjeta."
    },

    "duda_calculo_intereses": {
        "dudas": [
            "como se calculan los intereses",
            "como calcula el banco los intereses",
            "como se cobran los intereses"
        ],
        "respuesta": "Se calculan considerando la tasa de interés aplicable y los saldos sujetos a intereses, según las condiciones de tu tarjeta."
    },

    "duda_activacion": {
        "dudas": [
            "como puedo activar mi tarjeta",
            "como activo mi tarjeta",
            "quiero activar mi tarjeta"
        ],
        "respuesta": "Puedes consultar las opciones de activación disponibles en tu App BBVA o en los canales oficiales del banco."
    },

    "duda_tarjeta_digital": {
        "dudas": [
            "para que sirve mi tarjeta digital",
            "que es una tarjeta digital",
            "como funciona la tarjeta digital"
        ],
        "respuesta": "Te permite realizar compras por internet utilizando los datos de tu tarjeta digital, sin necesidad de proporcionar los de tu tarjeta física."
    },

    "duda_cvv_dinamico": {
        "dudas": [
            "donde puedo encontrar mi cvv dinamico",
            "donde esta el cvv dinamico",
            "como consultar mi cvv dinamico"
        ],
        "respuesta": "Puedes consultar el CVV dinámico desde la sección correspondiente a tu tarjeta digital dentro de la App BBVA."
    },

    "duda_compras": {
        "dudas": [
            "puedo seguir comprando con mi tarjeta fisica",
            "puedo pagar en tiendas con mi tarjeta",
            "puedo usar mi tarjeta fisica"
        ],
        "respuesta": "Sí, mientras tu tarjeta esté activa y habilitada, puedes utilizarla en establecimientos que acepten pagos con tarjeta."
    },

    "duda_domiciliaciones": {
        "dudas": [
            "que pasa con mis domiciliaciones si cambia mi tarjeta",
            "debo actualizar mis pagos domiciliados",
            "que pasa con mis suscripciones"
        ],
        "respuesta": "Es posible que debas actualizar los datos de tu tarjeta en los servicios donde tengas registrados pagos recurrentes."
    },

    "duda_reposicion": {
        "dudas": [
            "que pasa con mi tarjeta anterior cuando recibo una nueva",
            "puedo seguir usando mi tarjeta anterior",
            "que pasa cuando me reponen mi tarjeta"
        ],
        "respuesta": "El funcionamiento de la tarjeta anterior dependerá del tipo de reposición. Consulta las condiciones específicas en los canales oficiales de BBVA."
    },

    "despedida": {
        "dudas": [
            "gracias",
            "muchas gracias",
            "eso es todo",
            "adios"
        ],
        "respuesta": "Gracias por utilizar este chat."
    }
}
