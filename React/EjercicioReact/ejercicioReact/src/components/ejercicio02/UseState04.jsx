import { useState } from 'react'

export const UseState04 = () => {
    const [mensaje, setMensaje] = useState('Hacer Click')
    const [mostrarMensajeAlternativo, setMostrarMensajeAlternativo] = useState(true)
    const [colorFondo, setColorFondo] = useState('green')

    const alternarMensaje = () => {
        setMostrarMensajeAlternativo(!mostrarMensajeAlternativo)
        setMensaje(mostrarMensajeAlternativo ? 'hola' : 'adios')
        setColorFondo(mostrarMensajeAlternativo ? 'lightblue' : 'yellow') // <-- NUEVA LÍNEA
    }

    return (
      <div style={{backgroundColor: colorFondo}}>
        <button onClick={alternarMensaje}>
            {mensaje}
        </button>
      </div>
    )
}
