import React , {useEffect} from 'react'

export const MensajeConsola = () => {
    useEffect(() => {
        console.log('EL COMPONENTE RENDERIZADO')
    }, [])
  return (
    <div>
        Mira La CONSOLA PARA VER EL MENSAJE
    </div>
  )
}
