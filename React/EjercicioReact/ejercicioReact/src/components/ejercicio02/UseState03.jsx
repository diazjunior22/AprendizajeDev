import React, { useState } from 'react' // Importamos React y el hook useState para manejar estados en el componente

export const UseState03 = () => { // Declaramos un componente funcional llamado MiComponente

  const [mensaje, setMensaje] = useState('Hacer Click') 
  // Declaramos un estado llamado "mensaje" con valor inicial 'Hacer Click'
  // setMensaje es la función que permite cambiar el valor de "mensaje"

  const [mostrarMensajeAlternativo, setMostrarMensajeAlternativo] = useState(true)
  // Declaramos otro estado booleano que inicia en true
  // Este estado solo sirve para saber si debemos mostrar "hola" o "adios"

  const alternarMensaje = () => { // Función que se ejecuta al hacer click en el botón

    setMostrarMensajeAlternativo(!mostrarMensajeAlternativo) 
    // Invertimos el estado booleano: si era true pasa a false, y si era false pasa a true

    setMensaje(mostrarMensajeAlternativo ? 'hola' : 'adios') 
    // Usamos un operador ternario:
    // Si mostrarMensajeAlternativo es true → ponemos mensaje = 'hola'
    // Si es false → mensaje = 'adios'
  }

  return (
    <button onClick={alternarMensaje}>{mensaje}</button> 
    // Renderizamos un botón que muestra el texto guardado en "mensaje"
    // Al hacer click, se ejecuta la función alternarMensaje
  )
}
