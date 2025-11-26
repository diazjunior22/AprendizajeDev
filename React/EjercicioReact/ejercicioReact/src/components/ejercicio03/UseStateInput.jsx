import React , { useState } from 'react'

export const UseStateInput = () => {
    const [texto, setTexto] = useState('')
    const limite = 50

    const actualizaTexto = (e) => {
        const nuevoTexto = e.target.value
        setTexto(nuevoTexto)
    }
    const  carasteresRestantes = limite - texto.length


  return (
    <div>
        <input type="text" placeholder='Escribe Aqui'
        value={texto}
        onChange={actualizaTexto}
        maxLength={limite}
        />
        <p>Caracteres restantes {carasteresRestantes}</p>




    </div>
  )
}
