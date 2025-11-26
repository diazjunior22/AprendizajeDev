import React, { useState } from 'react'

export const UseState02 = () => {
    const [textoBotton , setTextoBotton] = useState('Hacer Click')
    const cambiarTexto = () => {
        setTextoBotton(textoBotton === 'Hacer Click'? 'HAZ HECHO CLICK' : 'Hacer Click')
        
    }



  return (
    <button onClick={cambiarTexto}>{textoBotton}</button>
  )
}
