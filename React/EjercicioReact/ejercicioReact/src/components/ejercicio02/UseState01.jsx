import React, { useState } from 'react'

export const UseState01 = () => {
    const [textoBotton, setTextoBotton] = useState('Hacer Click')
            // VARIABLE   FUNCION                     VALOR ACTUAL
    const cambiarTexto = () => {
        setTextoBotton('CLICK HECHO')
        
    }


  return (
    <div>
        <button onClick={cambiarTexto}>{textoBotton}</button>

    </div>
  )
}
