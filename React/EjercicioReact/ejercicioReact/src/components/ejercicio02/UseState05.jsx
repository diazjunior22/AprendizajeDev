import React, {  useState } from 'react' 
// Importamos React y el hook useState para poder crear estados dentro del componente

export const UseState05 = () => { 
    // Definimos un componente funcional llamado UseState05
    const [mensaje, setMensaje] = useState('Hacer Click')
    // Estado "mensaje" que controla lo que se muestra en el botón
    // Comienza con el texto 'Hacer Click'
    const [nuevoMensaje , setNuevoMensaje] = useState('')
    // Estado "nuevoMensaje" que guarda lo que el usuario escribe en el input
    // Comienza como un string vacío
    const cambiarMensaje = () => { 
        // Función que se ejecuta cuando se hace click en el botón
        setMensaje(nuevoMensaje ||'Hacer Click')
        // Aquí usamos el operador || (OR lógico)
        // Si "nuevoMensaje" tiene un valor (no está vacío), se usa ese valor
        // Si "nuevoMensaje" está vacío o es falso, se usa 'Hacer Click'
        // Ejemplo: nuevoMensaje = 'Hola' → mensaje = 'Hola'
        // Ejemplo: nuevoMensaje = '' → mensaje = 'Hacer Click'
        setNuevoMensaje('')
        // Esto limpia el input después de hacer el cambio
    }
    const cambiarMensajeInput = (e) => {
        // Función que se ejecuta cada vez que el usuario escribe en el input
        setNuevoMensaje(e.target.value)
        // Actualiza "nuevoMensaje" con el texto que el usuario está escribiendo
    }

  return (
    <div>
        <input
        type='text'
        placeholder='Cambiar El Nombre Del Bottton'
        value={nuevoMensaje}
        onChange={cambiarMensajeInput}
        />
        {/* Input controlado por el estado "nuevoMensaje"
            - placeholder = texto que se ve cuando está vacío
            - value = lo que actualmente está en el estado nuevoMensaje
            - onChange = función que actualiza el estado cuando se escribe */}

        <button onClick={cambiarMensaje}>
            {mensaje}
        </button>
        {/* Botón que al hacer click ejecuta cambiarMensaje
            Y muestra el texto que está en "mensaje" */}

    </div>
  )
}
