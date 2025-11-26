import React from 'react'

export const Controles = ({setContador}) => {

  return (
    <div>Controles

        <button onClick={() => setContador(prev => prev + 1)}>Sumar</button>
        <button onClick={() => setContador(prev => prev - 1)}>Quitar</button>
        <button onClick={() => setContador(0)}>Limpiar</button>

    </div>
    
  )
}
