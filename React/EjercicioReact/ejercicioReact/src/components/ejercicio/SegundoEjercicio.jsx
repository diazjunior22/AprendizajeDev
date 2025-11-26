import React from 'react'

export const SegundoEjercicio = () => {
    function enviarMensaje() {
        console.log("mensaje enviado")
    }

  return (
    <div>
        <button onClick={enviarMensaje}>
                enviar mensaje
        </button>
        
    </div>
    
    
  )
}
