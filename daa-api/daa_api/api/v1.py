from flask_restx import Api


api = Api(version='1.0',
		  title='daa-api',
		  description="Esta página contiene información detallada sobre cómo interactuar con nuestra API para acceder a recursos y funcionalidades avanzadas. Para garantizar el acceso adecuado a las rutas y su funcionamiento, es crucial incluir en los headers de cada solicitud el campo 'X-API-KEY', con el valor proporcionado por el administrador. Cada clave de API proporcionada tiene asignadas 200 peticiones por hora. Es esencial tener en cuenta que cada clave está asociada a una base de datos única, lo que significa que cada usuario accede a su propia información exclusiva. Asegúrate de leer detenidamente la información proporcionada para cada endpoint. Se detallan los datos que deben pasarse en cada solicitud, junto con el método correspondiente para optimizar tu interacción con nuestra API. ",
		)