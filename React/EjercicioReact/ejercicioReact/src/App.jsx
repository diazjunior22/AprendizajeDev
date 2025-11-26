import { ConsumoApi } from "./components/Curso/ConsumoApi"
import { Contador } from "./components/Curso/Contador"
import { ContadorEfect } from "./components/Curso/ContadorEfect"
import { Controles } from "./components/Curso/Controles"
import { Formulario } from "./components/Curso/Formulario"
import { InputText } from "./components/Curso/InputText"
import { MensajeCondicional } from "./components/Curso/MensajeCondicional"
import { MensajeConsola } from "./components/Curso/MensajeConsola"
import { Props } from "./components/Curso/Props"
import { Session } from "./components/Curso/session"
import { PrimerEjercicio } from "./components/ejercicio/PrimerEjercicio"
import { QuintoEjercicio } from "./components/ejercicio/QuintoEjercicio"
import { SegundoEjercicio } from "./components/ejercicio/SegundoEjercicio"
import { UseState01 } from "./components/ejercicio02/UseState01"
import { UseState02 } from "./components/ejercicio02/UseState02"
import { UseState03 } from "./components/ejercicio02/UseState03"
import { UseState04 } from "./components/ejercicio02/UseState04"
import { UseState05 } from "./components/ejercicio02/UseState05"
import { ListadoTareas } from "./components/ejercicio03/ListadoTareas"
import { Prueba } from "./components/ejercicio03/Prueba"
import { UseStateInput } from "./components/ejercicio03/UseStateInput"
import { UseStateinput02 } from "./components/ejercicio03/UseStateinput02"
import { ValidacionContraseña } from "./components/ejercicio03/ValidacionContraseña"
import { useState } from "react"

function App() {

  const nombre = 'Junior'
  const apellido = 'diaz'
  const [contador , setContador] = useState(0)
  

  return (
    <>

      <PrimerEjercicio/>
      <SegundoEjercicio/>
      <QuintoEjercicio/>
       <UseState01/>
       <UseState02/>
       <UseState04/>
       <UseState03/>
       <UseState05/>
       <UseStateInput/>
       <UseStateinput02/>
      <Prueba/>
      <ListadoTareas/>
      <ValidacionContraseña/>

      <Props  nombre={nombre} apellido={apellido}/>
      <hr />
      <Contador contador={contador}/>
      <Controles  setContador={setContador}/>
      <hr />
      <InputText/>
      <hr/>
      <Formulario/>
      <MensajeCondicional/>
      <hr/>
      <Session/>
      <h1>USE EFECT</h1>
      <MensajeConsola/>
      <ContadorEfect/>
      <hr/>
    <ConsumoApi/>



    </>
  )
}

export default App
