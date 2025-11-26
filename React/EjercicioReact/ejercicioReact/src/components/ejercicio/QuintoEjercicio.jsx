import React, { useState } from 'react'

export const QuintoEjercicio = () => {
       const [contador, setContador]= useState(0)

       function restar( ) {
          setContador(contador-1)

       }
       function sumar( ) {
          setContador(contador+1)

       }

  return (
    <div>
            <h1>{contador}</h1>
            <button onClick={sumar}  disabled={contador===10}>
              sumar</button>
            <button onClick={restar} disabled={contador===0}>
              restar</button>

    </div>
  )
}
