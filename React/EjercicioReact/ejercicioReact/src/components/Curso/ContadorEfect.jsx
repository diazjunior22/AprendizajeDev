import { use, useEffect, useState } from "react"
import React  from 'react'

export const ContadorEfect = () => {
    const [contador , setContador] = useState(0)

    useEffect(() => {
        console.log('el contador es :' + contador)
        alert(contador)
    } ,[contador])
  return (
    <div>
        <p>{contador}</p>
        <button onClick={() => setContador(contador + 1)}>Incrementar</button>



    </div>
  )
}
