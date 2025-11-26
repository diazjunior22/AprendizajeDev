import React, { useState } from 'react'

export const ValidacionContraseña = () => {

    const [contraseña , setContraseña] = useState("")
    const [validar , setValidar] = useState(false)
    // const [mensaje, SetMensaje] = useState('')

    const validarContra =  () => {
        const validarNumero = /\d/.test(contraseña);
        const validarMayuscula = /[A-Z]/.test(contraseña);
        const validarlogitud = contraseña.length >= 9;
        setValidar(validarNumero && validarMayuscula && validarlogitud);
        setContraseña('')
    }

  return (
    <div>

        <input type="text"   value={contraseña}  onChange={(e) => setContraseña(e.target.value)}/>
        <button
            onClick={validarContra} >Confirmar Contraseña</button>
        <p>{validar ?'LA CONTRASEÑA ES CORRECTA' : "LA CONTRASEÑA DEBE TENER ALMENOS 1 MAYUSCULA Y UN NUMERO  Y MAS DE 8 CARACTERES"}</p>




    </div>
  )
}
