import React , {useState} from 'react'

export const MensajeCondicional = () => {
    const [mensaje, setMensaje] = useState('')




  return (
    <div>
       <input type="text" placeholder='Escribe un mensaje' value={mensaje}  onChange={(e) => setMensaje(e.target.value)



       }/>


       {mensaje ? <p> tu texto es : {mensaje}</p> : <p>No has escrito nada</p>}
       {mensaje && <button onClick={() =>{alert("  mensaje enviado  " + mensaje)}}>Enviar</button>}
    </div>

  )


}
