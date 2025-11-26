import React, { useState } from 'react'

export const Prueba = () => {
    const [nombre, setNombre]  = useState('')
    const [color,setColor] = useState('black')


     const nombreCambiar = (e) => {
        setNombre(e.target.value)
  
     }



  return (
    <div>
        <h1>TU NOMBRE ES: {nombre}</h1>
        <input type="text" value={nombre} onChange={nombreCambiar} /> 
        <h2>ELIGE UN COLOR DEL TEXTO </h2>




    </div>
  )
}
