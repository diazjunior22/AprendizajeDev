import React from 'react'
import { use, useEffect, useState } from "react"

// fetch es una función nativa de JavaScript que sirve para hacer peticiones HTTP (por ejemplo, para consumir una API).
// 🔹 ¿Qué significa await fetch?
// fetch es asíncrono (tarda un tiempo en responder), así que para esperar la respuesta, usamos await.
export const ConsumoApi = () => {
    const [data , setData] = useState("")
    const getData = async ()  => {
        try {
            const respuestas = await fetch("https://api.sampleapis.com/beers/ale")
            const json = await respuestas.json()
            setData(json)
        }
        catch (error) {
            setData(error.mensaje)
        }
    }

    useEffect(() => {
        getData()
    } , [])


  return (
    <pre >

    {JSON.stringify(data, null ,2)}


    </pre>
  )
}



// 🔹 ¿Qué significa async?
// async es una palabra clave en JavaScript que se usa para declarar una función asíncrona.
// Cuando pones async antes de una función, le estás diciendo a JavaScript:
// “Esta función puede tardar en ejecutarse porque va a hacer cosas como fetch, setTimeout, o procesos que toman tiempo, así que déjala trabajar en segundo plano”.
// Además:
// Una función async SIEMPRE devuelve una Promesa.
// Dentro de una función async puedes usar await para esperar resultados.